import json

data={
    "name":"Rohan",
    "Age":23,
    "Skills":["python"]
}

with open("data.json","w") as file:
    json.dump(data,file,indent=2)