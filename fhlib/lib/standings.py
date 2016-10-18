from fhlib.lib.util import get_standings_data

class Standings:

    def __init__(self, league_id, season):
        self.raw_json = get_standings_data(league_id, season)