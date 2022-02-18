from flask import json # lib format json
from flask import request # lib rest-api
from flask import Flask # server web application
import sys
import slackAlertSend

sys.path.append("/credentials")
import credentials as crd

accessToke = crd.AUTH_TOKEN
sampleAlert = ""

app = Flask(__name__)


@app.route('/')

def home():
    
 return "WELCOME THOUSAND EYES"


@app.route('/messages',methods=['POST'])

def messages():
    
        sampleAlert = json.dumps(request.json)

        print("                                                                                     ")
        print("-------------------------------------------------------------------------------------")
        print("---------------          T-H-O-U-S-A-N-D   E-Y-E-S            -----------------------")
        print("-------------------------------------------------------------------------------------")
        print("*********************** ALERT_NOTIFICATION_TRIGGER **********************************")
        print("                                                                                     ")
          
        #print (sampleAlert)
       
        return sampleAlert


a = json.dumps(messages(), indent=4)
slackAlertSend.slackAlertSend (accessToke, a)
    
        


if __name__ == '__main__':
    app.run(debug=True)


