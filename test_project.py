import pytest
import pandas as pd
import project

def test_player_lookup(monkeypatch):

    inputs = iter(["Aaron","Judge"])

    def fake_input(prompt):
        return next(inputs)

    monkeypatch.setattr("builtins.input", fake_input)

    result = project.player_lookup()

    assert result == "aaron judge"


def test_batting_calculation():

    project.player_names.clear()
    project.player_stat_dict.clear()
    project.league_stat_dict.clear()

    project.player_names.append("aaron judge")

    bat_stats = pd.DataFrame([{
        "Name": "Aaron Judge",
        "OPS": 0.520,
        "OBP": 0.280,
        "SLG": 0.240,
        "BA": 0.125,
        "SB": 0,
        "OPS_percentile": 30,
        "OBP_percentile": 25,
        "SLG_percentile": 20,
        "BA_percentile": 15,
        "SB_percentile": 5
    }])

    project.league_stat_dict["league batting"] = bat_stats

    project.batting_calculation()

    batting = project.player_stat_dict["aaron judge"]["batting"]

    assert batting["OPS"] == 0.520
    assert batting["OBP"] == 0.280
    assert batting["Overall Batting Rating"] == "22/100"

def test_pitching_calculation():

    project.player_names.clear()
    project.player_stat_dict.clear()
    project.league_stat_dict.clear()

    project.player_names.append("pedro martinez")

    pitch_stats = pd.DataFrame([{
        "Name": "Pedro Martinez",
        "ERA": 1.80,
        "WHIP": 1.00,
        "SO/9": 13.0,
        "SO/W": 7.0,
        "BAbip": 0.150,
        "GB/FB": 0.45,
        "IP": 190,
        "ERA_percentile": 95,
        "WHIP_percentile": 90,
        "SO/9_percentile": 95,
        "SO/W_percentile": 95,
        "BAbip_percentile": 80,
        "GBFB_percentile": 85,
        "IP_percentile": 90
    }])

    project.league_stat_dict["league pitching"] = pitch_stats

    project.pitching_calculation()

    pitching = project.player_stat_dict["pedro martinez"]["pitching"]

    assert pitching["ERA"] == 1.80
    assert pitching["WHIP"] == 1.00
    assert pitching["Overall Pitching Rating"] == "91/100"
