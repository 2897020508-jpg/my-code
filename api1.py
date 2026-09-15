import urllib.request
import json
response = urllib.request.urlopen("https://jsonplaceholder.typicode.com/users/1")
data = json.load(response)
print(data["name"])