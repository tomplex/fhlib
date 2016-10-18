from fhlib.lib.util import get_scoreboard_data

class Scoreboard:

    def __init__(self, league_id, season):
        self.raw_json = get_scoreboard_data(league_id, season)