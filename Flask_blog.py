from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == "__main__":
    app.run(debug=True)