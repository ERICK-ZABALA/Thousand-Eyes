from flask import json 
from flask import request
from flask import Flask 
import sys
import slackAlertSend
import credentials as crd

sys.path.append("/credentials")


accessToken = crd.AUTH_TOKEN

app = Flask(__name__)


@app.route('/')

def home():
    
 return "WELCOME THOUSAND EYES"


@app.route('/messages',methods=['POST'])

def messages():
    
               
        print("                                                                                     ")
        print("-------------------------------------------------------------------------------------")
        print("                         T H O U S A N D   E Y E S                                   ")
        print("-------------------------------------------------------------------------------------")
        print("*********************** ALERT_NOTIFICATION_TRIGGER **********************************")
        print("                                                                                     ")
        
        sampleAlert = json.dumps(request.json)
                
        slackAlertSend.slackAlertSend (accessToken, sampleAlert)

        return sampleAlert



if __name__ == '__main__':
    app.run(debug=True)


