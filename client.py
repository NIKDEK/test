import requests, json, base64

auth_type = 'Basic'
with open('apipass.json', 'r') as api_info:
    user_info = json.loads(api_info.read())["User"][0]
    print(user_info)
    creds = '{}:{}'.format(user_info[0], user_info[1])
    print(creds)
    api_info.close()
auth_b64 = base64.b64decode(creds)

def err_handler(res):
    return 'API call error: {}'.format(res)

def get():
    header  = {'Authorization': '{} {}'.format(auth_type, auth_b64)}
    res = requests.get('http://127.0.0.1:5000/users', headers=header)
    if res.status_code != 200:
        raise Exception(err_handler(res))
    return res.text

def post(jsn):
    content = {'Content-Type': 'application/json'}
    res = requests.post('http://127.0.0.1:5000/users', headers=content, data=json.dumps(jsn))
    if res.status_code != 200:
        raise Exception(err_handler(res))
    return str(res.status_code)


inf = json.loads(get())
print(json.loads(post({'User':'tst'})))


# git stash
# git stash pop