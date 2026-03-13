import requests

URL = "https://users.roblox.com/v1/users/3290769146"
WEBHOOK = "https://discord.com/api/webhooks/1482150382514733207/MK3J5XQBhHgjr683M-kCROYD-1b6ELmUVfploDBNHHpPugoLshoydUmXRZmzhmnN4iZj"

r = requests.get(URL)
data = r.json()

if data.get("hasVerifiedBadge") == True:
    requests.post(WEBHOOK, json={
        "content": "🚨 c8jayson got VERIFIED BADGE!"
    })
