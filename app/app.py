from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "application": "complete-devops-automation",
            "status": "running",
            "version": "1.0.4",
            "message": os.getenv("APP_MESSAGE", "default message"),
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)