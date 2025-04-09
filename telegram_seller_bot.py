
from flask import Flask, request
import requests
import os

app = Flask(__name__)
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")  # Your Telegram ID

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text.lower() == "/start":
            send_message(chat_id, "Selamat datang! Pilih produk:
1. Akun Gmail
2. Token Listrik
3. Telegram Premium")
        elif text.lower() == "1":
            send_message(chat_id, "Harga Akun Gmail: Rp10.000
Silakan transfer dan kirim bukti.")
        elif text.lower() == "2":
            send_message(chat_id, "Token Listrik tersedia mulai Rp20.000
Silakan transfer dan kirim bukti.")
        elif text.lower() == "3":
            send_message(chat_id, "Telegram Premium: Rp50.000
Silakan transfer dan kirim bukti.")
        else:
            send_message(chat_id, "Pesan diterima. Admin akan segera merespon.")
            send_message(ADMIN_CHAT_ID, f"Pesan dari {chat_id}: {text}")
    return "ok"

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(debug=True)
