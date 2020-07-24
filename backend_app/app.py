import time
import os
import json
from flask import Flask, request, jsonify
import random
import lorem

app = Flask(__name__)

@app.route('/lorem')
def get_all():
    text = lorem.paragraph()
    data = {}
    data['lorem'] = text
    data['hostname'] = os.uname()[1]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5050"))
