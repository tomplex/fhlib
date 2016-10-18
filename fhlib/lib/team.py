from fhlib.lib.util import get_teams_data

def team_iterator(league_id, season):
    data = get_teams_data(league_id, season)
    for team in data['teams']:
        yield Team(team)


class Team:
    def __init__(self, json):
        self.raw_json = json

