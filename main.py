
from flask import json 
from flask import request
from flask import Flask 
from flask import render_template
import sys
import apiMessage
import credentials as crd

sys.path.append("/credentials")


accessToken = crd.AUTH_TOKEN

app = Flask(__name__)


@app.route('/')

def home():
    
 return render_template('index.html')

@app.route('/add_token',methods=['POST'])

def add_token():
    if request.method == 'POST':
        accessToken = request.form ['token']    
        print (accessToken)
        return 'Received'        


@app.route('/messages',methods=['POST'])

def messages():
    
               
        print("                                                                                     ")
        print("                                                                                     ")
        print("+++++++++++++++++++++++++++ T H O U S A N D +++ E Y E S +++++++++++++++++++++++++++++")
        print("                                                                                     ")
        print("-------------------------- ALERT_NOTIFICATION_TRIGGER -------------------------------")
        print("                                                                                     ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                                                                                     ")
        
        sampleAlert = json.dumps(request.json, indent = 4)
        print (sampleAlert)        
        apiMessage.slackAlertSend (accessToken, sampleAlert)

        return sampleAlert



if __name__ == '__main__':
    app.run(debug=True)

