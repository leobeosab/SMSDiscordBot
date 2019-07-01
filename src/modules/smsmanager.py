from twilio.rest import Client

# Handy manager for managing Twilio Messages


class SMS:

    def __init__(self, dbManager):
        self.dbManager = dbManager

    # Create Client for individual servers
    def createClient(self, serverID):
        creds = self.dbManager.getAuth(serverID)
        return {"client": Client(creds['sid'], creds['token']), "fromphone": creds['phonenumber']}

    def send_text_message(self, guild, toPhone, message):
        accountInfo = self.createClient(guild.id)
        message = guild.name + ": " + message
        try:
            accountInfo["client"].messages.create(
                to=toPhone, from_=accountInfo['fromphone'], body=message)
        except:
            raise Exception('Error, sending message through Twillio')

    def send_batch_message(self, guild, recipients, message):
        for recipient in recipients:
            self.send_text_message(guild, recipient['phonenumber'], message)
