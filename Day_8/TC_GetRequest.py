import requests
# GET
geturl="https://api.restful-api.dev/objects"

response = requests.get(geturl)

print(response.status_code)
print(response.json())


# POST

posturl=("https://api.restful-api.dev/objects")

body1={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

r1 = requests.post(posturl, json=body1)
print("post status code", r1.status_code)
print(r1.json())


# PUT

puturl="https://api.restful-api.dev/objects/ff8081819782e69e019be3ff2bd12e4a"

body2={
    "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

r2 = requests.put(puturl, json=body2)
print("put status code", r2.status_code)
print(r2.json())

# PATCH

patchurl="https://api.restful-api.dev/objects/ff8081819782e69e019be3ff2bd12e4a"

body3={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}


r3 = requests.patch(patchurl, json=body3)
print("patch status code", r3.status_code)
print(r3.json())

# DELETE

deleteurl="https://api.restful-api.dev/objects/ff8081819782e69e019be3ff2bd12e4a"


response = requests.delete(deleteurl)

print(response.status_code)
print(response.json())

