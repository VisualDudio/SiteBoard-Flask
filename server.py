from flask import Flask, render_template
from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET KEY'] = 'mysecret'
app.debug = True
socketio = SocketIO(app)

@socketio.on('mouse')
def handleMouse (data):
    socketio.emit('mouse', data, include_self=True)

@socketio.on('eraser-mouse')
def handleEraserMouse (data):
    socketio.emit('eraser-mouse', data, include_self=True)

@socketio.on('disengage')
def disengage():
    socketio.emit('disengage', include_self=True)

@socketio.on('chat-message')
def handleChat (data):
    socketio.emit('chat-message', data, include_self=False)

@socketio.on('color')
def handleColor(color):
    socketio.emit('color', color, include_self=True) 

@socketio.on('eraser')
def handleEraser():
    socketio.emit('eraser', include_self=True) 

@socketio.on('size')
def handleSize(size):
    socketio.emit('size', size, include_self=True)

@socketio.on('clear')
def handleClear():
    socketio.emit('clear', include_self=True) 

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app)