import praw
import pyperclip


# allows the bot to log into reddit servers. Be sure to change "WorldDudeMan" to whatever your praw.ini contains as the
# header. user_agent can be anything
def bot_login():
    reddit = praw.Reddit('SubredditManager', user_agent="Subreddit Manager")
    return reddit


def paste_from_subreddit(subreddit_name, filter_word=''):
    for submission in reddit.subreddit(subreddit_name).hot(limit=15):
        if filter_word in submission.title:
            threadURL = submission.url
            threadTitle = submission.title
            file = open("subredditlinks.txt", 'a')
            pyperclip.copy(threadTitle + ' ')
            file.write(pyperclip.paste())
            pyperclip.copy(threadURL + '\n')
            file.write(pyperclip.paste())
            reddit.subreddit('TestYourBeepBoop').submit(threadTitle, url=threadURL)


# initialize bot, run the paste command for each subreddit you want to post from
def main():
    paste_from_subreddit('worldnews')
    paste_from_subreddit('programming')
    paste_from_subreddit('askreddit')
    paste_from_subreddit('technology')
    paste_from_subreddit('explainlikeimfive')
    paste_from_subreddit('cscareerquestions')
    paste_from_subreddit('learnprogramming')

reddit = bot_login()
main()
