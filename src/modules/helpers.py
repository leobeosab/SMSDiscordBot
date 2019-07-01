import json
from pathlib import Path

CONFIG_PATH = str(Path(__file__).parent.parent.parent.absolute()) + "/config/secrets.json"
print(CONFIG_PATH)
def getSecretString(service, secret_key):
    try:
        with open(CONFIG_PATH) as f:
            return json.loads(f.read())[service][secret_key]
    except:
        return ""

def getServiceSecretSet(service):
    try:
        with open(CONFIG_PATH) as f:
            return json.loads(f.read())[service]
    except:
        return ""