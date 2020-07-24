import time
import os
from flask import Flask, request, render_template
import requests

template_path = os.environ.get('TEMPLATE_DIR')
backend_service_url = os.environ.get('BACKEND_URL')

app = Flask(__name__, template_folder=template_path)

def get_lorem():
    lorem_url = "http://" + backend_service_url + "/lorem"
    r = requests.get(lorem_url)
    lorem = r.json()
    return lorem

@app.route('/')
def get_index():
    data = {}
    data['hostname'] = os.uname()[1]
    backend_data = get_lorem()
    data['backend_hostname'] = backend_data['hostname']
    data['lorem'] = backend_data['lorem']
    print(data)
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))
