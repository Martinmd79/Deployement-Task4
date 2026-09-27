import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    app_env = os.getenv("APP_ENV", "Unknown")
    app_version = os.getenv("APP_VERSION", "Unknown")

    return f"""
    <html>
        <head>
            <title>SWE40006 Deployment Status</title>
        </head>
        <body>
            <h1>Deployment Status Dashboard</h1>
            <p><strong>Application:</strong> SWE40006 Docker Demo</p>
            <p><strong>Status:</strong> Running</p>
            <p><strong>Environment:</strong> {app_env}</p>
            <p><strong>Version:</strong> {app_version}</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)