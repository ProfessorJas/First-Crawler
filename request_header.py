import requests

# define the target url
# url = 'https://www.qq.com'
url = 'https://www.xicidaili.com/nn/'

# define the request header to prevent block from the socket
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

# get request
# requests.get(url, headers)
#       url is the url you would like to visit
#       headers is the headers you would like it to be
res = requests.get(url = url, headers = headers)

# get the response status code
code = res.status_code
print(code)

# write the response to a file
if code == 200:
    with open('./test.html', 'w', encoding='utf-8') as fp:
        fp.write(res.text)