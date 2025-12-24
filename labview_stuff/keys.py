import json

data = {
  "users": {
    "crogers": [
      "98bf3d234962a909a7212e24e28192a4332b53b5924a6c3a69379112e4f66708",
      "b3714cbdaff8fe3b50e5fafe82b49384a8dd92213fed737bd806abef3dff0706"
    ]
  },
  "proxies": {},
  "jwt": {
    "secret": "_xHaWpm91oYh4qah0cDqI2JGtjHcfNbgexTLxwa3GWo",
    "expiry_hours": 24
  }
}
users = list(data["users"].keys())
print(users)  