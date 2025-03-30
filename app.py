from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['Get'])
def home():
    return "Flask App3"

if __name__ == "__main__":
    app.run()