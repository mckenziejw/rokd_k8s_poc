import time
import os
from flask import Flask, request, render_template
import requests

template_path = os.environ.get('TEMPLATE_DIR')
cdn_service_url = os.environ.get('CDN_URL')

app = Flask(__name__, template_folder=template_path)

def get_quotes():
    quotes_url = "http://" + cdn_service_url + "/all"
    r = requests.get(quotes_url)
    quotes = r.json()
    return quotes

# def get_random_quote():
#     quotes_url = "http://" + cdn_service_url + "/random"
#     r = requests.get(quotes_url)
#     quote = r.json()
#     return quote

# @app.route('/random')
# def get_random():
#     data = {}
#     data['hostname'] = os.uname()[1]
#     cdn_data = get_random_quote()
#     data['cdn_hostname'] = cdn_data['hostname']
#     data['quote'] = cdn_data['quote']
#     return render_template("random.html", data=data)

@app.route('/')
def get_all():
    data = {}
    data['hostname'] = os.uname()[1]
    cdn_data = get_quotes()
    data['cdn_hostname'] = cdn_data['hostname']
    data['quotes'] = cdn_data['quotes']
    print(data)
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))
