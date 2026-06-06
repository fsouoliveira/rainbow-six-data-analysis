import pandas as pd

# =====================================================
# CARREGAMENTO DOS DADOS
# =====================================================

operators = pd.read_csv("operators.csv")
weapons = pd.read_csv("weapons.csv")

# =====================================================
# VISUALIZAÇÃO INICIAL
# =====================================================

print("=== OPERATORS ===")
print(operators.head())

print("\n=== WEAPONS ===")
print(weapons.head())

# =====================================================
# VALORES NULOS
# =====================================================

print("\n=== VALORES NULOS OPERATORS ===")
print(operators.isnull().sum())

print("\n=== VALORES NULOS WEAPONS ===")
print(weapons.isnull().sum())

# =====================================================
# TRATAMENTO DE VALORES NULOS
# =====================================================

weapons["barrels"] = weapons["barrels"].fillna("No Barrel")
weapons["grips"] = weapons["grips"].fillna("No Grip")

print("\n=== NULOS APÓS TRATAMENTO ===")
print(weapons.isnull().sum())

# =====================================================
# DUPLICADOS
# =====================================================

print("\n=== DUPLICADOS ANTES DA LIMPEZA ===")
print(f"Operators: {operators.duplicated().sum()}")
print(f"Weapons: {weapons.duplicated().sum()}")

operators = operators.drop_duplicates()
weapons = weapons.drop_duplicates()

print("\n=== DUPLICADOS APÓS LIMPEZA ===")
print(f"Operators: {operators.duplicated().sum()}")
print(f"Weapons: {weapons.duplicated().sum()}")

# =====================================================
# ESTRUTURA DOS DADOS
# =====================================================

print("\n=== INFO OPERATORS ===")
operators.info()

print("\n=== INFO WEAPONS ===")
weapons.info()

# =====================================================
# TIPOS DAS COLUNAS
# =====================================================

print("\n=== TIPOS OPERATORS ===")
print(operators.dtypes)

print("\n=== TIPOS WEAPONS ===")
print(weapons.dtypes)

# =====================================================
# ESTATÍSTICAS DESCRITIVAS
# =====================================================

print("\n=== ESTATÍSTICAS OPERATORS ===")
print(operators.describe(include="all"))

print("\n=== ESTATÍSTICAS WEAPONS ===")
print(weapons.describe(include="all"))

# =====================================================
# VALORES ÚNICOS (COLUNAS DE TEXTO)
# =====================================================

print("\n=== VALORES ÚNICOS OPERATORS ===")

for coluna in operators.select_dtypes(include="object").columns:
    print(f"\nColuna: {coluna}")
    print(f"Valores únicos: {operators[coluna].nunique()}")

print("\n=== VALORES ÚNICOS WEAPONS ===")

for coluna in weapons.select_dtypes(include="object").columns:
    print(f"\nColuna: {coluna}")
    print(f"Valores únicos: {weapons[coluna].nunique()}")

# =====================================================
# DIMENSÕES FINAIS
# =====================================================

print("\n=== DIMENSÕES FINAIS ===")
print(f"Operators: {operators.shape}")
print(f"Weapons: {weapons.shape}")

# =====================================================
# EXPORTAÇÃO DOS DADOS TRATADOS
# =====================================================

operators.to_csv("operators_clean.csv", index=False)
weapons.to_csv("weapons_clean.csv", index=False)

print("\nArquivos salvos com sucesso!")
print("operators_clean.csv")
print("weapons_clean.csv")