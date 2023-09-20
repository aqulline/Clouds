import requests
import json
import uuid
import string
import random
import base64

username = '8ccab9418dedde47'
password = "ZGVmNWVkMzYxZmRhNWQ3MjM3NDhkMThmMWFkYzg4ZTM0ZGUwMjZmMGZjYTkzNWNkODRkMzFiMWJkZmM0M2JmYw=="
secure_token = '<secure_token>'

url = 'https://checkout.beem.africa/v1/checkout'

prefix = 'YUMMY-'
reference_number = prefix + ''.join(random.choices(string.digits, k=5))
print(reference_number)
amount = 2000
mobile = '255715700411'
transaction_id = str(uuid.uuid4())
send_source = True

params = {
    'amount': amount,
    'transaction_id': transaction_id,
    'reference_number': reference_number,
    'mobile': mobile,
    'sendSource': send_source
}

headers = {
    'Authorization': 'Basic ' + str(base64.b64encode(bytes(username + ':' + password, "utf-8")), "utf-8"),
    'Content-Type': 'application/json',
    'beem-secure-token': secure_token,
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print(json.loads(response.content))
else:
    print("Error occurred: " + response.content.decode('utf-8'))
