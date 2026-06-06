# Rainbow Six Siege Data Analysis

## Sobre o Projeto

Este projeto utiliza Python e Pandas para realizar análise de dados sobre o jogo Rainbow Six Siege.

O objetivo é aplicar técnicas de:

* Limpeza de dados
* Transformação de dados
* Análise estatística
* Cruzamento de tabelas (JOIN)
* Geração de insights

## Dataset

Fonte dos dados:

https://www.kaggle.com/datasets/ektarr/rainbow-six-siege-encyclopedia

Arquivos utilizados:

* operators.csv
* weapons.csv
* seasons.csv

## Tecnologias

* Python
* Pandas
* Git
* GitHub

## Estrutura do Projeto

```text
data/
outputs/

limpeza.py
analise.py
joins.py
```

## Análises Realizadas

### 1. Limpeza de Dados

* Identificação de valores nulos
* Tratamento das colunas barrels e grips
* Remoção de registros duplicados

### 2. Cruzamento de Dados (JOIN)

Pergunta respondida:

Quais operadores foram introduzidos na mesma temporada que um mapa específico?

Exemplo:

* House Rework → Ace e Melusi

### 3. Análise Estatística

Pergunta respondida:

Qual a média de dano das armas por categoria?

Resultado:

* Shotguns apresentam o maior dano médio do conjunto analisado.

## Como Executar

```bash
pip install -r requirements.txt

python limpeza.py
python joins.py
python analise.py
```

## Autor

Felipe Oliveira
