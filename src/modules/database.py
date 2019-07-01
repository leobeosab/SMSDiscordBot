from pymongo import MongoClient
from modules.helpers import getServiceSecretSet
from pprint import pprint


class DBManager:

    def __init__(self):
        mongodbSecrets = getServiceSecretSet("mongodb")
        username = mongodbSecrets["username"]
        password = mongodbSecrets["password"]
        url = mongodbSecrets["url"]
        port = mongodbSecrets["port"]

        self.client = MongoClient(url,
                                  port=port,
                                  username=username,
                                  password=password,
                                  authSource='admin',
                                  authMechanism='SCRAM-SHA-256')

        self.serverDB = self.client.data.servers
        self.authDB = self.client.data.twillioauth

    def addAuth(self, serverID, sid, token, phonenumber):
        auth = {
            "_id": serverID,
            "sid": sid,
            "token": token,
            "phonenumber": phonenumber
        }
        self.authDB.update_one({'_id': serverID}, {'$set': auth}, upsert=True)

    def getAuth(self, serverID):
        return self.authDB.find_one({'_id': serverID})

    def addOrUpdateServer(self, serverID, optedInUsers):
        server = {
            "_id": serverID,
            "opted-in-users": optedInUsers
        }

        # Upsert being true will insert if it doesn't exist
        self.serverDB.update_one(
            {'_id': serverID}, {'$set': server}, upsert=True)

    def getServer(self, serverID):
        return self.serverDB.find_one({'_id': serverID})

    def addUserToOptedIn(self, serverID, memberID, phonenumber):
        server = self.getServer(serverID)
        users = []

        if server is not None:
            users = server["opted-in-users"]

        index = next((i for i, item in enumerate(users)
                      if item["memberID"] == memberID), -1)
        if index == -1:
            users.append({"memberID": memberID, "phonenumber": phonenumber})
        else:
            users[index]["phonenumber"] = phonenumber

        self.addOrUpdateServer(serverID, users)
