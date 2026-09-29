from pybaseball import batting_stats_range
from pybaseball import pitching_stats_range
from tabulate import tabulate
import sys

player_names = []
player_stat_dict = {}
league_stat_dict = {}

def main():

    while True:

        player_name = player_lookup()
        player_names.append(player_name)
        print(f"Players Selected: {player_names}")
        add_player = input("Add another player? (Y/N): ").upper()

        if add_player == "Y":

            continue

        elif add_player == "N":

            break

        else:

            print("Invalid input")

            continue

    league_stat_lookup()
    batting_calculation()
    pitching_calculation()
    display_table()

def player_lookup():
    print("Diamond Analytics: Baseball Stat Comparer & Ratings Calculator")
    first_name = input("Player First Name: ").strip().lower()
    last_name = input ("Player Last Name: ").strip().lower()

    player_name = f"{first_name} {last_name}"

    return player_name

def league_stat_lookup():

    while True:

        try:
            start_date = input("Start date?: ").strip()
            end_date = input("End date?: ").strip()
            league_batting = batting_stats_range(start_date,end_date)
            league_pitching = pitching_stats_range(start_date,end_date)

            break

        except ValueError:
            print("Incorrect Date Format, should be YYYY-MM-DD")

            continue

    league_batting["OPS_percentile"] = league_batting["OPS"].rank(pct=True) * 100
    league_batting["OBP_percentile"] = league_batting["OBP"].rank(pct=True) * 100
    league_batting["SLG_percentile"] = league_batting["SLG"].rank(pct=True) * 100
    league_batting["BA_percentile"] = league_batting["BA"].rank(pct=True) * 100
    league_batting["SB_percentile"] = league_batting["SB"].rank(pct=True) * 100

    league_pitching["ERA_percentile"] = league_pitching["ERA"].rank(pct=True, ascending=False) * 100
    league_pitching["WHIP_percentile"] = league_pitching["WHIP"].rank(pct=True, ascending=False) * 100
    league_pitching["SO/9_percentile"] = league_pitching["SO9"].rank(pct=True) * 100
    league_pitching["SO/W_percentile"] = league_pitching["SO/W"].rank(pct=True) * 100
    league_pitching["BAbip_percentile"] = league_pitching["BAbip"].rank(pct=True, ascending=False) * 100
    league_pitching["GBFB_percentile"] = league_pitching["GB/FB"].rank(pct=True) * 100
    league_pitching["IP_percentile"] = league_pitching["IP"].rank(pct=True) * 100

    league_stat_dict.update({"league batting": league_batting,
                            "league pitching": league_pitching})


def batting_calculation():


    for player_name in player_names:

        player_stat_dict.setdefault(player_name,{})
        df = league_stat_dict["league batting"]
        player_batting_data = df[df["Name"].str.lower() == player_name]

        if player_batting_data.empty:

            batting_rating = 0
            player_stat_dict[player_name]["batting"] = {
                "OPS": 0,
                "OBP": 0,
                "SLG": 0,
                "BA": 0,
                "SB": 0,
                "OPS Percentile": 0,
                "OBP Percentile": 0,
                "SLG Percentile": 0,
                "BA Percentile": 0,
                "SB Percentile": 0,
                "Overall Batting Rating": f"{batting_rating}/100"
            }

        else:

            ops = float(player_batting_data["OPS"].iloc[0])
            obp = float(player_batting_data["OBP"].iloc[0])
            slg = float(player_batting_data["SLG"].iloc[0])
            ba = float(player_batting_data["BA"].iloc[0])
            sb = int(player_batting_data["SB"].iloc[0])

            ops_percentile = float(player_batting_data["OPS_percentile"].iloc[0])
            obp_percentile = float(player_batting_data["OBP_percentile"].iloc[0])
            slg_percentile = float(player_batting_data["SLG_percentile"].iloc[0])
            ba_percentile = float(player_batting_data["BA_percentile"].iloc[0])
            sb_percentile = float(player_batting_data["SB_percentile"].iloc[0])

            batting_rating = int(((ops_percentile * .35) +
                                  (obp_percentile * .25) +
                                  (slg_percentile * .20) +
                                  (ba_percentile * .10) +
                                  (sb_percentile * .10)))

            player_stat_dict[player_name]["batting"] = {
                "OPS": ops,
                "OBP": obp,
                "SLG": slg,
                "BA": ba,
                "SB": sb,
                "OPS Percentile": ops_percentile,
                "OBP Percentile": obp_percentile,
                "SLG Percentile": slg_percentile,
                "BA Percentile": ba_percentile,
                "SB Percentile": sb_percentile,
                "Overall Batting Rating": f"{batting_rating}/100"
            }

