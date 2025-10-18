import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patheffects

# Leitura e preparação dos dados
df = pd.read_csv("leptospirose_2014_2023.csv", sep=";", encoding="utf-8-sig")

for col in ["PR", "SC", "RS", "Total"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

df = df[~df["UF de notificação"].str.contains("Total", case=False, na=False)]

# ✅ CORREÇÃO PRINCIPAL: Agregar por ano
df_ano = df.groupby('Ano')[['PR', 'SC', 'RS']].sum().reset_index()

# ✅ Paleta de cores PASTEL
cores = {"PR": "#FFB3BA", "SC": "#BAE1FF", "RS": "#BAFFC9"}

# Gráfico 1 – Evolução temporal COM TODOS OS ANOS NO EIXO X
plt.figure(figsize=(14, 8))

offsets = {"PR": (0, 22), "SC": (-25, 6), "RS": (25, 6)}

for estado in ["PR", "SC", "RS"]:
    linha = plt.plot(df_ano["Ano"], df_ano[estado], marker="o", label=estado, 
                     linewidth=2.5, markersize=8, color=cores[estado])
    
    for x, y in zip(df_ano["Ano"], df_ano[estado]):
        texto = plt.annotate(f'{int(y)}', 
                     xy=(x, y), 
                     xytext=offsets[estado],
                     textcoords='offset points',
                     ha='center',
                     fontsize=10,
                     fontweight='bold',
                     color=cores[estado])
        
        texto.set_path_effects([
            patheffects.Stroke(linewidth=2, foreground='black'),
            patheffects.Normal()
        ])

plt.title("Evolução dos casos de Leptospirose (2014–2023)", fontsize=14)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Casos confirmados", fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# ✅ FORÇAR EXIBIÇÃO DE TODOS OS ANOS
plt.xticks(df_ano["Ano"])
plt.ylim(bottom=0, top=df_ano[["PR", "SC", "RS"]].max().max() * 1.18)

plt.tight_layout()
plt.show()

# Gráfico 2 – Comparação (barras agrupadas) COM TODOS OS ANOS
df_melt = df_ano.melt(id_vars="Ano", value_vars=["PR", "SC", "RS"],
                      var_name="Estado", value_name="Casos")

fig, ax = plt.subplots(figsize=(12, 6))
for i, estado in enumerate(["PR", "SC", "RS"]):
    subset = df_melt[df_melt["Estado"] == estado]
    barras = ax.bar(subset["Ano"] + (i - 1)*0.25, subset["Casos"], 
                     width=0.25, label=estado, color=cores[estado],
                     edgecolor='gray', linewidth=0.5)
    
    for barra, valor in zip(barras, subset["Casos"]):
        altura = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2., altura,
                f'{int(valor)}',
                ha='center', va='bottom', fontsize=8.5, fontweight='bold')

y_max = df_melt["Casos"].max()
ax.set_ylim(0, y_max * 1.08)

# ✅ FORÇAR EXIBIÇÃO DE TODOS OS ANOS NO GRÁFICO 2
ax.set_xticks(df_ano["Ano"])
ax.set_xticklabels(df_ano["Ano"])

ax.set_title("Comparação de casos de Leptospirose por estado (2014–2023)")
ax.set_xlabel("Ano")
ax.set_ylabel("Casos confirmados")
ax.legend()
plt.tight_layout()
plt.show()

# Gráfico 3 – Total acumulado COM CORES PASTEL
totais = df_ano[["PR", "SC", "RS"]].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
cores_totais = [cores["RS"], cores["PR"], cores["SC"]]
barras = ax.barh(totais.index, totais.values, color=cores_totais,
                 edgecolor='gray', linewidth=0.5)

for barra, valor in zip(barras, totais.values):
    largura = barra.get_width()
    ax.text(largura + 50, barra.get_y() + barra.get_height()/2.,
            f'{int(valor)}',
            ha='left', va='center', fontsize=11, fontweight='bold')

x_max = totais.max()
ax.set_xlim(0, x_max * 1.08)

ax.set_title("Casos totais de Leptospirose (2013–2023)")
ax.set_xlabel("Casos acumulados")
ax.set_ylabel("Estado")
plt.tight_layout()
plt.show()

# Gráfico 4 – Pré/Pós pandemia COM CORES PASTEL
pre = df_ano[df_ano["Ano"] < 2020][["PR", "SC", "RS"]].mean()
pos = df_ano[df_ano["Ano"] >= 2020][["PR", "SC", "RS"]].mean()

comparativo = pd.DataFrame({
    "Pré-pandemia (2014–2019)": pre, 
    "Pós-pandemia (2020–2023)": pos
})

ax = comparativo.plot(kind="bar", figsize=(9, 6), 
                      color=["#FFABAB", "#C7CEEA"],
                      edgecolor='gray', linewidth=0.5)
plt.title("Média anual de casos – antes e depois da pandemia")
plt.ylabel("Casos médios por ano")
plt.xlabel("Estado")
plt.xticks(rotation=0)

for container in ax.containers:
    ax.bar_label(container, fmt='%.1f', padding=3, fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()

print("✅ Gráficos com cores pastel gerados com sucesso!")