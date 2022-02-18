from lib2to3.pgen2 import token
import requests
import json
import sys

sys.path.append("/index")
import index as alert

alertThousandEyes = json.dumps((alert.sampleAlert), indent=4)
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# credentials of Slack Token: T034565CZG8/B033JS4NC2Z/l9MbWBB5rJhstw7ly1muZdSK

#accessToken = token

def slackAlertSend (accessToken, alertThousandEyes):

    accessAuthorization = {
                            "Authorization": "Bearer {}".format (accessToken),
                            "Content-Type": "application/json"
                            }

    #payload = json.dumps ({ "text":"Hola Thousand Eyes!!!" })
    # la data se debe colocar en formato json por eso se usa el metodo json.dumps

    payload = json.dumps({"text": "{}".format (alertThousandEyes)})
    route = "https://hooks.slack.com/services/" + accessToken

    print (alertThousandEyes) # coloca en formato Json la alerta
    response = requests.post(url=route, headers=accessAuthorization, data= payload) # Envia el mensaje a Slack
    print (response.content) # Message Status
    return alertThousandEyes
