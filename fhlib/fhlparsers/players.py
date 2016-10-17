from bs4 import BeautifulSoup
from fhlib.config import DEFAULT_HTML_PARSER


class PlayerParser:

    def __init__(self, html):
        self.parsed = BeautifulSoup(html, DEFAULT_HTML_PARSER)
