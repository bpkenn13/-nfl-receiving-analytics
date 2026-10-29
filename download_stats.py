import nflreadpy as nfl

seasons = [2001, 2002, 2007, 2011, 2012, 2026]  # HOF test seasons + current

stats = nfl.load_player_stats(seasons, summary_level="week").to_pandas()

# Regular season only, receiving columns only
stats = stats[stats["season_type"] == "REG"]
cols = ["player_id", "player_display_name", "position", "season", "week",
        "team", "receptions", "receiving_yards", "receiving_tds"]
stats = stats[cols]

stats.to_csv("receiving_weekly.csv", index=False)
print(stats.shape)
print(stats.head())

print(stats[stats["player_display_name"] == "Randy Moss"].query("season == 2007"))
print(stats[stats["player_display_name"] == "Calvin Johnson"].query("season == 2011")) 

