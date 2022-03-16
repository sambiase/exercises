from aiohttp import web
import json


# GET API FUNCTION
async def response(request):
    responseObj = {'status': 'success'}
    return web.Response(text=json.dumps(responseObj), status=200)


# POST API FUNCTION
async def post_new_user(request):
    try:
        user = request.query['name']
        responseObj = {'status': 'success', 'message': 'user created'}
        print(f'Username: {user}')
        return web.Response(text=json.dumps(responseObj), status=200)

    except Exception as e:
        responseObj = {'status': 'not created', 'message': {e}}
        return web.Response(text=json.dumps(responseObj), status=500)


app = web.Application()
app.router.add_get('/', response)
app.router.add_post('/user', post_new_user)

web.run_app(app)
