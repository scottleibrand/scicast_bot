from time import sleep

from scicast_bot_session.client.scicast_bot_session import SciCastBotSession
from scicast_bot_session.common.utils import scicast_bot_urls
import os
from random import randint

api_key = os.getenv("BOT_API_KEY")
SITE = 'sandbox'
URL = scicast_bot_urls[SITE]

def get_qid():
    '''TODO: make this smarter. Dev span is only R5'''
    if SITE=='sandbox':
        return randint(2,301)
    if SITE=='dev':
        return randint(800,1102)

    raise ValueError('Simple Bot is not rated for production site!')

def get_latest_prob_from_history(history) -> float:
    return float(history[-1]['probabilities'].split(',')[1])

def get_new_prob(orig_prob):
            new_prob = orig_prob + .01
            if new_prob > .9:
                new_prob -= .02
            return new_prob

# Just some pretty-print routines. 
def print_dict(D, name='<DICT>', KEYLEN=15):
    '''Tabular pretty-print.'''
    if name is not None:
        print(f'___{name}___:')
    for key in D:
        print(f'\t{key:{KEYLEN}}: {D[key]}')

def print_trade(trade):
    t, q, u = trade['trade'], trade['question'], trade['user']
    print(f"___TRADE by {u['user_id']} on Q. {q['id']} at {t['created_at']}___")
    print_dict(q, None)
    print_dict(t, None)
    print_dict(u, None)

def print_box(s):
    stars = '*' * (6 + len(s))
    print(f"{stars}\n** {s} **\n{stars}")


if __name__ == '__main__':
    with SciCastBotSession(base_url=URL, api_key=api_key) as s:
        ri = s.get_round_info()
        print_dict(ri['R5'], f'ROUND 5 INFO')

    while(True):
        with SciCastBotSession(base_url=URL, api_key=api_key) as s:

            assets = s.get_user_info()
            print_dict(assets, 'ASSETS')

            recent_trades = s.get_recent_trades()[-3:]
            for item in recent_trades:
                print_trade(item)

            q_id = get_qid()
            print_box(f'SELECTING Q. {q_id} for trade.')
            history = s.get_question_history(q_id)
            orig_prob = get_latest_prob_from_history(history)
            new_prob = get_new_prob(orig_prob)
            
            print(f"Trading {orig_prob:.2f} -> {new_prob:.2f}")

            # add a trade
            s.trade(q_id, orig_prob+.01, comment='[SimpleBot]: change by 1%.')

            history = s.get_question_history(q_id)
            current_prob = get_latest_prob_from_history(history)
            print(current_prob)

            # Check assets
            assets = s.get_user_info()
            print_dict(assets, 'ASSETS')

            # undo it
            print(f"Undo. Trading {new_prob:.2f} -> {orig_prob:.2f}")
            s.trade(q_id, orig_prob, comment='[SimpleBot]: put it back.')

            history = s.get_question_history(q_id)
            current_prob = get_latest_prob_from_history(history)
            print(current_prob)

            # Check Assets
            assets = s.get_user_info()
            print_dict(assets, 'ASSETS')


        sleep(60)
