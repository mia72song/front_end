import requests

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"

req = requests.get(url)
#print(req.status_code) #200
#print(type(req.text)) #<class 'str'>
data = req.json()
#print(type(data)) #<class 'dict'>
count = data["result"]["count"]

data = data["result"]["results"]
#print(data)
#print(len(data)==count) #True

with open("data.txt", "w", encoding="utf8") as f:  
    for d in data:
        stitle = d["stitle"]
        longitude = d["longitude"]
        latitude = d["latitude"]
        imgs = d["file"].split(r"http://")
        img_link = "http://"+imgs[1]
        
        f.write(f"{stitle}, {longitude}, {latitude}, {img_link}\n")
