import urllib.request
import json
import config
from time import sleep


#variables
steam_id64 = '76561198018005583'
get_player_summary = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + config.steam_key + '&steamids=' + steam_id64
get_friend_list = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + config.steam_key + '&steamid=' + steam_id64 + '&relationship=friend'
get_recently_played = 'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=' + config.steam_key + '&steamid=' + steam_id64 + '&format=json'


#function to create database of steam ids
def GetSteamID():
    pass


#function to get summary info of steam user
def RequestSummaryInfo(url_name):
    with urllib.request.urlopen (url_name) as url:
        response_gps = url.read()    
    parsedDataSummary = json.loads(response_gps.decode())
    player_summary_steamid = parsedDataSummary['response']['players'][0]['steamid']
    player_summary_cvs = parsedDataSummary['response']['players'][0]['communityvisibilitystate']
    player_summary_personaName = parsedDataSummary['response']['players'][0]['personaname']
    return (player_summary_personaName, player_summary_steamid, player_summary_cvs)

'''
def RequestFriendInfo(url_name):
    with urllib.request.urlopen (url_name) as url:
        response_gfl = url.read()
    parsedFriendsList = json.loads(response_gfl.decode())
    for friend in range(len(parsedFriendsList['friendslist']['friends'])):
        print(RequestGameInfo('http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=' + config.steam_key + 
                              '&steamid=' + (parsedFriendsList['friendslist']['friends'][friend]['steamid']) + '&format=json'))
'''

#function to get game info of the user
def RequestGameInfo(url_name):    
    with urllib.request.urlopen (url_name) as url:
        response_grp = url.read()
    parsedRecentlyPlayed = json.loads(response_grp.decode())
    most_playtime_2weeks = (parsedRecentlyPlayed['response']['games'][0]['playtime_2weeks']) // 60
    most_playtime_appid = parsedRecentlyPlayed['response']['games'][0]['appid']
    most_playtime_name = parsedRecentlyPlayed['response']['games'][0]['name']
    return(most_playtime_2weeks, most_playtime_appid, most_playtime_name)


#tweet da tweet bruh
def TweetTheTweet():
    name = RequestSummaryInfo(get_player_summary)
    game = RequestGameInfo(get_recently_played)
    config.api.update_status(str(name[0]) +  "'s most popular game in the past 2 weeks is " + str(game[2]) + ' with ' + str(game[0]) + ' hours played!')


def main():
    TweetTheTweet()


while True:
    main()
    break;
    sleep(60 * 60 *12)
    
    
    
"""
-------------------
   MAJOR ISSUES:
-------------------
1. Currently,if a friend has no recent game time, app crashes.
Solutions:

2. Make PHP script to make a database and replace steam_id64 with a random item in the database.
"""