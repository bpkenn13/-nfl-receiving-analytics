import pandas as pd

stats = pd.read_csv("receiving_weekly.csv")

megatron = stats[stats["player_display_name"] == "Calvin Johnson"].query("season == 2011") 

print(megatron.head(7)["receiving_yards"].sum())
print(megatron.head(7)["receiving_tds"].sum())
print(megatron.head(7)["receptions"].sum())

sungod = stats[stats["player_display_name"] == "Amon-Ra St. Brown"].query("season == 2026")

print(sungod.head(7)["receiving_yards"].sum())
print(sungod.head(7)["receiving_tds"].sum())
print(sungod.head(7)["receptions"].sum())