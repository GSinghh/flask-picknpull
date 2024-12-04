from .extensions import socketio
from flask_socketio import emit 
import psutil
from flask import request
    
@socketio.on('test_event')
def handle_test_event(data):
    print(f"Received test event with data: {data}")
    socketio.emit('response', {'Test Data': 'Sending data to the client from the server'})

@socketio.on('connect')
def handle_connect():
    transport = request.args.get('transport', '')
    if transport == 'polling':
        print("Initial Polling Request Before WebSocket Upgrade")

@socketio.on('share_data')
def share_data_with_client():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu_freq = psutil.cpu_freq()
        load_avg = psutil.getloadavg()
        socketio.emit('response',{"cpu_usage": cpu_usage,
                "cpu_freq": cpu_freq,
                "avg_load": load_avg}) 