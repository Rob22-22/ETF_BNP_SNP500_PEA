import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

def calcul_rsi(prix, periode=14):
    delta = prix.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periode).mean()
    perte = (-delta.where(delta < 0, 0)).rolling(window=periode).mean()
    rs = gain / perte
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calcul_macd(prix, courte=12, longue=26, signal=9):
    ema_courte = prix.ewm(span=courte, adjust=False).mean()
    ema_longue = prix.ewm(span=longue, adjust=False).mean()
    macd = ema_courte - ema_longue
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def calcul_moyenne_mobile(prix, periode):
    return prix.rolling(window=periode).mean()

def calcul_bollinger(prix, periode=20, nb_std=2):
    sma = calcul_moyenne_mobile(prix, periode)
    rolling_std = prix.rolling(window=periode).std()
    bande_sup = sma + (rolling_std * nb_std)
    bande_inf = sma - (rolling_std * nb_std)
    return bande_sup, bande_inf

def calcul_stochastique(high, low, close, k_period=14, d_period=3):
    lowest_low = low.rolling(window=k_period).min()
    highest_high = high.rolling(window=k_period).max()
    percent_k = 100 * ((close - lowest_low) / (highest_high - lowest_low))
    percent_d = percent_k.rolling(window=d_period).mean()
    return percent_k, percent_d

def calcul_adx(high, low, close, periode=14):
    plus_dm = high.diff()
    moins_dm = low.diff().abs()

    plus_dm = np.where((plus_dm > 0) & (plus_dm > moins_dm), plus_dm, 0.0)
    moins_dm = np.where((moins_dm > 0) & (moins_dm > plus_dm), moins_dm, 0.0)

    plus_dm = pd.Series(plus_dm.flatten(), index=high.index)
    moins_dm = pd.Series(moins_dm.flatten(), index=low.index)

    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    atr = tr.rolling(window=periode).mean()

    plus_di = 100 * (plus_dm.rolling(window=periode).sum() / atr)
    moins_di = 100 * (moins_dm.rolling(window=periode).sum() / atr)

    dx = (abs(plus_di - moins_di) / (plus_di + moins_di)) * 100
    adx = dx.rolling(window=periode).mean()

    return adx, plus_di, moins_di

# === Paramètres ===
ticker = "ESE.PA"
heure_debut = "09:00"
heure_fin = "17:30"

periode_1d_1m = "1d"
intervalle_1d_1m = "1m"

periode_5d_2m = "5d"
intervalle_5d_2m = "2m"

periode_1mo_5m = "1mo"
intervalle_1mo_5m = "5m"

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

chemin_dossier_csv = "C:\\Users\\robin.guichon\\Documents\\Test\\CSV"
chemin_dossier_graphe = "C:\\Users\\robin.guichon\\Documents\\Test\\Graph"

