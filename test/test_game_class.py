import os
from yfpy.models import Games


def test_get_all_yahoo_fantasy_game_keys(yfpy_query_obj, config_obj):
    """Retrieve all Yahoo fantasy football game keys.
        """
    key_data = yfpy_query_obj.get_all_yahoo_fantasy_game_keys()

    assert len(key_data.games) >= 1


def test_save_yf_game_keys(yfpy_data_obj, config_obj, games_obj):
    yfpy_data_obj.save(config_obj["game_code"] + "-game_keys", games_obj)

    assert os.path.isfile(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "test_output",
            (config_obj["game_code"] + "-game_keys.json"),
        )
    )


def test_load_yf_game_keys(yfpy_data_obj, config_obj, games_obj):
    loaded_result_data = yfpy_data_obj.load(
        config_obj["game_code"] + "-game_keys", data_type_class=Games
    )
    assert games_obj == loaded_result_data


def test_get_game_key_by_season(yfpy_query_obj, config_obj):
    """Retrieve specific game key by season.
    """
    query_result_data = yfpy_query_obj.get_game_key_by_season(
        season=config_obj["season"]
    )
    assert query_result_data == config_obj["game_id"]


def test_get_current_game_info(yfpy_query_obj, config_obj):
    """Retrieve game info for current fantasy season.
    """
    query_result_data = yfpy_query_obj.get_current_game_info()
    query_result_data
