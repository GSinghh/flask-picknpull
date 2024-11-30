from .extensions import socketio
from flask_socketio import emit
import sys

@socketio.on('connect')
def handle_connect():
    print('Client Connected Succesfully')
    
    
@socketio.on('test_event')
def handle_test_event(data):
    print(f"Received test event with data: {data}")
    socketio.emit('response', {'Test Data': 'Sending data to the client from the server'})
