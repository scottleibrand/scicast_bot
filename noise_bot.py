from time import sleep

from scicast_bot_session.client.scicast_bot_session import SciCastBotSession
from scicast_bot_session.common.utils import scicast_bot_urls
import os
from random import randint
from simple_bot import *

# Simple bot sets up the API KEY and SITE, and defines our functions for us
# TODO: Refactor to base class and inherited


# TODO: override this to make it flip a coin and then raise or lower by up to 5%
def get_new_prob(orig_prob):
            new_prob = orig_prob + .01
            if new_prob > .9:
                new_prob -= .02
            return new_prob

if __name__ == '__main__':
    with SciCastBotSession(base_url=URL, api_key=api_key) as s:
        ri = s.get_round_info()
        print_dict(ri['R5'], f'ROUND 5 INFO')

    while(True):
        with SciCastBotSession(base_url=URL, api_key=api_key) as s:

            assets = s.get_user_info()
            cash, budget = assets['cash'], assets['cash'] * .01
            print(f"___ASSETS: cash: {cash}, budget: {budget}")

            q_id = get_qid()
            orig_prob = get_latest_prob_from_qid(q_id)
            new_prob = get_first_prob_from_qid(q_id)    # TODO: wasteful - makes two calls to q history
            
            # add a trade

            print(f"Trading {orig_prob:.2f} -> {new_prob:.2f}")
            result = s.trade(q_id, orig_prob+.01, max_cost=budget, comment='[PriorBot]: nudge towards starting prob.')
            if 'trade' in result.keys():
                print_trade(result, prefix='\t')
            else:
                print(result)

            current_prob = get_latest_prob_from_qid(q_id)
            print('Post-trade prob:', current_prob)

            # Check assets
            assets = s.get_user_info()
            print_dict(assets, 'POST-TRADE ASSETS')

            

        sleep(60)
