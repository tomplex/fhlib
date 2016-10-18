from fhlib.config import DEFAULT_SEASON_ID, DEFAULT_LEAGUE_ID
from fhlib.lib.scoreboard import Scoreboard
from fhlib.lib.standings import Standings
from fhlib.lib.settings import Settings
from fhlib.lib.team import team_iterator

class League:
    def __init__(self, league_id=None, season=None, config=None):
        self._config = config
        self.league_id = league_id if league_id else DEFAULT_LEAGUE_ID
        self.season = season if season else DEFAULT_SEASON_ID


    @property
    def scoreboard(self):
        return Scoreboard(self.league_id, self.season)

    @property
    def standings(self):
        return Standings(self.league_id, self.season)

    @property
    def settings(self):
        return Settings(self.league_id, self.season)

    @property
    def teams(self):
        return [team for team in team_iterator(self.league_id, self.season)]

