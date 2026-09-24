"""
Genera las gráficas de charts/ a partir del archivo de datos original
(Analisis_descriptiva.xlsx, hojas 'Dataset' y 'Usuarios').

El archivo de datos NO se incluye en este repositorio por confidencialidad
(ver README.md y DATA_DICTIONARY.md). Coloca tu copia local en data/raw/
y ajusta la variable SRC antes de ejecutar.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import warnings
warnings.filterwarnings("ignore")

SRC = "data/raw/Analisis_descriptiva.xlsx"  # <- coloca aquí tu copia local (no se sube a git)
OUT = "charts"

ds = pd.read_excel(SRC, sheet_name="Dataset")
us = pd.read_excel(SRC, sheet_name="Usuarios")
ds.columns = [c.strip() for c in ds.columns]
us.columns = [c.strip() for c in us.columns]

BLUE, SURFACE, TEXT_PRIMARY, TEXT_SECOND, GRID = "#2a78d6", "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3de"
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": GRID,
    "axes.labelcolor": TEXT_SECOND, "text.color": TEXT_PRIMARY,
    "xtick.color": TEXT_SECOND, "ytick.color": TEXT_SECOND, "font.size": 11,
})

def style_ax(ax):
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(length=0)

# 1. Género
g = ds.groupby("GENRE")["SCREENTIME_HOUR"].sum().sort_values(ascending=False).head(8).sort_values()
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(g.index, g.values, color=BLUE, height=0.6)
for b, v in zip(bars, g.values):
    ax.text(v + g.values.max()*0.01, b.get_y()+b.get_height()/2, f"{v:,.0f} h", va="center", fontsize=9.5)
ax.set_title("Horas de consumo por género (top 8)", loc="left", fontsize=13, fontweight="bold", pad=14)
ax.set_xlabel("Horas de pantalla (screentime)")
style_ax(ax); ax.set_xlim(0, g.values.max()*1.15)
plt.tight_layout(); plt.savefig(f"{OUT}/01_genero.png", dpi=180, bbox_inches="tight"); plt.close()

# 2. Dispositivo
d = ds.groupby("DEVICE")["SCREENTIME_HOUR"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(d.index, d.values, color=BLUE, width=0.55)
for b, v in zip(bars, d.values):
    ax.text(b.get_x()+b.get_width()/2, v+d.values.max()*0.02, f"{v:,.0f} h", ha="center", fontsize=9.5)
ax.set_title("Horas de consumo por dispositivo", loc="left", fontsize=13, fontweight="bold", pad=14)
ax.set_ylabel("Horas de pantalla"); style_ax(ax); ax.set_ylim(0, d.values.max()*1.18)
plt.tight_layout(); plt.savefig(f"{OUT}/02_dispositivo.png", dpi=180, bbox_inches="tight"); plt.close()

# 3. Tendencia diaria
daily = ds.groupby(ds["DATE"].dt.day)["SCREENTIME_HOUR"].sum()
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(daily.index, daily.values, color=BLUE, linewidth=2)
ax.fill_between(daily.index, daily.values, color=BLUE, alpha=0.08)
ax.set_title("Consumo diario de video durante marzo 2024", loc="left", fontsize=13, fontweight="bold", pad=14)
ax.set_xlabel("Día del mes"); ax.set_ylabel("Horas de pantalla")
style_ax(ax); ax.grid(axis="y", color=GRID, linewidth=0.8); ax.set_axisbelow(True)
plt.tight_layout(); plt.savefig(f"{OUT}/03_tendencia_diaria.png", dpi=180, bbox_inches="tight"); plt.close()

# 4. Top títulos
t = ds.groupby("TITLE")["SCREENTIME_HOUR"].sum().sort_values(ascending=False).head(10).sort_values()
fig, ax = plt.subplots(figsize=(8, 5.5))
bars = ax.barh(t.index, t.values, color=BLUE, height=0.6)
for b, v in zip(bars, t.values):
    ax.text(v + t.values.max()*0.01, b.get_y()+b.get_height()/2, f"{v:,.0f} h", va="center", fontsize=9.5)
ax.set_title("Top 10 títulos más vistos (horas totales)", loc="left", fontsize=13, fontweight="bold", pad=14)
ax.set_xlabel("Horas de pantalla"); style_ax(ax); ax.set_xlim(0, t.values.max()*1.2)
plt.tight_layout(); plt.savefig(f"{OUT}/04_top_titulos.png", dpi=180, bbox_inches="tight"); plt.close()

# 5. Multidispositivo
disp_col = "#_DISPOSITIVOS"
cnt = us[disp_col].apply(lambda x: "1 dispositivo" if x == 1 else "Más de 1 dispositivo").value_counts()
cnt = cnt.reindex(["1 dispositivo", "Más de 1 dispositivo"])
fig, ax = plt.subplots(figsize=(6, 4.5))
bars = ax.bar(cnt.index, cnt.values, color=BLUE, width=0.5)
for b, v in zip(bars, cnt.values):
    pct = v / cnt.sum() * 100
    ax.text(b.get_x()+b.get_width()/2, v+cnt.values.max()*0.02, f"{v:,} ({pct:.1f}%)", ha="center", fontsize=9.5)
ax.set_title("Usuarios según número de dispositivos usados", loc="left", fontsize=13, fontweight="bold", pad=14)
ax.set_ylabel("Usuarios"); style_ax(ax); ax.set_ylim(0, cnt.values.max()*1.2)
plt.tight_layout(); plt.savefig(f"{OUT}/05_multidispositivo.png", dpi=180, bbox_inches="tight"); plt.close()

# 6. Regiones
r = ds.groupby("REGION")["SCREENTIME_HOUR"].sum().sort_values(ascending=False).head(10).sort_values()
fig, ax = plt.subplots(figsize=(8, 5.5))
bars = ax.barh(r.index, r.values, color=BLUE, height=0.6)
for b, v in zip(bars, r.values):
    ax.text(v + r.values.max()*0.01, b.get_y()+b.get_height()/2, f"{v:,.0f} h", va="center", fontsize=9.5)
ax.set_title("Top 10 regiones por horas de consumo", loc="left", fontsize=13, fontweight="bold", pad=14)
ax.set_xlabel("Horas de pantalla"); style_ax(ax); ax.set_xlim(0, r.values.max()*1.15)
plt.tight_layout(); plt.savefig(f"{OUT}/06_regiones.png", dpi=180, bbox_inches="tight"); plt.close()

print("Listo: 6 gráficas generadas en charts/")
