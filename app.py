from flask import Flask, render_template
from config import url, key
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    result = requests.get(f"{url}?api_key={key}&hd=true").json()
    hdurl =  result['hdurl']
    title = result['title']
    explanation = result['explanation']
    return render_template('template.html', hdurl = hdurl, title=title, explanation = explanation)

app.run()
