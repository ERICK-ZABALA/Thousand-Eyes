from textwrap import indent
from flask import json 
from flask import request
from flask import Flask 
import sys
import apiMessage
import credentials as crd

sys.path.append("/credentials")


accessToken = crd.AUTH_TOKEN

app = Flask(__name__)


@app.route('/')

def home():
    
 return "W E L C O M E ----- T H O U S A N D ---- E Y E S"


@app.route('/messages',methods=['POST'])

def messages():
    
               
        print("                                                                                     ")
        print("-------------------------------------------------------------------------------------")
        print("                                                                                     ")
        print("+++++++++++++++++++++++++++ T H O U S A N D +++ E Y E S +++++++++++++++++++++++++++++")
        print("                                                                                     ")
        print("-------------------------------------------------------------------------------------")
        print("                                                                                     ")
        print("-------------------------- ALERT_NOTIFICATION_TRIGGER -------------------------------")
        print("                                                                                     ")
        
        sampleAlert = json.dumps(request.json, indent = 4)
        print (sampleAlert)        
        apiMessage.slackAlertSend (accessToken, sampleAlert)

        return sampleAlert



if __name__ == '__main__':
    app.run(debug=True)


