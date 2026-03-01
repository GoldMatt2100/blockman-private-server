from flask import Flask
import os

app = Flask(__name__)

# Root route for testing
@app.route("/")
def home():
    return "Blockman Go Private Server Running"

# Example create account route
@app.route("/create_account")
def create_account():
    return "Create Account Endpoint Active"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
