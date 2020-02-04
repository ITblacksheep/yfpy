def test_get_all_yahoo_fantasy_game_keys(yfpy_data_obj, yfpy_query_obj, config_obj):
    """Retrieve all Yahoo fantasy football game keys.
        """
    key_data = yfpy_query_obj.get_all_yahoo_fantasy_game_keys()

    query_result_data = yfpy_data_obj.save(
        config_obj["game_code"] + "-game_keys",
        yfpy_query_obj.get_all_yahoo_fantasy_game_keys,
    )

    loaded_result_data = yfpy_data_obj.load(config_obj["game_code"] + "-game_keys")

    assert query_result_data == loaded_result_data

