import requests

URL = "https://users.roblox.com/v1/users/3290769146"
WEBHOOK = "thank you good samaritan!"

r = requests.get(URL)
data = r.json()

if data.get("hasVerifiedBadge") == True:
    requests.post(WEBHOOK, json={
        "content": "<@303699809439711232> 🚨 c8jayson just got a VERIFIED BADGE!"
    })
