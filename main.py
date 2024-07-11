import random
import requests
id = random.randrange(1, 822263261)
url = f"https://api.github.com/repositories?since={id}"
json = requests.get(url).json()
print("https://github.com/" + json[0]["full_name"])
