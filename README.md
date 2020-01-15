# simple_bot for SciCast / ReplicationMarkets

simple_bot is a very simple SciCast bot. It uses the new simplified bot API
developed in January 2020 for Replication Markets. (See for example, 
[the Swagger docs](https://sandbox.replicationmarkets.com/bot/api_docs#!/Get_Round_Info/get_round_info).)

This API is built around the "change the probability" view of the market.
It assumes you have a model of what the probability should be. 

simple_bot has no real model. It simply makes a 1% change in a random claim, 
and then reverses it, every minute.

## Features:
* Demonstrates how to connect to a SciCastBotSession.
* Defaults to using the 'sandbox' site. 
* Shows how to get your available assets.
* Shows how to get recent trades.
* Shows how to get a particular claim's history.
* Shows how to extract the latest probability from that history.
* Shows how to make a trade with comment.
* Pretty-prints the returned data structures.

## Usage
1. Install the SciCastBotSession client: `pip install -r requirements.txt --upgrade`

2. Get a sandbox account.
  * Visit http://sandbox.replicationmarkets.com
  * Create an account.

3. Get an API key
  * Email your market helpdesk to ask them to give you one.
  * View your profile page to see what it is. (Not your public profile!)

4. Make your API key available to the simple_bot.
  * It assumes you've exported an environment variable BOT_API_KEY. 
    * Unix example: `export BOT_API_KEY=xxxxxxxxxxxx`   (Use a real API key!)
    * Or, set this in your IDE under Runtime settings.
  * Alternatively, put this in a file and replace the `os.getenv` call with
  a file read.
  * As a last resort, just hardcode it.  
    * **But not if you share your code or post to git!**

5. Run the script, e.g. `python simple_bot.py`


Of course, the point is for you to _modify_ simple_bot to do useful things.

Please take care to rate limit your actions.

It’s running in the background on my machine, trading once a minute.
		 

## Example Output
### Background info including 3 most recent trades
```
___ASSETS___:
        cash           : 299.9999064211614
___TRADE by 2 on Q. 62 at 2020-01-15T16:53:32+00:00___
        id             : 62
        name           : (Wright-2016-JConflictRes) Unpacking Territorial Disputes
        created_at     : 2020-01-15T16:53:32+00:00
        new_value      : 0.39999995
        old_value_list : ['0.59', '0.41000003']
        new_value_list : ['0.59999996', '0.39999995']
        dimension      : 1
        change         : -0.010000080000000022
        dimension_text : 
        user_id        : 2
        username       : sandbox_crt
___TRADE by 2 on Q. 62 at 2020-01-15T16:53:28+00:00___
        id             : 62
        name           : (Wright-2016-JConflictRes) Unpacking Territorial Disputes
        created_at     : 2020-01-15T16:53:28+00:00
        new_value      : 0.41000003
        old_value_list : ['0.6', '0.4']
        new_value_list : ['0.59', '0.41000003']
        dimension      : 1
        change         : 0.010000029999999993
        dimension_text : 
        user_id        : 2
        username       : sandbox_crt
___TRADE by 2 on Q. 32 at 2020-01-15T16:52:22+00:00___
        id             : 32
        name           : (Gray-2017-CompPolitStu) Leadership Turnover and the Durability of International Trade Commitments
        created_at     : 2020-01-15T16:52:22+00:00
        new_value      : 0.30000004
        old_value_list : ['0.68999994', '0.31']
        new_value_list : ['0.7', '0.30000004']
        dimension      : 1
        change         : -0.009999959999999974
        dimension_text : 
        user_id        : 2
        username       : sandbox_crt
```
### Now the trade:
```
*******************************
** SELECTING Q. 2 for trade. **
*******************************
Trading 0.80 -> 0.81
0.81
___ASSETS___:
        cash           : 292.59984827678375
Undo. Trading 0.81 -> 0.80
0.79999995
___ASSETS___:
        cash           : 299.9999064211614
```
