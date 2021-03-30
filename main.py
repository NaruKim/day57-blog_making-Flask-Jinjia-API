from flask import Flask, render_template
import requests

URL = "https://api.npoint.io/5abcca6f4e39b4955965"

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(URL)
    return render_template("index.html", data=response.json())

@app.route('/post/<n>')
def get_post(n):
    response = requests.get(URL)
    post = response.json()[int(n)-1]['body']
    return post

if __name__ == "__main__":
    app.run(debug=True)
