import requests
import json


def execute(url, payload):
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWRtaW4tY2xpZW50OnBhc3M='
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response)


def foo():
    x = {
        "env": "dev",
        "payloadFile": "temp1.json",
        "apiName": "submitApi"
    }
    baseUrl = ""
    url = ""
    if x["env"] == "dev":
        baseUrl = "https://jsonplaceholder.typicode.com"
    if x["apiName"] == "submitApi":
        contextPath = "/posts/10"
        url = baseUrl + contextPath
    execute(url, {})

if __name__ == '__main__':
    foo()
