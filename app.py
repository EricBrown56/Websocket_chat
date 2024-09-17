from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

message_db = []
socketio = SocketIO()

socketio.init_app(app, cors_allowed_origin = '*')# set cors to allow all origins with *


@socketio.on('connect') #this wrapper is responsible for triggering the following function based on the specified event
def handle_connect():
    print('Client Connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client Disconnected')

@socketio.on('message')#when a message comes through, create an empty list that gets appended
def handle_message(message): # When listening for a message events, takes in a message as an argument
    print(f"Message: {message}")
    socketio.emit('message', message) #.emit() method broadcasts a special message to everyone connected
    message_db.append(message)


@app.route('/')
def home():
    return render_template('base.html')


if __name__ == '__main__':
    app.debug = True
    socketio.run(app)


