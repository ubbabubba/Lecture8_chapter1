import requests
Response = requests.get('https://www.google.com/search?q=mazda+cx-5')
print (Response.text)
