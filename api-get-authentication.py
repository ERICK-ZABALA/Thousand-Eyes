import json
import requests
from requests import status_codes
from requests.packages.urllib3.exceptions import InsecureRequestWarning

APIC_URL = "https://devasc-aci-1.cisco.com"

def apic_login():
    """ Login to APIC"""

    token = ""
    err = ""

    try:
        response = requests.post (
            url=APIC_URL+"/api/aaaLogin.json",
            headers={"Content-Type":"application/json; charset=utf-8",},
            data=json.dumps(
                {
                    "aaaUser": {
                        "attributes": {
                            "name": "devnetuser",
                            "pwd": "CardBoardGreen12!"
                        }
                    }
                }
            ),
            verify=False
        )

        json_response = json.loads(response.content)
        token = json_response['imdata'][0]['aaaLogin']['attributes']['token']
        print(token)

        print('Response HTTP Status Code: {status_code}'.format(
               status_code=response.status_code))
    
    except requests.exceptions.RequestException as err:
        print("HTTP Request failed")
        print(err)

    return token

print('=========================APIC LOGIN=======================')
apic_login()