from datetime import date

try:
    import lxml
    del lxml
    DEFAULT_HTML_PARSER = 'lxml'
except ImportError:
    DEFAULT_HTML_PARSER = 'html.parser'


def get_current_season():
    today = date.today()
    return str(today.year + 1 if today.month >= 10 else today.year)


class LeagueConfiguration:

    @property
    def league_id(self):
        return

    @property
    def season_id(self):
        return get_current_season()

    @league_id.setter
    def league_id(self, value):
        self.league_id = value

    @season_id.setter
    def season_id(self, value):
        if value:
            self.season_id = value

    @property
    def api_params(self):
        return {
            'leagueId': int(self.league_id),
            'seasonId': int(self.season_id)
        }


class FHLibGlobalConfiguration:
    @property
    def default_html_parser(self):
        try:
            import lxml
            del lxml
            return 'lxml'
        except ImportError:
            return'html.parser'


PAGE_TYPES = {
    'players'       : 'freeagency',
    'scoreboard'    : 'scoreboard',
    'standings'     : 'standings',
    'teams'         : 'clubhouse'
}


DEFAULT_SEASON_ID = get_current_season()
DEFAULT_LEAGUE_ID = '44089'

WAIVER_REPORT = 'http://games.espn.com/fhl/waiverreport?leagueId={LEAGUE_ID}'
RECENT_ACTIVITY = 'http://games.espn.com/fhl/recentactivity?leagueId={LEAGUE_ID}'
ROSTER = "http://games.espn.com/fhl/clubhouse?leagueId=20834&seasonId=2017&teamId=1"
BASE_URL = 'http://games.espn.com/fhl/{PAGE_TYPE}?leagueId={LEAGUE_ID}&seasonId={SEASON_ID}'



API_BASE = 'http://games.espn.com/fhl/api/v2/'
API_SCOREBOARD = API_BASE + "scoreboard"
API_STANDINGS = API_BASE + "standings"
API_LEAGUE_SETTINGS = API_BASE + "leagueSettings"
API_TEAMS = API_BASE + "teams"

API_ENDPOINTS = {
    'scoreboard'        : API_SCOREBOARD,
    'standings'         : API_STANDINGS,
    'league_settings'   : API_LEAGUE_SETTINGS,
    'teams'             : API_TEAMS
}

fhlib_config = FHLibGlobalConfiguration()
