import json

def lambda_handler(event, context):
    #First check the request type.
    reqType = event['request']['type']
    
    if reqType == "LaunchRequest":
      return {
       "version": "1.0",
       "response": {
        "outputSpeech": {
          "type": "PlainText",
          "text": "Hi Peter, What can I help you with!"
        },
        "card": {
          "content": "Im here to make things easy for you",
          "title": "What can I help you with",
          "type": "Simple"
        },
        "reprompt": {
          "outputSpeech": {
            "type": "PlainText",
            "text": "Are you still there"
          }
        },
        "shouldEndSession": False
      },
      
      "sessionAttributes": {}
     }
    
    elif reqType=="IntentRequest":
        #Check the current intent and decide what needs to be sent
        intent = event['request']['intent']['name']
        if (intent == "GeneralNotifications"):
            return {
          "version": "1.0",
          "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "You havent missed anything important"
            },
            "card": {
              "content": "Nothing missed!",
              "title": "Nothing missed in General, have a good day",
              "type": "Simple"
            },
            "reprompt": {
              "outputSpeech": {
                "type": "PlainText",
                "text": "Do you want me to do anything else"
              }
            },
            "shouldEndSession": False
          },
          "sessionAttributes": {}
        }
        elif (intent == "FetchNotifications"):
        #TODO : Develop actual interactions to the applications with possible interfaces
        #Check application name and decide accordingly
          try:
            applicationsName = event['request']['intent']['slots']['applicationName']['value']
          except KeyError:
            applicationsName = ""
          if(applicationsName == "database"):
            return {
            "version": "1.0",
            "response": {
              "outputSpeech": {
                "type": "PlainText",
                "text": "There is no notification from application " + applicationsName
              },
              "card": {
                "content": "no notification for "+applicationsName,
                "title": "no notification",
                "type": "Simple"
              },
              "reprompt": {
                "outputSpeech": {
                  "type": "PlainText",
                  "text": "Do you want me to check up anything else"
                }
              },
              "shouldEndSession": False
            },
            "sessionAttributes": {}
          }
          elif(applicationsName == "Microsoft"):#Stub application
            return {
            "version": "1.0",
            "response": {
              "outputSpeech": {
                "type": "PlainText",
                "text": "There were 8 high priority notifications for" + applicationsName + "but our Smart Support assistant solved it already."
              },
              "card": {
                "content": "High priority notifications but resolved",
                "title": "Microsoft with high priority alerts resolved by Smart Support",
                "type": "Simple"
              },
              "reprompt": {
                "outputSpeech": {
                  "type": "PlainText",
                  "text": "Do you want me to check up anything else"
                }
              },
              "shouldEndSession": False
            },
            "sessionAttributes": {}
          }
          #This is to deal with utterance without the app name, in the case it will work like GeneralNotifications intent
          elif(applicationsName == ""):
          #appName = ['slots']['applicationName']
            return {
          "version": "1.0",
          "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "There is a low priority notification from Sequel. Thats all"
            },
            "card": {
              "content": "Low priority notification for Sequel",
              "title": "Low Priority notification, nothing more",
              "type": "Simple"
            },
            "reprompt": {
              "outputSpeech": {
                "type": "PlainText",
                "text": "Do you want me to check up anything else"
              }
            },
            "shouldEndSession": False
          },
          "sessionAttributes": {}
        }
        #TODO : Implement pusing out emails to actual users/contacts with the help of email orchestration or a local mail service
        elif (intent == "PushNotifications"):
          matter = event['request']['intent']['slots']['matter']['value']
          getter = event['request']['intent']['slots']['getter']['value']
          #Debug
           #print(matter)
           #print(getter)
          #EndDebug
          return {
          "version": "1.0",
          "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "Sent a mail about "+ matter + " to " + getter + " successfully " 
            },
            "card": {
              "content": "Nothing missed!",
              "title": "Sent notification successfully",
              "type": "Simple"
            },
            "reprompt": {
              "outputSpeech": {
                "type": "PlainText",
                "text": "Do you want me to do anything else"
              }
            },
            "shouldEndSession": False
          },
          "sessionAttributes": {}
        }
        #This is something sent for 
        else:
          return {
          "version": "1.0",
          "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "You havent programmed me to do that yet Peter. I guess I will leave"
            },
            "card": {
              "content": "Not yet programmed",
              "title": "Unknown action",
              "type": "Simple"
            },
            "reprompt": {
              "outputSpeech": {
                "type": "PlainText",
                "text": "Do you want me to do anything else"
              }
            },
            "shouldEndSession": True
          },
          "sessionAttributes": {}
        }
