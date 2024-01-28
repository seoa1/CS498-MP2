from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def seed_get():
    return socket.gethostname()

@app.route('/', methods=['POST'])
def seed_post():
    subprocess.Popen(['python3', './stress_cpu.py'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
