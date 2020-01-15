from time import sleep

from scicast_bot_session.client.scicast_bot_session import SciCastBotSession
from scicast_bot_session.common.utils import scicast_bot_urls
import os

api_key = os.getenv("BOT_API_KEY")

def get_latest_prob_from_history(history) -> float:
    return float(history[-1]['probabilities'].split(',')[1])


if __name__ == '__main__':
    with SciCastBotSession(base_url=scicast_bot_urls['dev'], api_key=api_key) as s:
        ri = s.get_round_info()
        print(ri)

    while(True):
        with SciCastBotSession(base_url=scicast_bot_urls['dev'], api_key=api_key) as s:


            assets = s.get_user_info()#['cash']
            print(assets)

            recent_trades = s.get_recent_trades()
            print(recent_trades)


            question_id = 503
            history = s.get_question_history(question_id)
            orig_prob = get_latest_prob_from_history(history)

            print(orig_prob)

            # add a trade
            s.trade(question_id, orig_prob+.01)

            history = s.get_question_history(question_id)
            current_prob = get_latest_prob_from_history(history)
            print(current_prob)

            s.trade(question_id, orig_prob)

            history = s.get_question_history(question_id)
            current_prob = get_latest_prob_from_history(history)
            print(current_prob)
        sleep(0)
