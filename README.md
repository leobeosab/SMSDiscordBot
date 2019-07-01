##### Created for Discord Hack Week 2019 by @leobeosab & @CJosephW :)
# Textee SMS bot
Twilio integrated bot for managing groups of players to send sms to (if they have opted in)

## Packages
* Twilio
* PyMongo
* Discord


## Running
1.  clone repo into SMSDiscordBot
2.  install required packages (see above)
3.  create a config/secrets.js [this](#config/secrets.js-file-structure) file structure
4. run ```python3 bot.py```

### Textee Bot commands
#### $authenticate:
Sets your Twillio credentials in the database. This is needed to send any messages. </br>
**Note: this should be done in a private text channel as your credentials need to be kept a secret** </br>
```$authenticate \<your Twillio sid> \<your Twillio token> \<your Twillio from phonenumber>``` <br/>

Example: ```$authenticate 123i849402148021 s3cr3t_t0k3n 1234567890```

#### $join
Opts in a user to be texted by the current server will also update phone number if user already exists </br>
```$join \<your phone number>``` </br>

Example: ```$join 1234567890```
#### $text
Sends a message to the mentioned users, roles, and channels</br>
**Note: these roles, users and channels can be chained to call any amount of them** </br>
```$text "\<your message>" @\<a role> #\<a channel> @\<a user> </br>``` </br>

Example: ```$text "Overwatch comp practice in 10 minutes, jump on!" @OWPlayers```

### config/secrets.js File Structure
```
// Note you need a running mongodb server with a data db and servers + auth collections
{
  "mongodb": {
    "url": your url,
    "port": your porty(27017 is the default port),
    "username": your username,
    "password": your password
  },
  "discord": {
    "token": your bot token
  }
}
```
