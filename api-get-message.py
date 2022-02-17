
import json
import requests
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

MESSAGE_ID = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvOWRhMTNlODAtODYzZC0xMWVjLTgxMmUtNTVjM2U3OTBmNGRm'
API_GET_MESSAGE_URL = "https://webexapis.com/v1/messages/" + MESSAGE_ID

def api_get_message():

    access_token = 'YmQ3ZTY3ZjUtMjVhZC00YWFhLWJlYTEtZDljOTc1ZGNlMGMwZmMzNTVlYmItYmYx_P0A1_82bf7487-2ebe-4fc9-a984-8a94fc400056'
    token = ""
    err = ""

    try:
        response = requests.get(
            url = API_GET_MESSAGE_URL,
            headers={
                "Authorization": "Bearer {}".format(access_token),
                "Content-Type": "application/json"
            },
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


print('======================== API GET MESSAGE =======================')
api_get_message()
