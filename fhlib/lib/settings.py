from fhlib.lib.util import get_settings_data

class Settings:

    def __init__(self, league_id, season):
        self.raw_json = get_settings_data(league_id, season)