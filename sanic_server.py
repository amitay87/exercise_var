from json import loads as json_loads

from sanic import Sanic
from sanic.response import json
from sanic_jwt import Initialize

from users import users

app = Sanic("My Hello, world app")


@app.route('/')
async def test(request):
    return json({'hello': 'world'})


@app.route('/normalize', methods=['POST'])
def normalize(request):
    body = json_loads(request.body)
    print(body)
    normalized_json = [{item['name']: item['strVal']} for item in body]
    return json(normalized_json)


async def authenticate(request):
    print(f"AAA request: {request}")

    print(request.body)
    print(json_loads(request.body))
    credentials = json_loads(request.body)
    if credentials['username'] in users:
        if users[credentials['username']]['password'] == credentials['password']:
            return dict(user_id='some_id')
    else:
        raise Exception('authentication failed')



if __name__ == '__main__':
    Initialize(app, authenticate=authenticate)
    app.run()