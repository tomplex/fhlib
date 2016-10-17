from fhlparsers import PlayerParser, ScoreboardParser, TeamParser, StandingsParser
from config import DEFAULT_SEASON

class League:
    def __init__(self, league_id, season=DEFAULT_SEASON):
        self.league_id = league_id
        self.free_agents = PlayerParser(league_id)
        self.scoreboard = ScoreboardParser(league_id)
        self.teams = TeamParser(league_id)
        self.standings = StandingsParser(league_id)

