from flask import json # lib format json
from flask import request # lib rest-api
from flask import Flask # server web application

app = Flask(__name__)


@app.route('/')

def home():
    
        return "Webhook App"

@app.route('/messages',methods=['POST'])

def messages():
    
        my_info = json.dumps(request.json)
        print("********** FORMAT JSON POST REQUEST MESSAGE *************")
        print (my_info)
        return my_info

@app.route('/rooms',methods=['POST'])

def rooms():
    
        my_info = json.dumps(request.json)
        print("********** FORMAT JSON POST REQUEST ROOMS *************")
        print (my_info)
        return my_info

if __name__ == '__main__':
    app.run(debug=True)


