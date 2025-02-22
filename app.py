# from flask import Flask, request, abort
# from flask_mail import Mail, Message

# app = Flask(__name__)
# mail = Mail(app) # instantiate the mail class
   
# # configuration of mail
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'akash.deep@sait.ac.in'
# app.config['MAIL_PASSWORD'] = 'nutanakash'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)


# @app.route('/webhook-get', methods=['GET', 'POST'])
# def get_webhook():
#     if request.method == 'GET':
#         return request.args.get('hub.challenge'), 200
#     else:
#         print("json is : ", request.json["entry"][0]["changes"][0]["value"]["leadgen_id"])
#         send_email(request.json["entry"][0]["changes"][0]["value"]["leadgen_id"])
#         return request.json
    

# def send_email(lead_id):
#     msg = Message(
#                 'Hello',
#                 sender ='akash.deep@sait.ac.in',
#                 recipients = ['akash.deep@essentia.dev']
#                )
#     msg.body = f'Hello Akash, You have received an email with lead id {lead_id}'
#     mail.send(msg)
#     return "Email Sent"


from flask import Flask, request, jsonify
from decouple import config

app = Flask(__name__)

VERIFY_TOKEN = config("VERIFY_TOKEN")  # Set this securely

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Facebook verification
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("Webhook verified successfully!")
            return challenge, 200
        else:
            return "Verification token mismatch", 403

    elif request.method == "POST":
        # Receiving the lead
        data = request.json
        print("Received lead data ------------------------:", data)

        # Process lead data (e.g., save to DB, send email, etc.)
        return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
