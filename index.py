from flask import json # lib format json
from flask import request # lib rest-api
from flask import Flask # server web application

app = Flask(__name__)


@app.route('/')

def home():
    
        return "W E L C O M E      T H O U S A N D     E Y E S"

@app.route('/messages',methods=['POST'])

def messages():
    
        sampleAlert = json.dumps(request.json)

        print("                                                                                     ")
        print("-------------------------------------------------------------------------------------")
        print("---------------          T-H-O-U-S-A-N-D   E-Y-E-S            -----------------------")
        print("-------------------------------------------------------------------------------------")
        print("*********************** ALERT_NOTIFICATION_TRIGGER **********************************")
        print("                                                                                     ")

        print (sampleAlert)
        
        return sampleAlert

  

if __name__ == '__main__':
    app.run(debug=True)


