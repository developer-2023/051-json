# pypi.org/project/requests
# itunes

import requests
import sys

# docs.python.org/3/library/json.html

import json

if len(sys.argv) != 2:
    sys.exit

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])