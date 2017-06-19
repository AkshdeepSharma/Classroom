import tweepy

#steam stuff
steam_key = '5D2799C66902D2A91E7E123B319DA43D'


#twitter stuff
t_consumer_key = 'F1W19DWPYl11QAQwkI7QK66WF'
t_consumer_secret = 'QbooWV2aCscS60KCBuy5HklMjo2SBTSeS4gZ7MLPqoYaJtNANf'
t_access_token = '813666730249777152-YG8krn8lmCpWhDxHHOPNrj1gcmVyYEp'
t_token_secret = 'SRCWVCGo8SJWUZO87rh57x3LIbzgKLFmHzMBmNnWR86bj'

auth = tweepy.OAuthHandler(t_consumer_key, t_consumer_secret)
auth.set_access_token(t_access_token, t_token_secret)
auth.secure = True
api = tweepy.API(auth)