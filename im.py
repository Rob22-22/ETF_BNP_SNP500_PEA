import yfinance as yf
import matplotlib.pyplot as plt
import os
import pandas as pd

# Dossier de sauvegarde
chemin_dossier = "C:\\Users\\robin.guichon\\Documents\\Test"
os.makedirs(chemin_dossier, exist_ok=True)

# Télécharger les données minute par minute pour ESE.PA
data = yf.download("ESE.PA", period="3d", interval="1m")
data = data.tz_convert('Europe/Paris')  # Fuseau horaire Paris

# Garder seulement les heures d'ouverture (9h à 17h30)
data = data.between_time("09:00", "17:30")

# Réinitialiser l’index pour manipuler comme liste continue
data.reset_index(inplace=True)

# Créer un nouvel index pour que matplotlib n'interprète pas les sauts de temps
x = range(len(data))
y = data['Close']
labels = data['Datetime'].dt.strftime("%d/%m %H:%M")

# Tracer
plt.figure(figsize=(14, 6))
plt.plot(x, y, label="ESE.PA - Prix minute", color='blue')
plt.xlabel("Temps (minutes de marché)")
plt.ylabel("Prix (€)")
plt.title("Prix minute par minute - Heures d'ouverture uniquement (ESE.PA)")
plt.grid(True)
plt.legend()

# Afficher seulement quelques labels pour ne pas surcharger l’axe
step = len(x) // 10  # 10 labels max
plt.xticks(ticks=x[::step], labels=labels[::step], rotation=45)

plt.tight_layout()
plt.show()




# Définir le chemin où tu veux enregistrer les fichiers (ici, sur le Bureau dans 'finance')
chemin_dossier = "C:\\Users\\robin.guichon\\Documents\\Test"

# Créer le dossier si nécessaire
os.makedirs(chemin_dossier, exist_ok=True)

# Télécharger les données historiques de l'ETF ESE.PA
data = yf.download("ESE.PA", start="2018-01-01", end="2025-05-20")
print(data['Close'].head())
dates = data.index
prix = data['Close']

# Télécharger les données de l'indice S&P 500
data1 = yf.download("KO", start="2025-01-01", end="2025-05-20")
print(data1['Close'].head())
dates1 = data1.index
prix1 = data1['Close']

# --- Graphique 1 : ESE.PA ---
plt.figure(figsize=(10, 6))
plt.plot(dates, prix, label='Prix Close de ESE.PA', color='blue')
plt.xlabel('Date')
plt.ylabel('Prix')
plt.title('Prix Close de l\'ETF ESE.PA')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Sauvegarder le graphique dans le dossier spécifique
plt.savefig(os.path.join(chemin_dossier, "graphique_ese.png"))
plt.show()

# --- Graphique 2 : S&P 500 ---
plt.figure(figsize=(10, 6))
plt.plot(dates1, prix1, label='Prix Close de l\'indice S&P 500', color='green')
plt.xlabel('Date')
plt.ylabel('Prix')
plt.title('Prix Close de l\'indice S&P 500')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Sauvegarder le graphique dans le dossier spécifique
plt.savefig(os.path.join(chemin_dossier, "graphique_sp500.png"))
plt.show()

# Sauvegarder les données dans des fichiers CSV
data.to_csv(os.path.join(chemin_dossier, "ese_data.csv"))
data1.to_csv(os.path.join(chemin_dossier, "sp500_data.csv"))


rr