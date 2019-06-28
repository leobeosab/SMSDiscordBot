from pymongo import MongoClient

class DBManager:

    def __init__(self):
        username = ""
        password = ""
        url = ""
        port = 27017

        self.client = MongoClient(url,
            port=port,
            username=username,
            password=password,
            authSource='admin',
            authMechanism='SCRAM-SHA-256')

        self.serverDB = self.client.data.servers
        
    def addOrUpdateServer(self, serverID, optedInUsers):
        server = {
            "_id": serverID,
            "opted-in-users": optedInUsers
        }

        # Upsert being true will insert if it doesn't exist
        self.serverDB.update_one({'_id': serverID}, {"$set": server}, upsert=True)
    
    def getServer(self, serverID):
        return self.serverDB.find_one({'_id': serverID})