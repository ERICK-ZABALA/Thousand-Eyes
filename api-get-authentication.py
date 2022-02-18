import requests
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
import json
import sys

### Cisco DNA Center URL and Authentication Credentials
# In a 'real' application, this information might be in a 'config.py' file
# to keep authentication and target information out of the primary
# https://api.thousandeyes.com/v6/status -u webex.code@gmail.com:5ij5239r4oowevck38tlj2tcl7fh06d3


# Authentication to DevAsc DNA Center

username = "webex.code@gmail.com"
password = "C1sc0123!"

# define  Authentication method

def get_X_auth_token(username,password):
    """
    Authenticate to remote Cisco DNA Center
    
    Parameters
    ----------
    dnacip (str): dnac routable DNS address or ip
    username (str): dnac user name
    password (str): password

    Return:
    ----------
    str:dnac access token
    """
    # Supress credential warning for this exercise
    requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

    # Authentication API full URI

    post_uri = "https://api.thousandeyes.com/v6/status"

    print ("\nAuthenticate: POST %s"%(post_uri))

    try:
        #verify - set to False to tell requests to NOT verify server's TLS certificate
        # In production code this should be left to default to 'True'
        r = requests.post(post_uri, auth=(username, password), verify=False)
        return r.json()["Token"]
    except:
        #Something wrong, cannot get access token
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()

# Authenticate to the Cisco Dna Center
# and obtain an authentication token

token = get_X_auth_token(username,password)
print("return Authentication Token: ", (token))

