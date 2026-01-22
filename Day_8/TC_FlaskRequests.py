import requests
# GET
geturl="//127.0.0.1:5000/"

response = requests.get(geturl)

print(response.status_code)
print(response.json())