import requests

URL = "http://127.0.0.1:5000/anime/all"

resp = requests.get(URL).json()

for dic in resp:
    for key in dic:
        print(f"{key}-----{dic[key]}\n")
