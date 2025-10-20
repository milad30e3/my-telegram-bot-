from flask import Flask
import os

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "✅ Bot is alive!"

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
