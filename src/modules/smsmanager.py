from twilio.rest import Client

# Handy manager for managing Twilio Messages
class Manager:

  def __init__(self, twilioSid, twilioToken, fromNumber):
    self.client = Client(twilioSid, twilioToken)
    self.fromNumber = fromNumber

  def send_text_message(self, toPhone, message):
    message = self.client.messages.create(to=toPhone, from_=self.fromNumber, body=message)
    return(message.sid)