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
1. Install the SciCastBotSession client.
```bash
pip install -r requirements.txt --upgrade```

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
		 


 

Console pretty-print: background info first, including 3 most recent trades:
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

Now the trade:
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

Charles Twardy, Ph.D. | Jacobs | Senior Data Scientist / Replication Markets PI
O:+1.703.817.4773 | charles.twardy @jacobs.com
2551 Dulles View Dr, Suite 700 | Herndon, VA 20171 | US
ctwardy@replicationmarkets.com | www.replicationmarkets.com | @replicationmkts 




On 1/15/20, 10:15 AM, "Ayesha N. Baig" <abaig@replicationmarkets.com> wrote:

Sure. I am using PyCharm professional. I thought it ran it in the background. But thanks for the pointer. 
 
From: Brandon Goldfedder <brandon@goldfedder.com>
Reply-To: "brandon@goldfedder.com" <brandon@goldfedder.com>
Date: Wednesday, January 15, 2020 at 9:39 AM
To: "Ayesha N. Baig" <abaig@replicationmarkets.com>
Cc: David Mackenzie <dmackenzie@replicationmarkets.com>, Abdul Gouda <agouda@replicationmarkets.com>, Brandon Goldfedder <bgoldfedder@replicationmarkets.com>, Charles Twardy <ctwardy@replicationmarkets.com>
Subject: Re: bot call?
 
Ayesha,
I *think* its checked in/updated. As a sanity check you might need to manually force it to update since the git+https stuff sometimes ignores things. The version should be 1.0.4.
 
Do a pip uninstall and a pip install to verify?
 
-Brandon
 
On Wed, Jan 15, 2020 at 8:54 AM Ayesha N. Baig <abaig@replicationmarkets.com> wrote:
Wow guys, thanks for chiming in last night. You seemed to be busy 😉
 
So it seems that the SciCastBotSession has not been updated? I did a pull this morning and tried to run, however, I get an error:  “AttributeError: 'SciCastBotSession' object has no attribute 'get_round_info”
 
Thoughts?
 
Very Respectfully,
Ayesha
 
From: Brandon Goldfedder <brandon@goldfedder.com>
Reply-To: "brandon@goldfedder.com" <brandon@goldfedder.com>
Date: Tuesday, January 14, 2020 at 11:56 PM
To: David Mackenzie <dmackenzie@replicationmarkets.com>
Cc: Abdul Gouda <agouda@replicationmarkets.com>, "Ayesha N. Baig" <abaig@replicationmarkets.com>, Brandon Goldfedder <bgoldfedder@replicationmarkets.com>, Charles Twardy <ctwardy@replicationmarkets.com>
Subject: Re: bot call?
 
Great. I think the only open issues that I am aware of is that the json returned from the calls that we might want to simplify (nothing not available in web but still may be more then we like)
 
On Tue, Jan 14, 2020 at 11:52 PM David Mackenzie <dmackenzie@replicationmarkets.com> wrote:
oh cool.  In that case I think you make a good point to have roundid in there to view historical questions.  If you can view past, present, and future questions from the web interface, then bots being able to do the same and learn from history, and also prepare for the next round, would be a good capability.
 
Thanks for answering the questions and helping me understand it.
 
 
From: Brandon Goldfedder <brandon@goldfedder.com>
Sent: Tuesday, January 14, 2020 10:49 PM

To: David Mackenzie <dmackenzie@replicationmarkets.com>
Cc: Abdul Gouda <agouda@replicationmarkets.com>; Ayesha N. Baig <abaig@replicationmarkets.com>; Brandon Goldfedder <bgoldfedder@replicationmarkets.com>; Charles Twardy <ctwardy@replicationmarkets.com>
Subject: Re: bot call? 
 
Yes, they currently can see pending questions once loaded into the market in he web interface
 
On Tue, Jan 14, 2020 at 11:40 PM David Mackenzie <dmackenzie@replicationmarkets.com> wrote:
can they also see future questions?
lets say we preload the questions 24 hours before the round and they put in the next sequential round id.  
 
From: Brandon Goldfedder <brandon@goldfedder.com>
Sent: Tuesday, January 14, 2020 10:37 PM
To: David Mackenzie <dmackenzie@replicationmarkets.com>
Cc: Abdul Gouda <agouda@replicationmarkets.com>; Ayesha N. Baig <abaig@replicationmarkets.com>; Brandon Goldfedder <bgoldfedder@replicationmarkets.com>; Charles Twardy <ctwardy@replicationmarkets.com>
Subject: Re: bot call? 
 
I think they should be able to see all questions (non current as well) since they can from the market by setting the paused filter. They might want to use these for trends?
 
On Tue, Jan 14, 2020 at 10:19 PM David Mackenzie <dmackenzie@replicationmarkets.com> wrote:
if not supplied, will it return questions for all rounds?  do we want outside users to be able to get non current questions?
 
From: Brandon Goldfedder <brandon@goldfedder.com>
Sent: Tuesday, January 14, 2020 9:17 PM

To: David Mackenzie <dmackenzie@replicationmarkets.com>
Cc: Ayesha N. Baig <abaig@replicationmarkets.com>; Charles Twardy <ctwardy@replicationmarkets.com>; Brandon Goldfedder <bgoldfedder@replicationmarkets.com>; Abdul Gouda <agouda@replicationmarkets.com>
Subject: Re: bot call? 
 
Right, and there it's only as an optimization filter to limit the results that return. 
 
-Brandon
 
