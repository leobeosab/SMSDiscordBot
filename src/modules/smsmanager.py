from twilio.rest import Client
from pprint import pprint

# Handy manager for managing Twilio Messages
class SMS:

  def __init__(self, dbManager):
    self.dbManager = dbManager

  # Create Client for individual servers
  def createClient(self, serverID):
    creds = self.dbManager.getAuth(serverID)
    return { "client": Client(creds['sid'], creds['token']), "fromphone": creds['phonenumber']}
    
  def send_text_message(self, serverID, toPhone, message):
    accountInfo = self.createClient(serverID)
    message = accountInfo["client"].messages.create(to=toPhone, from_=accountInfo['fromphone'], body=message)
    return(message.sid)

  def send_batch_message(self, serverID, recipients, message):
    for recipient in recipients:
      self.send_text_message(serverID, recipient.number, message)