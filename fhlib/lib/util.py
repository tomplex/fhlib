import requests

from fhlib.config import API_ENDPOINTS


def make_json_request(url, params):
    return requests.get(url, params=params).json()


def get_scoreboard_data(league_id, season_id):
    url = API_ENDPOINTS['scoreboard']
    return make_json_request(url, params={
                                'leagueId' : league_id,
                                'seasonId' : season_id
                            })


def get_standings_data(league_id, season_id):
    url = API_ENDPOINTS['standings']
    return make_json_request(url, params={
                                'leagueId' : league_id,
                                'seasonId' : season_id
                            })


def get_settings_data(league_id, season_id):
    url = API_ENDPOINTS['league_settings']
    return make_json_request(url, params={
                                'leagueId' : league_id,
                                'seasonId' : season_id
                            })


def get_teams_data(league_id, season_id):
    url = API_ENDPOINTS['teams']
    return make_json_request(url, params={
                                'leagueId' : league_id,
                                'seasonId' : season_id
                            })