import praw
import time
import pyperclip

#allows the bot to log into reddit servers. Be sure to change "WorldDudeMan" to whatever your praw.ini contains as the header. user_agent can be anything

def bot_login():
    reddit = praw.Reddit('WorldDudeMan', user_agent = "world news puller but I love cats")
    print ('Logged in.')
    return reddit

#copy and paste to the .txt file and to the private subreddit. limit can be changed from 15 (line 16), .txt file name can be changed (line 20), subreddit
#name must be changed to your private subreddit (line 25). If you don't want to post to a .txt file, remove lines 20-24.

def paste_from_subreddit(subreddit_name, filter_word):
    for submission in reddit.subreddit(subreddit_name).hot(limit=15):
        if (filter_word) in submission.title:
            threadURL = submission.url
            threadTitle = submission.title
            file = open("subredditlinks.txt", 'a')
            pyperclip.copy(threadTitle + ' ')
            file.write(pyperclip.paste())
            pyperclip.copy(threadURL + '\n')
            file.write(pyperclip.paste())
            reddit.subreddit('TestYourBeepBoop').submit(threadTitle, url=threadURL)
             
#initialize bot, run the paste command for each subreddit you want to post from. Note that image links will post the URL as the image hosting site, self 
#posts (i.e. AskReddit) will link to the post, and external links (i.e. news outlets) will link to the website. The bot will then sleep for 12 hours
#before posting again. Below are some examples of subreddits to access.

reddit = bot_login()
while True:
    paste_from_subreddit('worldnews', 'Trump')
    paste_from_subreddit('mechanicalkeyboards', 'board')
    paste_from_subreddit('personalfinance', 'debt')
    paste_from_subreddit('askreddit', '')
    paste_from_subreddit('aww','')
    paste_from_subreddit('explainlikeimfive', '')
    paste_from_subreddit('showerthoughts', '')
    paste_from_subreddit('learnprogramming','')
    print("Sleeping.")
    time.sleep(43200)