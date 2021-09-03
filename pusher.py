import requests
from datetime import date
import time

URL = 'http://gotify'
TOKEN = False

def new_app():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    data = '{ "description": "Test", "name": "test"}'

    response = requests.post(URL + '/application', headers=headers, data=data, auth=('admin', 'admin'))
    print(response.json())
    return response.json()['token']

if not TOKEN :
    TOKEN = new_app()

while True:
    today = date.today()
    resp = requests.post(URL + '/message?token=' + TOKEN, json={
        "message": "Test by " + str(today),
        "priority": 2,
        "title": "This is my title"
    })
    time.sleep(3)

