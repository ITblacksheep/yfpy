import pytest
import os
import json

from yfpy import Data
from yfpy.query import YahooFantasySportsQuery


@pytest.fixture(scope='session')
def yfpy_data_obj():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_output")
    yahoo_data = Data(data_dir)
    return yahoo_data

@pytest.fixture(scope='session')
def yfpy_query_obj(config_obj):
    auth_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "auth")
    game_id = config_obj['game_id']
    game_code = config_obj['game_code']
    league_id = config_obj['league_id']
    yahoo_query = YahooFantasySportsQuery(auth_dir, league_id, game_id=game_id,
                                                   game_code=game_code, offline=False, all_output_as_json=False)
    yahoo_query.league_key = game_id + ".l." + league_id
    return yahoo_query

@pytest.fixture(scope='session')
def config_obj():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data