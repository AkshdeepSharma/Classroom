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
            match_id = parsed_data[0]['match_id']
            break
    return match_id


def request_match_info(match_id):
    with urllib.request.urlopen('https://api.opendota.com/api/matches/' + str(match_id)) as url:
        response = url.read()
    parsed_data = json.loads(response.decode())
    return parsed_data['radiant_team'][0]


while True:
    game_id = request_pro_game()
    print(request_match_info(game_id))
    time.sleep(10)


'''
    for i in range(len(parsed_data)):
        if parsed_data[i]['leagueid'] == 5401:
            teams.append('Radiant: ' + parsed_data[i]['radiant_name'])
            teams.append('Dire: ' + parsed_data[i]['dire_name'])
            if parsed_data[i]['radiant_win']:
                teams.append(parsed_data[i]['radiant_name'] + ' Victory')
            elif not parsed_data[i]['radiant_win']:
                teams.append(parsed_data[i]['dire_name'] + ' Victory')'''