On Tue, Jan 14, 2020 at 10:12 PM David Mackenzie <dmackenzie@replicationmarkets.com> wrote:
I was looking at the get_questions, but youre right, it isnt present on any other calls.
 
 
 
 
From: Brandon Goldfedder <brandon@goldfedder.com>
Sent: Tuesday, January 14, 2020 8:36 PM
To: David Mackenzie <dmackenzie@replicationmarkets.com>
Cc: Ayesha N. Baig <abaig@replicationmarkets.com>; Charles Twardy <ctwardy@replicationmarkets.com>; Brandon Goldfedder <bgoldfedder@replicationmarkets.com>; Abdul Gouda <agouda@replicationmarkets.com>
Subject: Re: bot call? 
 
we don't use the round_id for any actions. You can query the questions by the round_id for optimization but otherwise there really isn't anything round_id related that uses the current round or similar concepts. 
-Brandon
 
On Tue, Jan 14, 2020 at 9:24 PM David Mackenzie <dmackenzie@replicationmarkets.com> wrote:
awesome..  Thanks
I was thinking something that allowed the user to query what the current round was.  (no round id needed for input).
 
On that, an idea, should any of the calls actually have round id?  For bots it will ALWAYS be the current round. 
 
 
 
From: Brandon Goldfedder <brandon@goldfedder.com>
Sent: Tuesday, January 14, 2020 7:45 PM
To: Ayesha N. Baig <abaig@replicationmarkets.com>
Cc: Charles Twardy <ctwardy@replicationmarkets.com>; David Mackenzie <dmackenzie@replicationmarkets.com>; Brandon Goldfedder <bgoldfedder@replicationmarkets.com>; Abdul Gouda <agouda@replicationmarkets.com>
Subject: Re: bot call? 
 
swagger finally complied: 
 
 
 
On Tue, Jan 14, 2020 at 8:30 PM Brandon Goldfedder <brandon@goldfedder.com> wrote:
The scicast_bot_session object has the method btw so no need to directly hit the swagger ui (actually I think the session has ~100% wrapping of the webservice calls - but my swagger docs are likely better ;-) ) 
 
-Brandon
 
On Tue, Jan 14, 2020 at 8:28 PM Brandon Goldfedder <brandon@goldfedder.com> wrote:
Swagger docs and I are fighting over spacing... should be fixed up shortly 
 
 
 
On Tue, Jan 14, 2020 at 8:23 PM Ayesha N. Baig <abaig@replicationmarkets.com> wrote:
Thanks Brandon. We are using the sci_bot_session and writing it in python. Will it take some time to populate on Swagger?(/round_info call) Don’t seem to see it as of yet. (I can work on it some more tomorrow).
 
Thanks for chiming in 😊
 
Very Respectfully,
Ayesha
 
From: Brandon Goldfedder <brandon@goldfedder.com>
Reply-To: "brandon@goldfedder.com" <brandon@goldfedder.com>
Date: Tuesday, January 14, 2020 at 8:15 PM
To: "Ayesha N. Baig" <abaig@replicationmarkets.com>
Cc: Charles Twardy <ctwardy@replicationmarkets.com>, David Mackenzie <dmackenzie@replicationmarkets.com>, Brandon Goldfedder <bgoldfedder@replicationmarkets.com>, Abdul Gouda <agouda@replicationmarkets.com>
Subject: Re: bot call?
 
Good timing. I just added the new bot server as well as the simple_bot client (which is why you might be noticing it going up/down right now). 
 
Round info are now accessible from the /round_info call. I do not have a concept of 'current' round but we could find all rounds that might be valid by a date pretty easily
 
 
 
If writing in python use the scicast_bot_session class, if using anything else the swagger api should suffice.
 
Sample bot:
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
 
On Tue, Jan 14, 2020 at 8:03 PM Ayesha N. Baig <abaig@replicationmarkets.com> wrote:
Was trying to add some functionality to “simple bot” and one of the “requirements” was the ability to get “round id”. I checked swagger to validate. There is not currently an API call listed as “round_id”. Thoughts?
 
https://dev.replicationmarkets.com/bot/api_docs
 
Very Respectfully,
Ayesha
 
From: Charles Twardy <ctwardy@replicationmarkets.com>
Date: Tuesday, January 14, 2020 at 10:31 AM
To: David Mackenzie <dmackenzie@replicationmarkets.com>
Cc: "Ayesha N. Baig" <abaig@replicationmarkets.com>
Subject: Re: bot call?
 
Hm, we have a FastAI at 11 central.  I’ll talk to Ayesha this morning and Dave after FastAI.  
 
Charles Twardy, Ph.D. | Jacobs | Senior Data Scientist / Replication Markets PI
O:+1.703.817.4773 | charles.twardy @jacobs.com
2551 Dulles View Dr, Suite 700 | Herndon, VA 20171 | US
ctwardy@replicationmarkets.com | www.replicationmarkets.com | @replicationmkts 


 
 
On 1/14/20, 10:22 AM, "David Mackenzie" <dmackenzie@replicationmarkets.com> wrote:
 
Good morning
Morning
I have a call at 930 (central), 10(central), and a 1030.  Talk after?
 
 
 
From: Charles Twardy <ctwardy@replicationmarkets.com>
Sent: Tuesday, January 14, 2020 8:53 AM
To: David Mackenzie <dmackenzie@replicationmarkets.com>
Cc: Ayesha N. Baig <abaig@replicationmarkets.com>
Subject: bot call? 
 
Dave,
 
Are you free this morning for a call about bots?  Say 9:30 or 10 your time?
 
-C
 
Charles Twardy, Ph.D. | Jacobs | Senior Data Scientist / Replication Markets PI
O:+1.703.817.4773 | charles.twardy @jacobs.com
2551 Dulles View Dr, Suite 700 | Herndon, VA 20171 | US
ctwardy@replicationmarkets.com | www.replicationmarkets.com | @replicationmkts 


 
