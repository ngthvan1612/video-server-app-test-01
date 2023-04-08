HTTP_SERVER = "http://server:5050/swagger"
import requests
import json

while True:
    print(requests.get(HTTP_SERVER).text)

    import time
    time.sleep(1)

