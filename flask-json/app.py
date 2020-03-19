from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    content = request.json
    print(content)
    for i in content['password']:
        print(i)
    return jsonify(content)

app.run(host='0.0.0.0', port=5000, debug=True)