# 📊 Análise de Casos de Leptospirose na Região Sul (2014-2023)
  Análise epidemiológica dos casos confirmados de leptospirose nos estados do Paraná, Santa Catarina e Rio Grande do Sul, com base em dados do DATASUS/SINAN.
# 💡 Motivação
  Este projeto nasceu da necessidade de resolver um problema enfrentado por uma pessoa querida, combinando isso com a oportunidade de aplicar e aprimorar conhecimentos adquiridos em mineração de dados. O objetivo foi transformar dados brutos do DATASUS em visualizações claras e insights relevantes sobre a evolução da leptospirose na Região Sul do Brasil.

# 🛠️ Tecnologias Utilizadas
## 🐍 Python - Linguagem principal
## 📊 Pandas - Manipulação e análise de dados
## 📈 Matplotlib - Visualização de dados e gráficos
## 🔢 NumPy - Operações numéricas
  
# 🔧 Funcionalidades
## 1. Consolidação de Dados (scriptAgrupaCSV.py)
Script que processa e consolida múltiplos arquivos CSV anuais em um único dataset:

- Lê 10 arquivos CSV individuais (2014-2023)
- Adiciona coluna de ano a cada registro
- Trata valores ausentes (substitui "-" por 0)
- Converte dados para formato numérico
- Exporta arquivo consolidado leptospirose_2014_2023.csv

# 2. Visualização de Dados (scriptGraficos.py)
- Gera 4 gráficos analíticos com cores pastel:

## 📈 Gráfico 1: Evolução Temporal
 - Linhas mostrando a tendência de casos por estado ao longo dos anos.
<img width="900" height="500" alt="CasosTotaisLeptospirose2014-2023" src="https://github.com/user-attachments/assets/e0fec542-ede8-4e80-9a37-3e23e7229c06" />

## 📊 Gráfico 2: Comparação por Estado
- Barras agrupadas comparando os três estados ano a ano.
<img width="1240" height="662" alt="Evolução dos casos de Leptospirose2014-2023" src="https://github.com/user-attachments/assets/fc820958-6934-440a-a0f2-94eece523c42" />
 
## 🏆 Gráfico 3: Totais Acumulados
- Ranking dos estados por número total de casos no período.
<img width="1200" height="600" alt="ComparaçãoCasosLeptospirosePorEstado2014-2023" src="https://github.com/user-attachments/assets/d61c9a32-47c9-4f26-a2b0-517fe03c472a" />

## 🔍 Gráfico 4: Impacto da Pandemia
- Comparação de médias anuais pré-pandemia (2014-2019) vs pós-pandemia (2020-2023).
<img width="900" height="600" alt="MédiaAnualDeCasosPréPósPandemia" src="https://github.com/user-attachments/assets/87d8304b-7b85-496f-b580-b6c9f401207f" />

# 📝 Fonte dos Dados
Dados extraídos do DATASUS/SINAN (Sistema de Informação de Agravos de Notificação), referentes a casos confirmados de leptospirose notificados nos estados da Região Sul do Brasil.
