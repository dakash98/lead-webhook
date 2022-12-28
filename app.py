from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Webhook Sample!'

@app.route('/webhook', methods=['POST'])
def post_webhook():
    if request.method == 'POST':
        print("received data: ", request.json)
        return 'success', 200
    else:
        print("not allowed")
        abort(400)


@app.route('/webhook-get', methods=['GET', 'POST'])
def get_webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge'), 200
    else:
        return request.json
    