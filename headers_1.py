import requests

request_headers = {}
request_headers["content-type"] = "text/plain"
request_headers["User-Agent"] = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Mobile Safari/537.36"
response = requests.get(url="https://www.testapp.com",headers=request_headers)

cookie_jar ={}
cookie_jar['sessionid'] = 'test1234'
