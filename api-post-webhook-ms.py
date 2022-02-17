# CODE POST https://webexapis.com/v1/webhooks 

import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

API_POST_WEBHOOKS_URL = "https://webexapis.com/v1/webhooks"
access_token = 'YTVhNDgxNzYtNmE1OC00ZWYzLWJhYjItNzI3NzJiYTRjMTY4MTMzOWMyYWItNGNl_P0A1_82bf7487-2ebe-4fc9-a984-8a94fc400056'
WEBHOOK_URL = "https://webex-api.herokuapp.com/messages"

def api_post_webhook():

    token = ""
    err = ""

    try:
        response = requests.post(
            url= API_POST_WEBHOOKS_URL,
            headers={
                "Authorization": "Bearer {}".format(access_token),
                "Content-Type": "application/json"
            },
            data=json.dumps(
                {
                    
                    "name": "Webhook API Messages",
                    "targetUrl": WEBHOOK_URL,
                    "resource": "messages",
                    "event": "created"
                }
            ),
            verify=False
        )

        json_response = json.loads(response.content)
        #token = json_response['imdata'][0]['aaaLogin']['attributes']['token']
        #print(token)
        print(json_response)
        
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))

    except requests.exceptions.RequestException as err:
        print("HTTP Request failed")
        print(err)

    return token


print('======================== API-POST-WEBHOOK-MESSAGE ======================')

api_post_webhook()
