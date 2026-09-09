# BIST Heikin Ashi Telegram Bot

BIST hisselerinin son Heikin Ashi mumunu kontrol eder ve mum kirmizi kapandiysa Telegram bildirimi gonderir.

> Bu proje yatirim tavsiyesi degildir. Veriler `yfinance` uzerinden alinir ve veri gecikmesi veya API kesintisi olabilir.

## Takip edilen hisseler

Hisseler [symbols.txt](symbols.txt) dosyasinda, her satira bir Yahoo Finance sembolu gelecek sekilde tanimlanir. BIST sembollerinde `.IS` uzantisi kullanilir.

```text
ASELS.IS
TUPRS.IS
ASTOR.IS
BIMAS.IS
KTLEV.IS
```

## GitHub Actions kurulumu

1. Repoyu GitHub'da public veya private olarak olusturun.
2. Repository Settings > Secrets and variables > Actions yolundan su iki repository secret'i ekleyin:
   - `TELEGRAM_TOKEN`: BotFather token'i
   - `TELEGRAM_CHAT_ID`: Bildirim gonderilecek sohbet ID'si
3. Actions sekmesinden workflow'u manuel calistirarak kurulumu test edin.

Workflow hafta ici her gun `15:20 UTC` saatinde, yani Istanbul saatiyle yaklasik `18:20`'de calisir. GitHub Actions zamanlamalari birkac dakika gecikebilir.

## Yerelde calistirma

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
$env:TELEGRAM_TOKEN="BOT_TOKENINIZ"
$env:TELEGRAM_CHAT_ID="CHAT_IDINIZ"
.\.venv\Scripts\python bot.py
```

Telegram token veya chat ID'sini kaynak koda, `symbols.txt` dosyasina, issue'lara ya da commit mesajlarina yazmayin. Token sizarsa BotFather'dan yenileyin ve eski token'i iptal edin.

## Lisans

Bu depo icin henuz bir lisans secilmemistir. Kodu public olarak paylasmadan once uygun bir lisans ekleyin veya tum haklari sakli tutun.
