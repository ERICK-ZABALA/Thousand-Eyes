
import requests
import json

from requests.exceptions import RequestException



def slackAlertSend (accessToken, alertThousandEyes):

    err = ""
    #alertThousandEyes = json.dumps((alertThousandEyes), indent=4)
    

    accessAuthorization = {
                            "Authorization": "Bearer {}".format (accessToken),
                            "Content-Type": "application/json"
                            }

    #payload = json.dumps ({ "text":"Hola Thousand Eyes!!!" })
    # la data se debe colocar en formato json por eso se usa el metodo json.dumps

    payload = json.dumps({"text": "{}".format (alertThousandEyes)})
    route = "https://hooks.slack.com/services/" + accessToken

    try: 

       # print (alertThousandEyes) # coloca en formato Json la alerta
        response = requests.post(url=route, headers=accessAuthorization, data= payload) # Envia el mensaje a Slack
        print (response.content) # Message Status
        

    except requests.exceptions.RequestException as err:
        print("HTTP Request failed")
        print(err)
    
    return alertThousandEyes
