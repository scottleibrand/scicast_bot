import random
from scicast_bot_session.client.scicast_bot_session import SciCastBotSession
from scicast_bot_session.common.utils import scicast_bot_urls
import botutils
from time import sleep
import datetime
import sys

def getinfo(site,bot='',roundid:str='', percent=0.005):
    try:
        api_key = botutils.lookup_key(site+bot)
        URL = scicast_bot_urls[site]
        s = SciCastBotSession(base_url=URL, api_key=api_key)
        assets = s.get_user_info()
        currentCash=assets["cash"]
        budget = botutils.get_trade_cost(cash=currentCash,fraction=percent)

        print(f'Pulling from {URL}',file=sys.stderr)
        print(f'cash = {currentCash}, budget = {budget}',file=sys.stderr)
        print("claim_id,short_name,latest_prob")
        questions = s.get_questions(roundid)
        for q in questions:
            #print(q)
            print(q['question']['claim_id'],",",q['question']['short_name'],",",q['prob'][1], sep='')
    except Exception as e:
            print(f'Noise Bot Error: {e}')

    
    
