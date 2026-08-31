import yfinance as yf
import pandas as pd
import requests
import os

# GitHub Secrets'tan token ve chat_id verilerini alıyoruz (Güvenlik için)
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# BİST hisseleri .IS uzantısı ile yazılmalıdır
hisseler = ["ASELS.IS", "THYAO.IS", "KCHOL.IS", "GARAN.IS"]

def send_telegram(mesaj):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": mesaj, "parse_mode": "Markdown"})

def check_heikin_ashi(symbol):
    # Son 5 günlük veriyi çek
    df = yf.download(symbol, period="5d", interval="1d", progress=False)
    
    if df.empty or len(df) < 2:
        return
    
    # Heikin Ashi Kapanış: (Open + High + Low + Close) / 4
    ha_close = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
    
    # Heikin Ashi Açılış: (Önceki HA_Open + Önceki HA_Close) / 2
    ha_open = [(df['Open'].iloc[0] + df['Close'].iloc[0]) / 2]
    for i in range(1, len(df)):
        ha_open.append((ha_open[i-1] + ha_close.iloc[i-1]) / 2)
    
    df['HA_Close'] = ha_close
    df['HA_Open'] = ha_open
    
    # Önceki mum yeşil (Close > Open), son mum kırmızı (Close < Open) ise
    onceki_yesil = df['HA_Close'].iloc[-2] > df['HA_Open'].iloc[-2]
    son_kirmizi = df['HA_Close'].iloc[-1] < df['HA_Open'].iloc[-1]
    
    if onceki_yesil and son_kirmizi:
        temiz_isim = symbol.replace('.IS', '')
        send_telegram(f"🚨 *{temiz_isim}* Heikin Ashi grafiğinde yeşilden **KIRMIZIYA** döndü! (Trend Değişimi)")

for hisse in hisseler:
    check_heikin_ashi(hisse)
