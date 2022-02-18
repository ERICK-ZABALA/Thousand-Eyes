from flask import json # lib format json
from flask import request # lib rest-api
from flask import Flask # server web application
import sys
import slackAlertSend

sys.path.append("/credentials")
import credentials as crd

accessToken = crd.AUTH_TOKEN

app = Flask(__name__)


@app.route('/')

def home():
    
 return "WELCOME THOUSAND EYES"


@app.route('/messages',methods=['POST'])

def messages():
    
               
        print("                                                                                     ")
        print("-------------------------------------------------------------------------------------")
        print("---------------          T-H-O-U-S-A-N-D   E-Y-E-S            -----------------------")
        print("-------------------------------------------------------------------------------------")
        print("*********************** ALERT_NOTIFICATION_TRIGGER **********************************")
        print("                                                                                     ")
        sampleAlert = json.dumps(request.json)
        #print (sampleAlert)
        
        return sampleAlert


a = json.dumps(messages(), indent=4)
slackAlertSend.slackAlertSend (accessToken, a)
        
        


if __name__ == '__main__':
    app.run(debug=True)


