"""botutils.py. 
Utility functions for claim selection, history, trading...etc"""
import logging
import random
import lmsrutils as lmsr
import os
import numpy as np  
#Lookup key 
def lookup_key(kind=''):
    home = os.path.expanduser('~')
    '''Read key info from key file.'''
    try:
        with open(f'{home}/{kind}_key.txt') as f:
            return(f.read().strip())
    except FileNotFoundError:
        with open(f'{home}/.{kind}_key.txt') as f:
            return(f.read().strip())
    except Exception as e:
        print(f'Error getting key: {e}')


#question id
def get_qid(s,roundId,flag=None):
    try:
        qIds = [x['question']['id'] for x in s.get_questions(roundId) if \
                x['question']['is_tradeable']]
        if flag:
            return qIds
        return random.choice(qIds)
    except Exception as e:
        print(f'Error getting question id: {e}')
        return -1 

def get_first_prob(s,history: list = None, qid: int = None) -> float:
    """Return first P(Yes). If given history, use it, else fetch history first.
    """
    if history is None:
        history = s.get_question_history(qid)
    return float(history[0]['probabilities'].split(',')[1])


def get_latest_prob(s, history: list = None, qid: int = None) -> float:
        """Return P(Yes). If given history, return last P(Yes), 
        else fetch history then do that."""
        if history is None:
            history = s.get_question_history(qid)
        return float(history[-1]['probabilities'].split(',')[1])

def get_deltas(s,qids):
    deltas = {}
    for qid in qids:
        try:
            q_history = s.get_question_history(qid)
            prior = float(q_history[0]['probabilities'].split(',')[1])
            curr =  float(q_history[-1]['probabilities'].split(',')[1])
#            history[qid] = q_history
            deltas[qid] = (abs(curr - prior),curr - prior,curr,prior)     
        except Exception as e:
            print(f'Error getting deltas for question id: {qid}. Error {e}')
            continue 
    deltas = sorted(deltas.items(), key=lambda kv: kv[1][0],reverse=True)    
    return deltas   


       
def print_box(s):
    stars = '*' * (6 + len(s))
    print(f"{stars}\n** {s} **\n{stars}")
    

def get_trade_cost(cash:int=0, fraction:float=0,
                   trade_min=1.0):
        """How much can we spend on this trade? Our {fraction} 
        of *current* assets."""
        try:
            trade_cost = cash * fraction
        except KeyError:
            logging.warning("Call failed. Bad API Key?")
            raise KeyError
        if trade_cost < trade_min:
            trade_cost = 0.0
        logging.debug(f"\tCash = ${cash:.2f}, Trade_cost=${trade_cost:.2f}")
        return trade_cost
    

def capped_trade(s,qid: int, new_prob: float, 
                 old_prob: float, max_cost: float, comment:str='',
                 epsilon=0.001):
        """Trade P(Yes) from oldValue *towards* newValue, 
        spending no more than max_cost."""
        
        P = [1 - old_prob, old_prob]
        q_min, q_max = lmsr.trade_limits(P, max_cost, 1)
        params = {'question_id': qid, 'comment': comment,
                  'old_value': str(P), 'max_cost': max_cost}
        if q_min < new_prob < q_max:
            params['new_value'] = new_prob
        elif new_prob > old_prob:
            params['new_value'] = q_max - epsilon
        else:
            params['new_value'] = q_min + epsilon
        return s.trade(**params)
    
def clip(oldP, newP, limit=.02):
    delta = newP-oldP
    if abs(delta) > limit:
        newP = oldP + limit * np.sign(delta)
    return newP
def get_ques_trade_counts(s,qids):
    trades = [(qid, len(s.get_question_history(qid))) for qid in qids]
    return sorted(dict(trades).items(), key=lambda kv: kv[1],reverse=True)