def pitching_calculation():

    for player_name in player_names:

            player_stat_dict.setdefault(player_name,{})
            df = league_stat_dict["league pitching"]
            player_pitching_data = df[df["Name"].str.lower() == player_name]

            if player_pitching_data.empty:

                pitching_rating = 0
                player_stat_dict[player_name]["pitching"] = {
                    "ERA": 0,
                    "WHIP": 0,
                    "SO/9": 0,
                    "SO/W": 0,
                    "BAbip": 0,
                    "GB/FB": 0,
                    "IP": 0,
                    "ERA Percentile": 0,
                    "WHIP Percentile": 0,
                    "SO/9 Percentile": 0,
                    "SO/W Percentile": 0,
                    "BAbip Percentile": 0,
                    "GB/FB Percentile": 0,
                    "IP Percentile": 0,
                    "Overall Pitching Rating": f"{pitching_rating}/100"
                }

            else:

                era = float(player_pitching_data["ERA"].iloc[0])
                whip = float(player_pitching_data["WHIP"].iloc[0])
                so9 = float(player_pitching_data["SO9"].iloc[0])
                sow = float(player_pitching_data["SO/W"].iloc[0])
                babip = float(player_pitching_data["BAbip"].iloc[0])
                gbfb = float(player_pitching_data["GB/FB"].iloc[0])
                ip = float(player_pitching_data["IP"].iloc[0])

                era_percentile = float(player_pitching_data["ERA_percentile"].iloc[0])
                whip_percentile = float(player_pitching_data["WHIP_percentile"].iloc[0])
                so9_percentile = float(player_pitching_data["SO/9_percentile"].iloc[0])
                sow_percentile = float(player_pitching_data["SO/W_percentile"].iloc[0])
                babip_percentile = float(player_pitching_data["BAbip_percentile"].iloc[0])
                gbfb_percentile = float(player_pitching_data["GBFB_percentile"].iloc[0])
                ip_percentile = float(player_pitching_data["IP_percentile"].iloc[0])

                pitching_rating = int(((era_percentile * .25) +
                                       (whip_percentile * .20) +
                                       (so9_percentile * .15) +
                                       (sow_percentile * .15) +
                                       (babip_percentile * .10) +
                                       (gbfb_percentile * .10) +
                                       (ip_percentile * .05)))

                pitching_rating  = round(pitching_rating,1)


                player_stat_dict[player_name]["pitching"] = {
                    "ERA": era,
                    "WHIP": whip,
                    "SO/9": so9,
                    "SO/W": sow,
                    "BAbip": babip,
                    "GB/FB": gbfb,
                    "IP": ip,
                    "ERA Percentile": era_percentile,
                    "WHIP Percentile": whip_percentile,
                    "SO/9 Percentile": so9_percentile,
                    "SO/W Percentile": sow_percentile,
                    "BAbip Percentile": babip_percentile,
                    "GB/FB Percentile": gbfb_percentile,
                    "IP Percentile": ip_percentile,
                    "Overall Pitching Rating": f"{pitching_rating}/100"
                }

def display_table():

    table = []

    for player_name in player_stat_dict:

        batting = player_stat_dict[player_name]["batting"]
        pitching = player_stat_dict[player_name]["pitching"]

        row = {
            "Player": player_name.title(),
            "Batting Rating": batting["Overall Batting Rating"],
            "OPS": batting["OPS"],
            "OBP": batting["OBP"],
            "SLG": batting["SLG"],
            "BA": batting["BA"],
            "SB": batting["SB"],
            "OPS Percentile": batting["OPS Percentile"],
            "OBP Percentile": batting["OBP Percentile"],
            "SLG Percentile": batting["SLG Percentile"],
            "BA Percentile": batting["BA Percentile"],
            "SB Percentile": batting["SB Percentile"],
            "Pitching Rating": pitching["Overall Pitching Rating"],
            "ERA": pitching["ERA"],
            "WHIP": pitching["WHIP"],
            "SO/9": pitching["SO/9"],
            "SO/W": pitching["SO/W"],
            "BAbip": pitching["BAbip"],
            "GB/FB": pitching["GB/FB"],
            "IP": pitching["IP"],
            "ERA Percentile": pitching["ERA Percentile"],
            "WHIP Percentile": pitching["WHIP Percentile"],
            "SO/9 Percentile": pitching["SO/9 Percentile"],
            "SO/W Percentile": pitching["SO/W Percentile"],
            "BAbip Percentile": pitching["BAbip Percentile"],
            "GB/FB Percentile": pitching["GB/FB Percentile"],
            "IP Percentile": pitching["IP Percentile"],
        }

        table.append(row)

    print(tabulate(table, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()

