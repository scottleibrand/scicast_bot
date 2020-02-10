from time import sleep

from scicast_bot_session.client.scicast_bot_session import SciCastBotSession
from scicast_bot_session.common.utils import scicast_bot_urls
import os
from random import randint
from simple_bot import *
from numpy import allclose

# Simple bot sets up the API KEY and SITE, and defines our functions for us
# TODO: Refactor to base class and inherited

def get_qid() -> Sequence:
    '''Select q, return [qid, history, last_prob, first_prob]
    
    TODO: make this smarter. Dev span is only R5
    '''
    if SITE=='predict':
        raise ValueError('Simple Bot is not rated for production site!')

    while True:
        if SITE=='sandbox':
            qid = randint(2,301)
        elif SITE=='dev':
            qid = randint(1103,1403)
        print(f'Checking qid={qid}.')
        hist = s.get_question_history(qid)
        first_prob = get_nth_prob_from_history(hist, 0)
        last_prob = get_nth_prob_from_history(hist, -1)
        if not allclose(first_prob, last_prob, atol=.005, rtol=.005):
            return qid, hist, last_prob, first_prob

if __name__ == '__main__':
    with SciCastBotSession(base_url=URL, api_key=api_key) as s:
        ri = s.get_round_info()
        print_dict(ri['R6'], f'ROUND 6 INFO')

    while(True):
        with SciCastBotSession(base_url=URL, api_key=api_key) as s:
            assets = s.get_user_info()
            cash, budget = assets['cash'], assets['cash'] * .01
            print(f"___ASSETS: cash: {cash:.1f}, budget: {budget:.1f}")

            q_id, hist, orig_prob, new_prob = get_qid()
            
            # add a trade - using budget to constrain
            print(f"Trading {orig_prob} towards {new_prob} with budget={budget:.1f}.")
            result = s.trade(q_id, new_prob, max_cost=budget, comment='[PriorBot]: nudge towards starting prob.')
            if 'trade' in result.keys():
                print_trade(result, prefix='\t')
            else:
                print(result)

            current_prob = get_latest_prob_from_qid(q_id, s)
            print('\tPost-trade prob:', current_prob)

            # Check assets
            assets = s.get_user_info()
            print_dict(assets, 'POST-TRADE ASSETS')

        sleep(60)
