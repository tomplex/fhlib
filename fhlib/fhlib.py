from fhlib.fhlparsers import PlayerParser, ScoreboardParser, TeamParser, StandingsParser
from fhlib.config import DEFAULT_SEASON


class League:
    def __init__(self, league_id, season=DEFAULT_SEASON):
        self.league_id = league_id

    def __load_freeagents(self):
        self.free_agents = PlayerParser()

    def __load_scoreboard(self):
        self.scoreboard = ScoreboardParser()

    def __load_teams(self):
        self.teams = TeamParser()

    def __load_standings(self):
        self.standings = StandingsParser()

