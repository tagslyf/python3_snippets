import requests
from requests.structures import CaseInsensitiveDict

url = "http://api.xiaofamao.com/api.php?json=0&v=1&key=testkey"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "wenzhang=%E5%BA%8A%E5%89%8D%E6%98%8E%E6%9C%88%E5%85%89%EF%BC%8C%E7%96%91%E6%98%AF%E5%9C%B0%E4%B8%8A%E9%9C%9C%E3%80%82"


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
