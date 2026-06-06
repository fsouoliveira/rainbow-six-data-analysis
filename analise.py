import pandas as pd

weapons = pd.read_csv("weapons_clean.csv")

media_dano = (
    weapons
    .groupby("type")["stats_damage"]
    .mean()
    .reset_index()
)

media_dano.columns = [
    "weapon_type",
    "average_damage"
]

media_dano = media_dano.sort_values(
    by="average_damage",
    ascending=False
)

print(media_dano)

