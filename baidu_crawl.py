import re
import requests

session = requests.session()

# send the request and get the content
def fetch_url(url):
    # print(session.get(url).content.decode('gbk'))
    return session.get(url).content.decode('gbk')

def get_doc_id(url):
    return re.findall('view/(.*).html',url)[0]

# doc type
def parser_type(content):
    return re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]

# main function
def main():
    url = input('Please enter the URL you would like to download: \n')

    # request
    content = fetch_url(url)

    # get id
    doc_id = get_doc_id(url)
    print(content)

    # doc type
    type = parser_type(content)
    print(type)

    # title
    # title = parser_title(content)

main()