import argparse
from scicast_bot_session.common.utils import scicast_bot_urls
import PriorBot as pb
import NoiseBot as nb

if __name__ == "__main__":
    sites = list(scicast_bot_urls.keys())
    bots = ['noise','prior']
    parser = argparse.ArgumentParser(description="Parser for Trading Bots")
    
    parser.add_argument('--bot',choices=bots,type=str,help=f'Which Bot to run?')
    parser.add_argument('--site',choices=sites,type=str,
                        help=f'Site for trading. Options: {sites}')
    parser.add_argument('--round',type=str,help=f'Round to trade for?')
    
    args = parser.parse_args()
    site = args.site
    rnd = args.round
    bot = args.bot
    
    if site != 'predict':
        if bot == 'prior':
            pb.trade(site=site,roundid=rnd)
        elif bot =='noise':
            nb.trade(site=site,roundid=rnd)
    elif site == 'predict':
        if bot == 'prior':
            pb.trade(site=site,bot=bot,roundid=rnd)
        elif bot =='noise':
            nb.trade(site=site,bot=bot,roundid=rnd)
