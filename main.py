from http.server import BaseHTTPRequestHandler,HTTPServer
import json
from discord_webhook import DiscordWebhook
from flask import Flask,request,abort
import sys
import time
filename="config.json"
app = Flask(__name__)

with open(filename, 'r') as f:
        config = json.load(f)


def send_discord(message):
        webhook = DiscordWebhook(url=config["discord-webhook"], content=message)
        print("Sending to discord: {}".format(message))
        webhook.execute()

@app.route('/', methods=['GET'])
def index():
        print("Illegal metod")
        return "OK"

@app.route('/', methods=['POST'])
def accept_webhook():
        data=json.loads(request.data)
        for element in data:
                print(element)
                message=element["message"]
                if message["level"] < int(config["filter"]["min_lvl"]):
                        print("To low level, ignoring")
                        continue
                if(config["filter"]["raid"] and element["pokemon_id"] != 0):
                        timeleft=int((message["raid_end"]-time.time())/60)
                        send_discord("!raid {} {} {}".format(message["pokemon_id"],message["name"],timeleft))
                if(config["filter"]["egg"] and message["pokemon_id"] == 0):
                        timeleft=int((message["raid_begin"]-time.time())/60)
                        send_discord("!egg {} \"{}\" {}".format(message["level"],message["name"],timeleft))
        return "OK"

app.run(config["host"], config["port"])

