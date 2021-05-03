# Built-in library
import json
# from uuid import uuid4
# Third-party library
# import asyncio
# from aiohttp import web
# from aiopg.sa import create_engine


# examples/server_simple.py
from aiohttp import web

async def get_home(request):
    return web.

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle),
                web.get('/home', get_home),
                ])

if __name__ == '__main__':
    web.run_app(app)