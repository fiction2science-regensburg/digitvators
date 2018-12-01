import json

def lambda_handler(event, context):
    # TODO implement
    #First check the request type.
    reqType = event['request']['type']
    
    if reqType == "LaunchRequest":
      return {
       "version": "1.0",
       "response": {
        "outputSpeech": {
          "type": "PlainText",
          "text": "What can I help you with!"
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
          try:
            applicationsName = event['request']['intent']['slots']['applicationName']['value']
          except KeyError:
            applicationsName = ""
          if(applicationsName == "service"):
            return {
            "version": "1.0",
            "response": {
              "outputSpeech": {
                "type": "PlainText",
                "text": "There is no notification from application " + applicationsName
              },
              "card": {
                "content": "Low priority notification for XYZ",
                "title": "Low Priority notification",
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
          elif(applicationsName == "Microsoft"):
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
          elif(applicationsName == ""):
          #appName = ['slots']['applicationName']
            return {
          "version": "1.0",
          "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "There is a low priority notification from application XYZ. Thats all"
            },
            "card": {
              "content": "Low priority notification for XYZ",
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
        
        elif (intent == "PushNotifications"):
          matter = event['request']['intent']['slots']['matter']['value']
          getter = event['request']['intent']['slots']['getter']['value']
          print(matter)
          print(getter)
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
        
        else:
          return {
          "version": "1.0",
          "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "This is a generic response"
            },
            "card": {
              "content": "Generic response",
              "title": "Generic response",
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

