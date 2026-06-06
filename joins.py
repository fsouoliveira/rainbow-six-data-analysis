import pandas as pd

# =====================================================
# CARREGAMENTO DOS DADOS
# =====================================================

operators = pd.read_csv("operators.csv")
seasons = pd.read_csv("seasons.csv")

# =====================================================
# JOIN ENTRE OPERADORES E TEMPORADAS
# =====================================================

join_df = pd.merge(
    operators,
    seasons,
    left_on="season_introduced",
    right_on="code",
    how="inner"
)

# =====================================================
# FUNÇÃO DE CONSULTA
# =====================================================

def operadores_por_mapa(mapa):

    resultado = join_df[
        join_df["map"]
        .fillna("")
        .str.contains(mapa, case=False)
    ]

    return resultado[
        [
            "name_x",
            "season_introduced",
            "name_y",
            "map"
        ]
    ].rename(
        columns={
            "name_x": "operator",
            "season_introduced": "season",
            "name_y": "season_name"
        }
    )

# =====================================================
# CONSULTAS
# =====================================================

print("\n=== HOUSE REWORK ===")
print(operadores_por_mapa("House Rework"))

print("\n=== VILLA ===")
print(operadores_por_mapa("Villa"))

print("\n=== COASTLINE ===")
print(operadores_por_mapa("Coastline"))