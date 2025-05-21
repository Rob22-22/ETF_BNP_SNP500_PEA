import yfinance as yf
import matplotlib.pyplot as plt
import os
import pandas as pd

# ====================== Variables modifiables en haut ======================

ticker = "ESE.PA"
heure_debut = "09:00"
heure_fin = "17:30"

periode_1d_1m = "1d"
intervalle_1d_1m = "1m"

periode_5d_15m = "5d"
intervalle_5d_15m = "15m"

periode_3mo_1h = "3mo"
intervalle_3mo_1h = "1h"

periode_6mo_1h = "6mo"
intervalle_6mo_1h = "1h"

periode_1y_1h = "1y"
intervalle_1y_1h = "1h"

periode_5y_1d = "5y"
intervalle_5y_1d = "1d"

periode_10y_1d = "10y"
intervalle_10y_1d = "1d"

chemin_dossier_csv = "C:\\Users\\robin.guichon\\Documents\\Test\\csv"
chemin_dossier_graphe = "C:\\Users\\robin.guichon\\Documents\\Test\\graphe"

# Nouveau paramètre taille de figure
taille_figure = (28, 12)

os.makedirs(chemin_dossier_csv, exist_ok=True)
os.makedirs(chemin_dossier_graphe, exist_ok=True)


# ========================================================================================== 1d/1m ==========================================================================================

data = yf.download(ticker, period=periode_1d_1m, interval=intervalle_1d_1m)
data = data.tz_convert('Europe/Paris')

data = data.between_time(heure_debut, heure_fin)
data.reset_index(inplace=True)

x = range(len(data))
y = data['Close']
labels = data['Datetime'].dt.strftime("%d/%m %H:%M")

plt.figure(figsize=taille_figure)
plt.plot(x, y, label=ticker, color='black')
plt.xlabel("Date")
plt.ylabel("Prix (€)")
plt.title(f"{periode_1d_1m}/{intervalle_1d_1m}")
plt.grid(axis='y')
plt.legend()

