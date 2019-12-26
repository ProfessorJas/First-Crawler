import requests

# define the target url
url = 'https://www.baidu.com/'

# get request
res = requests.get(url=url)

print(res)
print(res.content)
print("RES_TEXT --->>> ", res.text)
print("RES_CONTENT_DECODE --->>> ", res.content.decode('utf-8'))
print("RES_HEADER --->>> ", res.headers)
print("RES_REQUEST_HEADER --->>> ", res.request.headers)