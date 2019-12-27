import requests

# define url
u = 'https://fanyi.baidu.com/sug/'

# define header
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

x = input("Enter a thing: \n")
print(x)

# data send from post
# data = {'kw': '你好'}
data = {'kw': x}

# send request
res = requests.post(url = u, headers = headers, data = data)

# get the return data
code = res.status_code

if code == 200:
    print('Request successfully')
    data = res.json()

    if data['errno'] == 0:
        print('Response successfully')
        
        k = data['data'][0]['k']
        v = data['data'][0]['v'].split(';')[-2]
        # v = data['data'][0]['v'].split(';')[1]
        # print(v.split(';')[-2])
        
        print(k, '====', v)

print(res.json())