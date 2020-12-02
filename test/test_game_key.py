import os

from yfpy import Data
from yfpy.query import YahooFantasySportsQuery
from dotenv import load_dotenv
from yfpy.models import Games

env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
load_dotenv(dotenv_path=env_path)

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_output")
yahoo_data = Data(data_dir)
auth_dir = "."
game_code = "nfl"
league_id = "655434"
game_key = "399"
browser_callback = False
season = 2020

yahoo_query = YahooFantasySportsQuery(
    auth_dir,
    league_id,
    game_id=game_key,
    game_code=game_code,
    offline=False,
    all_output_as_json=False,
    consumer_key=os.environ["YFPY_CONSUMER_KEY"],
    consumer_secret=os.environ["YFPY_CONSUMER_SECRET"],
    browser_callback=browser_callback
)

def test_get_all_yahoo_fantasy_game_keys():

    
    """Retrieve all Yahoo fantasy football game keys.
    """
    query_result_data = yahoo_data.save(game_code + "-game_keys-current",
                                        yahoo_query.get_all_yahoo_fantasy_game_keys)

    loaded_result_data = yahoo_data.load(game_code + "-game_keys-current")

    assert query_result_data == loaded_result_data

def test_get_all_yahoo_fantasy_game_keys_pydantic():

    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_output")
    yahoo_data = Data(data_dir)
    auth_dir = "."
    game_code = "nfl"
    league_id = "655434"
    game_key = "399"
    browser_callback = False

    yahoo_query = YahooFantasySportsQuery(
        auth_dir,
        league_id,
        game_id=game_key,
        game_code=game_code,
        offline=False,
        all_output_as_json=False,
        consumer_key=os.environ["YFPY_CONSUMER_KEY"],
        consumer_secret=os.environ["YFPY_CONSUMER_SECRET"],
        browser_callback=browser_callback
    )

    """Retrieve all Yahoo fantasy football game keys.
    """

    query_result_data = yahoo_data.save2(game_code + "-game_keys-new",
                                        yahoo_query.get_all_yahoo_fantasy_game_keys2)

    loaded_result_data = yahoo_data.load2(game_code + "-game_keys-new",Games)

    assert query_result_data == loaded_result_data

def test_get_game_key_by_season():
    """Retrieve specific game key by season.
    """
    query_result_data = yahoo_query.get_game_key_by_season(season=season)
    assert query_result_data == game_key

def test_get_game_key_by_season2():
    """Retrieve specific game key by season.
    """
    query_result_data = yahoo_query.get_game_key_by_season2(season=season)
    assert query_result_data == game_key