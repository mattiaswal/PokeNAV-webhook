import requests
import json
import time
import time

URL="http://localhost:8888"

WH_PAYLOAD = """[{
    "message": {
        "name": "Test",
        "latitude": 1.0,
        "longitude": 1.0,
        "level": 5,
        "pokemon_id": 175,
        "raid_end":  """+str(time.time()+3600)+""",
        "raid_begin": """+str(time.time()+1000)+""",
        "cp": 0,
        "move_1": 0,
        "move_2": 0,
        "gym_id": "Fake gym 1",
        "team": 1
    },
    "type": "egg"
} ]"""

payload = json.dumps(WH_PAYLOAD)

data = json.loads(payload)
raid_end=(time.time()+3600)/69
raid_start=(time.time()+100)/60

requests.post(URL, data = WH_PAYLOAD)



