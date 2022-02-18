from flask import json # lib format json
from flask import request # lib rest-api
from flask import Flask # server web application
import sys
import slackAlertSend

sys.path.append("/credentials")
import credentials as crd

accessToken = crd.AUTH_TOKEN
sampleAlert = ""

app = Flask(__name__)


@app.route('/')

def home():
    
        return "W E L C O M E      T H O U S A N D     E Y E S"

@app.route('/messages',methods=['POST'])

def messages():
    
        #sampleAlert = json.dumps(request.json)

        print("                                                                                     ")
        print("-------------------------------------------------------------------------------------")
        print("---------------          T-H-O-U-S-A-N-D   E-Y-E-S            -----------------------")
        print("-------------------------------------------------------------------------------------")
        print("*********************** ALERT_NOTIFICATION_TRIGGER **********************************")
        print("                                                                                     ")
  
        sampleAlert = {"alert": {"active": 1, "agents": [{"active": 1, "agentId": 20739, "agentName": "Guadalajara, Mexico (Trial)", "dateStart": "2022-02-17 23:43:00", "metricsAtEnd": "", "metricsAtStart": "Error: \"502 Bad Gateway\"", "permalink": "https://app.thousandeyes.com/alerts/list/?__a=415786&alertId=108381281&agentId=20739"}], "alertId": 108381281, "apiLinks": [{"href": "https://api.thousandeyes.com/v4/tests/2585349", "rel": "related"}, {"href": "https://api.thousandeyes.com/v4/web/http-server/2585349", "rel": "data"}], "dateStart": "2022-02-17 23:43:00", "dateStartZoned": "2022-02-17 23:43:00 EST", "permalink": "https://app.thousandeyes.com/alerts/list/?__a=415786&alertId=108381281", "ruleAid": 415786, "ruleExpression": "Error is present", "ruleId": 1927034, "ruleName": "Webhook Teyes", "testId": 2585349, "testLabels": [], "testName": "Web Server ", "testTargetsDescription": ["https://db42-192-226-134-67.ngrok.io"], "text": "Perdida de paquetes", "type": "HTTP Server", "violationCount": 1}, "eventId": "366215001-108381281", "eventType": "ALERT_NOTIFICATION_TRIGGER"}
  
        print (sampleAlert)

        slackAlertSend (accessToken, sampleAlert)
  
        return
        
        


if __name__ == '__main__':
    app.run(debug=True)


