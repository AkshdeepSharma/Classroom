import urllib.request
import json
import time

get_pro_game = 'https://api.opendota.com/api/proMatches'


def request_pro_game():
    with urllib.request.urlopen(get_pro_game) as url:
        response = url.read()
    parsed_data = json.loads(response.decode())
    for i in range(len(parsed_data)):
        if parsed_data[i]['leagueid'] == 5401:
            match_id = parsed_data[i]['match_id']
            break
    return match_id


def request_match_info(match_id):
    with urllib.request.urlopen('https://api.opendota.com/api/matches/' + str(match_id)) as url:
        response = url.read()
    parsed_data = json.loads(response.decode())
    radiant_data = parsed_data['radiant_team']['name'], 'Barracks:', parsed_data['barracks_status_radiant'], \
                   'Kills:', parsed_data['radiant_score'], 'Towers:', parsed_data['tower_status_radiant'], \
                   'XP and Gold Advantage:', parsed_data['radiant_gold_adv'], parsed_data['radiant_xp_adv']
    dire_data = parsed_data['dire_team']['name'], 'Barracks:', parsed_data['barracks_status_dire'], 'Kills:', \
                parsed_data['dire_score'], 'Towers:', parsed_data['tower_status_dire']
    if parsed_data['radiant_win']:
        victory = "Radiant Victory"
    else:
        victory = "Dire Victory"
    return radiant_data, dire_data, victory


while True:
    game_id = request_pro_game()
    print(request_match_info(game_id))
    time.sleep(10)
