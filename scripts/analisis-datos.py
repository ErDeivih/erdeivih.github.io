# -*- coding: utf-8 -*-
"""Genera los gráficos de la sección «Datos y análisis» con NumPy y matplotlib.

Fuentes:
  - Cobertura del catálogo de Fondo Popular: tabla canónica publicada el 10/11/2026
    (docs del proyecto facylf; total 867 competiciones, 206 completas).
  - Fútbol y xG: dataset CC0 `futbol-partidos.csv` de Data School (380 partidos).
  - Cartera: dataset CC0 `cartera-acciones.csv` de Data School (120 meses, 3 activos).

Salida: public/analisis/*.png (2400x1350, fondo del sitio). Reproducible:
  python scripts/analisis-datos.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "analisis"
DATOS = Path(r"F:\Proyectos\data-school\datasets\csv")
OUT.mkdir(parents=True, exist_ok=True)

FONDO, TINTA, SUAVE = "#f2efe7", "#181814", "#615f58"
PRIMARIO, SECUNDARIO, ACENTO = "#f0522d", "#3655f5", "#087e6b"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13,
    "figure.facecolor": FONDO, "axes.facecolor": FONDO,
    "axes.edgecolor": TINTA, "axes.labelcolor": TINTA,
    "xtick.color": TINTA, "ytick.color": TINTA, "text.color": TINTA,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": TINTA, "grid.alpha": 0.12, "grid.linewidth": 0.8,
})


def guardar(fig, nombre):
    destino = OUT / nombre
    fig.savefig(destino, dpi=200, bbox_inches="tight", facecolor=FONDO)
    plt.close(fig)
    print("OK", destino, f"{destino.stat().st_size // 1024} KB")


# 1) Cobertura del catálogo de Fondo Popular (datos publicados)
temporadas = np.array(["2012-13","2013-14","2014-15","2015-16","2016-17","2017-18",
                       "2018-19","2019-20","2020-21","2021-22","2022-23","2023-24",
                       "2024-25","2025-26","2026-27"])
ediciones = np.array([3,46,61,65,58,60,61,56,31,66,70,83,79,71,57])
completas = np.array([2,5,18,9,6,10,9,1,16,12,32,24,41,20,1])
cobertura = np.divide(completas, ediciones) * 100
total_ed, total_com = int(ediciones.sum()), int(completas.sum())
global_pct = total_com / total_ed * 100

fig, ax = plt.subplots(figsize=(12, 6.75))
colores = [PRIMARIO if c >= global_pct else SECUNDARIO for c in cobertura]
barras = ax.bar(temporadas, cobertura, color=colores, width=0.72)
ax.axhline(global_pct, color=TINTA, linewidth=1.4, linestyle="--")
ax.text(1.012, global_pct, f"media\n{global_pct:.1f} %", transform=ax.get_yaxis_transform(), ha="left", va="center", fontsize=11)
for barra, valor, ed in zip(barras, cobertura, ediciones):
    ax.text(barra.get_x() + barra.get_width() / 2, valor + 1.2, f"{valor:.0f}%", ha="center", fontsize=10)
ax.set_ylim(0, 105)
ax.set_ylabel("% de ediciones completas")
ax.set_title(f"Cobertura del catálogo de Fondo Popular · {total_ed} competiciones, {total_com} completas ({global_pct:.1f} %)", loc="left", fontsize=15, pad=14)
ax.set_xticks(np.arange(len(temporadas)))
ax.set_xticklabels([t[2:] for t in temporadas])
ax.tick_params(axis="x", rotation=0)
guardar(fig, "cobertura-fondo-popular.png")

# 2) Fútbol y xG (dataset CC0 de Data School)
f = pd.read_csv(DATOS / "futbol-partidos.csv")
goles_local = f["goles_local"].to_numpy(dtype=int)
goles_visitante = f["goles_visitante"].to_numpy(dtype=int)
goles = goles_local + goles_visitante
xg = (f["xg_local"] + f["xg_visitante"]).to_numpy(dtype=float)
local_pct = (goles_local > goles_visitante).mean() * 100
empate_pct = (goles_local == goles_visitante).mean() * 100
visitante_pct = (goles_local < goles_visitante).mean() * 100
correlacion = np.corrcoef(xg, goles)[0, 1]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6.0), gridspec_kw={"width_ratios": [1, 1]})
valores, cuentas = np.unique(goles, return_counts=True)
ax1.bar(valores, cuentas / len(goles) * 100, color=PRIMARIO, width=0.7)
ax1.set_title(f"Goles por partido · media {goles.mean():.2f}", loc="left", fontsize=14)
ax1.set_xlabel("goles en el partido")
ax1.set_ylabel("% de partidos")
ax1.set_xticks(valores)
ax2.scatter(xg, goles, s=8, color=SECUNDARIO, alpha=0.28, edgecolors="none")
limite = [0, max(xg.max(), goles.max()) + 0.5]
ax2.plot(limite, limite, color=TINTA, linewidth=1.2, linestyle="--")
ax2.set_title(f"xG esperado frente a goles reales · r = {correlacion:.2f}", loc="left", fontsize=14)
ax2.set_xlabel("xG del partido")
ax2.set_ylabel("goles reales")
fig.suptitle(f"Fútbol: {len(f)} partidos · local gana {local_pct:.0f} %, empate {empate_pct:.0f} %, visitante {visitante_pct:.0f} %", x=0.01, ha="left", fontsize=15)
fig.tight_layout()
guardar(fig, "futbol-goles-xg.png")

# 3) Cartera: rentabilidad y volatilidad (dataset CC0 de Data School)
c = pd.read_csv(DATOS / "cartera-acciones.csv")
meses = np.unique(c["mes"].to_numpy())
activos = list(dict.fromkeys(c["activo"].tolist()))
fig, ax = plt.subplots(figsize=(12, 6.0))
paleta = [TINTA, PRIMARIO, SECUNDARIO, ACENTO, "#8a5a2b", "#6b7a8a"]
colores = {a: paleta[i % len(paleta)] for i, a in enumerate(activos)}
resumen = []
for activo in activos:
    retornos = c.loc[c["activo"] == activo, "retorno"].to_numpy(dtype=float)
    acumulado = np.cumprod(1 + retornos)
    vol = retornos.std(ddof=1) * np.sqrt(12) * 100
    anual = (acumulado[-1] ** (12 / len(retornos)) - 1) * 100
    ax.plot(np.arange(len(acumulado)), acumulado, linewidth=2.2,
            label=f"{activo} · {anual:+.1f} % anual · vol {vol:.1f} %", color=colores[activo])
ax.set_xticks(np.arange(0, len(meses), 12))
ax.set_xticklabels([m[:4] for m in meses[::12]], rotation=0)
ax.set_ylabel("crecimiento de 1 €")
ax.set_title(f"Cartera: 1 € invertido en cada activo ({len(meses)} meses)", loc="left", fontsize=15, pad=14)
ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.10), fontsize=10.5)
guardar(fig, "cartera-rentabilidad-volatilidad.png")

# 4) Ventas por tienda y día de la semana (dataset CC0 de Data School)
v = pd.read_csv(DATOS / "ventas-mensuales.csv")
ingresos = v["ingresos"].to_numpy(dtype=float)
tiendas = v["tienda"].to_numpy()
dias = pd.to_datetime(v["fecha"]).dt.dayofweek.to_numpy()
nombres_dias = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]
totales_tienda = np.array([ingresos[tiendas == t].sum() for t in np.unique(tiendas)])
medias_dia = np.array([ingresos[dias == d].mean() for d in range(7)])
etiquetas_tienda = [str(t) for t in np.unique(tiendas)]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.8), gridspec_kw={"width_ratios": [1, 1.35]})
barras = ax1.bar(etiquetas_tienda, totales_tienda, color=[SECUNDARIO, PRIMARIO, ACENTO], width=0.66)
for barra, valor in zip(barras, totales_tienda):
    ax1.text(barra.get_x() + barra.get_width() / 2, valor * 0.5, f"{valor/1000:.1f}".replace(".", ",") + " k€", ha="center", color="white", fontweight="bold", fontsize=12)
ax1.set_title("Ingresos por tienda · 6 meses", loc="left", fontsize=14)
ax1.set_ylabel("ingresos (€)")
ax1.set_ylim(0, totales_tienda.max() * 1.12)
colores_dia = [SUAVE if d < 5 else PRIMARIO for d in range(7)]
ax2.bar(nombres_dias, medias_dia, color=colores_dia, width=0.7)
ax2.set_title("Ingreso medio por día de la semana", loc="left", fontsize=14)
ax2.set_ylabel("ingresos medios (€)")
ax2.set_ylim(0, medias_dia.max() * 1.18)
for i, valor in enumerate(medias_dia):
    ax2.text(i, valor + medias_dia.max() * 0.03, f"{valor:,.0f}".replace(",", "."), ha="center", fontsize=10)
fig.suptitle(f"Ventas de tres tiendas de barrio: {ingresos.sum():,.0f} € en {len(v)} días de registro".replace(",", "."), x=0.01, ha="left", fontsize=15)
fig.tight_layout()
guardar(fig, "ventas-tienda-dia-semana.png")

print("Gráficos generados en", OUT)
