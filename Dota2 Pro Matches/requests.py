import config
import dota2api
import json
import urllib.request
import time

#api = dota2api.Initialise(config.steam_key)
call = 'https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v0001/?key=' + config.steam_key


def request_pro_game():
    with urllib.request.urlopen(call) as url:
        response = url.read()
    parsed_data = json.loads(response.decode())
    print(parsed_data['result'])
    return parsed_data


def main():
    request_pro_game()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(10)
