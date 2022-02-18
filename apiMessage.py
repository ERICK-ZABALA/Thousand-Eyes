
import requests
import json

from requests.exceptions import RequestException



def slackAlertSend (accessToken, alertThousandEyes):

    err = ""
   
    

    accessAuthorization = {
                            "Authorization": "Bearer {}".format (accessToken),
                            "Content-Type": "application/json"
                            }



    payload = json.dumps({"text": "{}".format (alertThousandEyes)}, indent= 4, separators= (',',':') )
    print (payload)
    # Displayed in Heroku Console

    route = "https://hooks.slack.com/services/" + accessToken

    try: 

        # Send Message to Slack
        response = requests.post(url=route, headers=accessAuthorization, data= payload) 
        # Message Status
        print (response.content) 
        

    except requests.exceptions.RequestException as err:
        print("HTTP Request failed")
        print(err)
    
    return alertThousandEyes
