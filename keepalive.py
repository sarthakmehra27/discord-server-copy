# keepalive.py
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/ping')
def ping():
    return "pong", 200

def run():
    port = int(os.environ.get("PORT", 8080))  # Use env port or fallback to 8080
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
