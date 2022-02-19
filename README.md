
![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/thousandEyesLogo.jpg)

# ThousandEyes

## OVERVIEW

This example is an integration between Thousand Eyes and Slack using Python. Thousand Eyes sends alert notifications via our webhook service and those notifications are received in the Web Server API deployed as an application in the cloud of Heroku. The Web Server API is hosted in the Heroku Cloud send the notifications to Slack device using an incoming webhook of Slack that is a simple way to post messages from external sources (third parties).

![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/flowAlert.png?raw=true)

## PREREQUISITES

* Create a trial account at https://www.thousandeyes.com/signup/. Write “Cisco” in the company field.
* Configure a Test (Web Server TD Bank) with an alert that will trigger and clear alerts for your testing in Thousand Eyes.
* Create a Slack instance https://slack.com/get-started#/createnew.
* Create a Heroku account at https://id.heroku.com/login.
* Deploy a Web Server TD Bank in your PC to make testing with Thousand Eyes, you can use the folder:webServerTdBank and the app:babywebssl.rar and ngrok (https://ngrok.com/download) to publish the service to internet.

![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/webServerTdBank.png?raw=true)


## CONFIGURATION

* Create your virtual environment in Python 3.9.2 and added the file runtime.txt, install all dependencies indicated in requirements.txt as well added Procfile file.
* You can work with the same files:
     * apiMessage.py ------> Submit POST Request to Slack if there is any alert in our Thousand Eyes.
     * credentials.py ------> You must to replace with your Slack Token when you activate Incoming Webhook.

     ![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/webhookSlack.png?raw=true)

     * index.py ------> Activate your Web Server API using flask framework to receive POST request from Thousand Eyes Webhook service.

* The "index.py" file allows you to active a Web Server API in Heroku Cloud where you can see the flow request using the line command "heroku logs --tail" however you need to install Heroku CLI https://devcenter.heroku.com/articles/heroku-cli.

## RUNNING

* Activate your Web Server TD Bank with your Ngrok and Babyweb then go to ThousandEyes > Cloud & Enterprise Agents > Test Settings  and change your URL “https://6ffa-192-226-134-67.ngrok.io”

![image](ttps://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/thousandEyesTest.jpg?raw=true)

* You will receive an alert cleared in the channel of Slack “# thousand-eyes-alerts”
	
     - Action: Alert Cleared
          Output: 
          {
          "alert": {
               "active": 0,
               "agents": [
                    {
                         "active": 0,
                         "agentId": 20739,
                         "agentName": "Guadalajara, Mexico (Trial)",
                         "dateEnd": "2022-02-19 08:12:00",
                         "dateStart": "2022-02-18 20:25:00",
                         "metricsAtEnd": "Error: \"\"",
                         "metricsAtStart": "Error: \"502 Bad Gateway\"",
                         "permalink": "https://app.thousandeyes.com/alerts/list/?__a=415786&alertId=108505079&agentId=20739"
                    }
               ],
               "alertId": 108505079,
               "apiLinks": [
                    {
                         "href": "https://api.thousandeyes.com/v4/tests/2585349",
                         "rel": "related"
                    },
                    {
                         "href": "https://api.thousandeyes.com/v4/web/http-server/2585349",
                         "rel": "data"
                    }
               ],
               "dateEnd": "2022-02-19 08:12:00",
               "dateEndZoned": "2022-02-19 08:12:00 EST",
               "dateStart": "2022-02-18 20:25:00",
               "dateStartZoned": "2022-02-18 20:25:00 EST",
               "permalink": "https://app.thousandeyes.com/alerts/list/?__a=415786&alertId=108505079",
               "ruleAid": 415786,
               "ruleExpression": "Error is present",
               "ruleId": 1927034,
               "ruleName": "Webhook Thousand Eyes",
               "testId": 2585349,
               "testLabels": [],
               "testName": "TD Bank Web Server ",
               "testTargetsDescription": [
                    "https://6ffa-192-226-134-67.ngrok.io"
               ],
               "type": "HTTP Server",
               "violationCount": 1
          },
          "eventId": "367417671-108505079",
          "eventType": "ALERT_NOTIFICATION_CLEAR"
          }

     ![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/alertCleared.png?raw=true)

     ![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/alertClearedTe.png?raw=true)

     ![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/alertClearedWeb.png?raw=true)

* Turn off your Web Server TD Bank using “Babyweb” application, you will receive an alert active “active": 1,” in the channel of Slack “# thousand-eyes-alerts”

    ![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/alertClearedBw.png?raw=true)

     - Action: Alert Active
          Output: 
          {
          "alert": {
               "active": 1,
               "agents": [
                    {
                         "active": 1,
                         "agentId": 20739,
                         "agentName": "Guadalajara, Mexico (Trial)",
                         "dateStart": "2022-02-19 08:22:00",
                         "metricsAtEnd": "",
                         "metricsAtStart": "Error: \"502 Bad Gateway\"",
                         "permalink": "https://app.thousandeyes.com/alerts/list/?__a=415786&alertId=108562975&agentId=20739"
                    }
               ],
               "alertId": 108562975,
               "apiLinks": [
                    {
                         "href": "https://api.thousandeyes.com/v4/tests/2585349",
                         "rel": "related"
                    },
                    {
                         "href": "https://api.thousandeyes.com/v4/web/http-server/2585349",
                         "rel": "data"
                    }
               ],
               "dateStart": "2022-02-19 08:22:00",
               "dateStartZoned": "2022-02-19 08:22:00 EST",
               "permalink": "https://app.thousandeyes.com/alerts/list/?__a=415786&alertId=108562975",
               "ruleAid": 415786,
               "ruleExpression": "Error is present",
               "ruleId": 1927034,
               "ruleName": "Webhook Thousand Eyes",
               "testId": 2585349,
               "testLabels": [],
               "testName": "TD Bank Web Server ",
               "testTargetsDescription": [
                    "https://6ffa-192-226-134-67.ngrok.io"
               ],
               "type": "HTTP Server",
               "violationCount": 1
          },
          "eventId": "367422871-108562975",
          "eventType": "ALERT_NOTIFICATION_TRIGGER"
          }

          Send a message to thousand-eyes-alerts

     ![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/alertActive.png?raw=true)

     ![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/alertActiveTe.png?raw=true)

     ![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/alertActiveWeb.png?raw=true)

## SEARCHING WITH THIS CODE

* The intention to make this code is to generate curiosity, with them coming new ideas and as consequence arrive the creativity, finally you are in the innovation. Reach out via Cisco Webex ID erickzabala@hotmail.com for any support questions.





