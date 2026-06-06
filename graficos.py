import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
weapons = pd.read_csv("outputs/weapons_clean.csv")

# Contagem de armas por categoria
weapon_count = weapons["type"].value_counts()

# Criar gráfico
plt.figure(figsize=(10, 6))

weapon_count.plot(kind="bar")

plt.title("Quantidade de Armas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade")

plt.tight_layout()

# Salvar imagem
plt.savefig("images/charts/weapons_by_type.png")

#plt.show()