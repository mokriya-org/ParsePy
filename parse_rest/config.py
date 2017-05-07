from parse_rest.connection import API_ROOT
from parse_rest.datatypes import ParseResource


class Config(ParseResource):
    ENDPOINT_PATH = 'config'

    @classmethod
    def get(cls):
        return cls.GET('').get('params')

