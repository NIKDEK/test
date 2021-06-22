import requests, json, base64

auth_type = 'Basic'
creds = '{}:{}'.format('admin', 'S83H4448JD8')
auth_b64 = base64.b64decode(creds)

def get():
    header  = {'Authorization': '{} {}'.format(auth_type, auth_b64)}
    res = requests.get('http://127.0.0.1:5000/users', headers=header)
    return res.text

def post(jsn):
    content = {'Content-Type': 'application/json'}
    res = requests.post('http://127.0.0.1:5000/users', headers=content, data=json.dumps(jsn))
    return str(res.status_code)

inf = json.loads(get())

print(json.loads(post({'User':'tst'})))