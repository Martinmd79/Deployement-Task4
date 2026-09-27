from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from Docker</h1>
    <p>SWE40006 Task 4.2</p>
    <p>The Python Flask container is running successfully.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)