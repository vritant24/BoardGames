import socketio
from aiohttp import web

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)

@sio.on('my message')
def message(sid, data):
    print('message ', data)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    web.run_app(app, port=5000)