step = max(len(x) // 10, 1)
plt.xticks(ticks=x[::step], labels=labels[::step], rotation=45)

plt.tight_layout()

data.to_csv(os.path.join(chemin_dossier_csv, f"{periode_1d_1m}_{intervalle_1d_1m}_{ticker.replace('.', '_')}.csv"), index=False)
plt.savefig(os.path.join(chemin_dossier_graphe, f"{periode_1d_1m}_{intervalle_1d_1m}_{ticker.replace('.', '_')}.png"))
plt.close()


# ========================================================================================== 5d/15m ==========================================================================================

data = yf.download(ticker, period=periode_5d_15m, interval=intervalle_5d_15m)
data = data.tz_convert('Europe/Paris')

data = data.between_time(heure_debut, heure_fin)
data.reset_index(inplace=True)

x = range(len(data))
y = data['Close']
labels = data['Datetime'].dt.strftime("%d/%m %H:%M")

plt.figure(figsize=taille_figure)
plt.plot(x, y, label=ticker, color='black')
plt.xlabel("Date")
plt.ylabel("Prix (€)")
plt.title(f"{periode_5d_15m}/{intervalle_5d_15m}")
plt.grid(axis='y')
plt.legend()

step = max(len(x) // 10, 1)
plt.xticks(ticks=x[::step], labels=labels[::step], rotation=45)

plt.tight_layout()

data.to_csv(os.path.join(chemin_dossier_csv, f"{periode_5d_15m}_{intervalle_5d_15m}_{ticker.replace('.', '_')}.csv"), index=False)
plt.savefig(os.path.join(chemin_dossier_graphe, f"{periode_5d_15m}_{intervalle_5d_15m}_{ticker.replace('.', '_')}.png"))
plt.close()


# ========================================================================================== 3mo/1h ==========================================================================================

data = yf.download(ticker, period=periode_3mo_1h, interval=intervalle_3mo_1h)
data = data.tz_convert('Europe/Paris')

data = data.between_time(heure_debut, heure_fin)
data.reset_index(inplace=True)

x = range(len(data))
y = data['Close']
labels = data['Datetime'].dt.strftime("%d/%m %H:%M")

plt.figure(figsize=taille_figure)
plt.plot(x, y, label=ticker, color='black')
plt.xlabel("Date")
plt.ylabel("Prix (€)")
plt.title(f"{periode_3mo_1h}/{intervalle_3mo_1h}")
plt.grid(axis='y')
plt.legend()

step = max(len(x) // 10, 1)
plt.xticks(ticks=x[::step], labels=labels[::step], rotation=45)

plt.tight_layout()

data.to_csv(os.path.join(chemin_dossier_csv, f"{periode_3mo_1h}_{intervalle_3mo_1h}_{ticker.replace('.', '_')}.csv"), index=False)
plt.savefig(os.path.join(chemin_dossier_graphe, f"{periode_3mo_1h}_{intervalle_3mo_1h}_{ticker.replace('.', '_')}.png"))
plt.close()


# ========================================================================================== 6mo/1h ==========================================================================================

data = yf.download(ticker, period=periode_6mo_1h, interval=intervalle_6mo_1h)
data = data.tz_convert('Europe/Paris')

data = data.between_time(heure_debut, heure_fin)
data.reset_index(inplace=True)

x = range(len(data))
y = data['Close']
labels = data['Datetime'].dt.strftime("%d/%m %H:%M")

plt.figure(figsize=taille_figure)
plt.plot(x, y, label=ticker, color='black')
plt.xlabel("Date")
plt.ylabel("Prix (€)")
plt.title(f"{periode_6mo_1h}/{intervalle_6mo_1h}")
plt.grid(axis='y')
plt.legend()

step = max(len(x) // 10, 1)
plt.xticks(ticks=x[::step], labels=labels[::step], rotation=45)

plt.tight_layout()

data.to_csv(os.path.join(chemin_dossier_csv, f"{periode_6mo_1h}_{intervalle_6mo_1h}_{ticker.replace('.', '_')}.csv"), index=False)
plt.savefig(os.path.join(chemin_dossier_graphe, f"{periode_6mo_1h}_{intervalle_6mo_1h}_{ticker.replace('.', '_')}.png"))
plt.close()


# ========================================================================================== 1y/1h ==========================================================================================

data = yf.download(ticker, period=periode_1y_1h, interval=intervalle_1y_1h)
data = data.tz_convert('Europe/Paris')

data = data.between_time(heure_debut, heure_fin)
data.reset_index(inplace=True)

x = range(len(data))
y = data['Close']
labels = data['Datetime'].dt.strftime("%d/%m %H:%M")

plt.figure(figsize=taille_figure)
plt.plot(x, y, label=ticker, color='black')
plt.xlabel("Date")
plt.ylabel("Prix (€)")
plt.title(f"{periode_1y_1h}/{intervalle_1y_1h}")
plt.grid(axis='y')
plt.legend()

step = max(len(x) // 10, 1)
plt.xticks(ticks=x[::step], labels=labels[::step], rotation=45)

plt.tight_layout()

data.to_csv(os.path.join(chemin_dossier_csv, f"{periode_1y_1h}_{intervalle_1y_1h}_{ticker.replace('.', '_')}.csv"), index=False)
plt.savefig(os.path.join(chemin_dossier_graphe, f"{periode_1y_1h}_{intervalle_1y_1h}_{ticker.replace('.', '_')}.png"))
plt.close()


# ========================================================================================== 5y/1d ==========================================================================================

data = yf.download(ticker, period=periode_5y_1d, interval=intervalle_5y_1d)
dates = data.index
prix = data['Close']

plt.figure(figsize=taille_figure)
plt.plot(dates, prix, label=ticker, color='black')
plt.xlabel("Date")
plt.ylabel("Prix (€)")
plt.title(f"{periode_5y_1d}/{intervalle_5y_1d}")
plt.grid(axis='y')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

data.to_csv(os.path.join(chemin_dossier_csv, f"{periode_5y_1d}_{intervalle_5y_1d}_{ticker.replace('.', '_')}.csv"))
plt.savefig(os.path.join(chemin_dossier_graphe, f"{periode_5y_1d}_{intervalle_5y_1d}_{ticker.replace('.', '_')}.png"))
plt.close()


# ========================================================================================== 10y/1d ==========================================================================================

data = yf.download(ticker, period=periode_10y_1d, interval=intervalle_10y_1d)
dates = data.index
prix = data['Close']

plt.figure(figsize=taille_figure)
plt.plot(dates, prix, label=ticker, color='black')
plt.xlabel("Date")
plt.ylabel("Prix (€)")
plt.title(f"{periode_10y_1d}/{intervalle_10y_1d}")
plt.grid(axis='y')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

data.to_csv(os.path.join(chemin_dossier_csv, f"{periode_10y_1d}_{intervalle_10y_1d}_{ticker.replace('.', '_')}.csv"))
plt.savefig(os.path.join(chemin_dossier_graphe, f"{periode_10y_1d}_{intervalle_10y_1d}_{ticker.replace('.', '_')}.png"))
plt.close()
