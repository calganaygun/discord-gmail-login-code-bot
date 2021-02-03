# Discord Gmail Code Bot
Get login codes from a Discord text channel.

## Get Google Credentials
You can generate Gmail API service account with [this link](https://console.developers.google.com/start/api?id=gmail&credential=client_key).

## How to run?
### Heroku
You can easily deploy this app to Heroku:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

> GOOGLE_CREDENTIALS env variable is the content of your service account credentials JSON file.

### Docker
Or you can run this app on Docker:
```bash
# Clone this repo
git clone https://github.com/calganaygun/discord-gmail-login-code-bot.git
```

Move service account credentials JSON file to project directory with `google-credentials.json` name.

```bash
# Build docker image
docker build -t discord-gmail-login-code-bot .

# Edit env variables.
cp env.example .env && nano .env

# Run container
docker run --rm --env-file .env -d --name login-code-bot discord-gmail-login-code-bot

# See logs and authenticate your gmail account
docker logs discord-gmail-login-code-bot
```

| Env Variable         | Description                                                 |
|----------------------|-------------------------------------------------------------|
| `DISCORD_BOT_TOKEN`  | Discord bot token.                                          |
| `CODE_EMAIL_SENDER`  | The sender of the mail to be fetched.                       |
| `CODE_EMAIL_SUBJECT` | The subject of the mail to be fetched.                      |
| `CODE_REGEX`         | The regex that will be used to search for code in the mail. |
| `LISTENING_CHANNEL`  | The channel name the bot will listen to.                    |
| `LISTENING_PREFIX`   | The command prefix the bot will listen to.                  |
| `LISTENING_ROLE_NAME`| The only role that can get the code.                        |
