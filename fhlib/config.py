
try:
    import lxml
    del lxml
    DEFAULT_HTML_PARSER = 'lxml'
except ImportError:
    DEFAULT_HTML_PARSER = 'html.parser'


# class Configuration:

DEFAULT_SETTINGS = {
    'season'        : '2017',
    'league_id'     : '44089',
}

PAGE_TYPES = {
    'players'       : 'freeagency',
    'scoreboard'    : 'scoreboard',
    'standings'     : 'standings',
    'teams'         : 'clubhouse'
}

DEFAULT_SEASON = '2017'
DEFAULT_LEAGUE_ID = '44089'

WAIVER_REPORT = 'http://games.espn.com/fhl/waiverreport?leagueId={LEAGUE_ID'
RECENT_ACTIVITY = 'http://games.espn.com/fhl/recentactivity?leagueId={LEAGUE_ID}'

BASE_URL = 'http://games.espn.com/fhl/{PAGE_TYPE}?leagueId={LEAGUE_ID}&seasonId={SEASON_ID}'
