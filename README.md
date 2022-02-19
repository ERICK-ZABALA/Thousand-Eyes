
![image](https://github.com/ERICK-ZABALA/Thousand-Eyes/blob/master/slackBot/thousandEyesLogo.jpg)

# THOUSAND EYES

## OVERVIEW

This example is an integration between ThousandEyes and Slack using Python. ThousandEyes sends alert notifications via our webhook service and those notifications are received in the Web Server deployed as an application in the cloud of Heroku. The Web Server who is hosted in Heroku Cloud send the notifications to Slack device using an incomming webhook of Slack that is a simple way to post messages from external sources (third parties).

## PREREQUISITES

*  Create a trial account at https://www.thousandeyes.com/signup/. Write “Cisco” in the company field.
*  Configure a test with an alert that will trigger and clear alerts for your testing in Thousand Eyes.
*  Create a Slack instance https://slack.com/get-started#/createnew. 
*  Create a Heroku account at https://id.heroku.com/login.
*  Deploy a Web Server in your PC to make testing with Thousand Eyes, you can use the folder:webServerTdBank and the app:babywebssl.rar and ngrok (https://ngrok.com/download) to publish the service to internet.


## CONFIGURATION

 * Create your virtual environmet in Python 3.9.2 and added the file runtime.txt, intall all dependecies indicated in requirements.txt as well added Procfile file.

 * You can use the same files:
 
      * apiMessage.py  ------> Submit POST Request to Slack if there is any alert in out Thousand Eyes.
      * credentials.py ------> You need to remplace to your Slack Token.
      * index.py       ------> Active your Web Server using flask framework to receive POST request from Thosand Eyes Webhook service.

 * The "index.py" file allows you to active a web server in heroku Cloud where you can see the flow request using the comand line "heroku logs --tail" however you need to install Heroku CLI https://devcenter.heroku.com/articles/heroku-cli.



 ## UNDERSTANDING THE CODE

The intention to make this code is generate curiosity, then comming new ideas as consequence of creativity and finally your are in the inovation. 

Reach out via Cisco Webex for any support questions.



