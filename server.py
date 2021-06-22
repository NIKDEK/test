from flask import Flask, request

import json

app = Flask(__name__)

app.secret_key = b"_93JE93JR9R49RTI"

info = {
    'Users':['TEST1']
}

@app.route('/users', methods=['GET', 'POST'])
def users():
    print(request.headers)
    if request.method == 'GET':
        return json.dumps(info)
    elif request.method == 'POST':
        print(request.get_data())
        return 'POSTED'