def tracer_periode(periode, intervalle):
    print(f"Téléchargement des données pour {periode} / {intervalle} ...")
    data = yf.download(ticker, period=periode, interval=intervalle)

    if data.index.tz is None:
        data.index = data.index.tz_localize('UTC').tz_convert('Europe/Paris')
    else:
        data.index = data.index.tz_convert('Europe/Paris')

    if intervalle in ['1m', '2m', '5m', '15m', '30m', '60m', '1h', '90m', '120m']:
        data = data.between_time(heure_debut, heure_fin)

    data.reset_index(inplace=True)

    x = np.arange(len(data))
    y = data['Close'].to_numpy().ravel()

    if 'Datetime' in data.columns:
        labels = data['Datetime'].dt.strftime("%d/%m %H:%M")
    elif 'Date' in data.columns:
        labels = data['Date'].dt.strftime("%d/%m/%Y")
    else:
        labels = x.astype(str)

    close = data['Close']
    high = data['High']
    low = data['Low']

    data['RSI'] = calcul_rsi(close)
    data['MACD'], data['MACD_signal'] = calcul_macd(close)
    data['SMA_20'] = calcul_moyenne_mobile(close, 20)
    data['SMA_50'] = calcul_moyenne_mobile(close, 50)
    data['Bollinger_sup'], data['Bollinger_inf'] = calcul_bollinger(close)
    data['Stoch_K'], data['Stoch_D'] = calcul_stochastique(high, low, close)
    data['ADX'], data['Plus_DI'], data['Minus_DI'] = calcul_adx(high, low, close)

    fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(
        6, 1, figsize=(48, 26), sharex=True,
        gridspec_kw={'height_ratios': [3, 1, 1, 1, 1, 1]}
    )

    ax1.plot(x, y, label=ticker, color='black')
    ax1.fill_between(x, y, color='black', alpha=0.3)
    ax1.plot(x, data['SMA_20'], label='SMA 20', color='blue', linewidth=1.5)
    ax1.plot(x, data['SMA_50'], label='SMA 50', color='red', linewidth=1.5)
    ax1.plot(x, data['Bollinger_sup'], label='Bollinger Supérieure', color='green', linestyle='--')
    ax1.plot(x, data['Bollinger_inf'], label='Bollinger Inférieure', color='green', linestyle='--')
    ax1.set_ylabel("Prix (€)")
    ax1.set_title(f"{periode}/{intervalle} avec RSI, MACD, Moyennes mobiles, Bollinger, Stochastique, ADX et Volume")
    ax1.legend()
    ax1.grid(axis='y')

    min_y, max_y = y.min(), y.max()
    margin = 0.1 * (max_y - min_y)
    ax1.set_ylim(min_y - margin, max_y + margin)

    ax2.plot(x, data['RSI'], label='RSI (14)', color='blue')
    ax2.axhline(70, color='red', linestyle='--')
    ax2.axhline(30, color='green', linestyle='--')
    ax2.set_ylabel("RSI")
    ax2.legend()
    ax2.grid()

    ax3.plot(x, data['MACD'], label='MACD', color='purple')
    ax3.plot(x, data['MACD_signal'], label='Signal', color='orange')
    ax3.set_ylabel("MACD")
    ax3.legend()
    ax3.grid()

    if 'Volume' in data.columns:
        volumes = data['Volume'].fillna(0).astype(float).to_numpy().flatten()
        if len(volumes) == len(x):
            ax4.bar(x, volumes, color='grey', label='Volume')
            ax4.set_ylabel('Volume')
            ax4.legend()
            ax4.grid()
        else:
            ax4.axis('off')
    else:
        ax4.axis('off')

    ax5.plot(x, data['Stoch_K'], label='%K', color='blue')
    ax5.plot(x, data['Stoch_D'], label='%D', color='red')
    ax5.axhline(80, color='red', linestyle='--')
    ax5.axhline(20, color='green', linestyle='--')
    ax5.set_ylabel('Stochastique')
    ax5.legend()
    ax5.grid()

    ax6.plot(x, data['ADX'], label='ADX', color='purple')
    ax6.plot(x, data['Plus_DI'], label='+DI', color='green', linestyle=':')
    ax6.plot(x, data['Minus_DI'], label='-DI', color='red', linestyle=':')
    ax6.set_ylabel('ADX et DI')
    ax6.legend()
    ax6.grid()

    step = max(len(x) // 10, 1)
    plt.xticks(ticks=x[::step], labels=labels[::step], rotation=45)
    plt.tight_layout()

    data.to_csv(os.path.join(chemin_dossier_csv, f"{periode}_{intervalle}_{ticker.replace('.', '_')}.csv"), index=False)
    plt.savefig(os.path.join(chemin_dossier_graphe, f"{periode}_{intervalle}_{ticker.replace('.', '_')}_graph.png"))
    plt.close()

# Appels
tracer_periode(periode_1d_1m, intervalle_1d_1m)
tracer_periode(periode_5d_2m, intervalle_5d_2m)
tracer_periode(periode_1mo_5m, intervalle_1mo_5m)
tracer_periode(periode_3mo_1h, intervalle_3mo_1h)
tracer_periode(periode_6mo_1h, intervalle_6mo_1h)
tracer_periode(periode_1y_1h, intervalle_1y_1h)
tracer_periode(periode_5y_1d, intervalle_5y_1d)
tracer_periode(periode_10y_1d, intervalle_10y_1d)
