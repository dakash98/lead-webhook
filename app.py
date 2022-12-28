from flask import Flask, request, abort
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'akash.deep@sait.ac.in'
app.config['MAIL_PASSWORD'] = 'nutanakash'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/webhook-get', methods=['GET', 'POST'])
def get_webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge'), 200
    else:
        print("json is : ", request.json["entry"][0]["changes"][0]["value"]["leadgen_id"])
        send_email(request.json["entry"][0]["changes"][0]["value"]["leadgen_id"])
        return request.json
    

def send_email(lead_id):
    msg = Message(
                'Hello',
                sender ='akash.deep@sait.ac.in',
                recipients = ['akash.deep@essentia.dev']
               )
    msg.body = f'Hello Akash, You have received an email with lead id {lead_id}'
    mail.send(msg)
    return "Email Sent"