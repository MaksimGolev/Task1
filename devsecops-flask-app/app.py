from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to our vulnerable app!"

# Уязвимость: доступ к переменным окружения
@app.route('/debug')
def debug():
    return str(dict(os.environ))

# Уязвимость: команда из запроса (Remote Code Execution)
@app.route('/run')
def run():
    cmd = request.args.get('cmd')
    return os.popen(cmd).read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
