"""Простое веб-приложение для практики CI/CD."""
import os

from flask import Flask, jsonify

from app.calculator import add, divide, multiply, subtract

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(message="Hello from CI/CD practice!", version=APP_VERSION)


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/calc/<op>/<int:a>/<int:b>")
def calc(op, a, b):
    operations = {"add": add, "sub": subtract, "mul": multiply, "div": divide}
    if op not in operations:
        return jsonify(error=f"unknown operation: {op}"), 400
    try:
        return jsonify(result=operations[op](a, b))
    except ZeroDivisionError:
        return jsonify(error="division by zero"), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
