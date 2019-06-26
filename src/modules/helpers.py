import json

def get_secret_string(service, secret_key):
    try:
        with open('config/secrets.json') as f:
            return json.loads(f.read())["service"]["secret_key"]
    except:
        return ""