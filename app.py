from flask import Flask
import os

app = Flask(__name__)


@app.route("/info")
def srtechopsinfo():
    return '<h1 style="color:violet;">Welcome </h1>'

@app.route("/contact")
def srtechopsmobilenumber():
    return  '<h1 style="color:blue;">Hi</h1>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
