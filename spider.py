import requests
from bs4 import BeautifulSoup
import pprint
import json

def download_all_htmls():
    """
        download all the htmls for later analysis
    """
    htmls = []

    for idx in range(24):
        url = f"http://www.crazyant.net/page/{idx+1}"
        print("Crawl html: ", url)
        r = requests.get(url)

        if r.status_code != 200:
            raise Exception("Error!")
        htmls.append(r.text)
    
    return htmls

htmls = download_all_htmls()

# print(htmls[0])

def parse_single_html(html):
    '''
        parsing a single html file, and get the data
        @return list({"link", "title", [label]})
    '''

    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all("article")
    datas = []

    for article in articles:
        # get the hyper link
        title_node = (
            article
            .find("h2", class_="entry-title")
            .find("a")
        )
        title = title_node.get_text()
        link = title_node["href"]

        # get tag nodes
        tag_nodes = (
            article
            .find("footer", class_="entry-footer")
            .find("span", class_="tags-links")
            .find_all("a")
        )
        tags = [tag_node.get_text() for tag_node in tag_nodes]
        datas.append(
            {"title": title, "link": link, "tags": tags}
        )
    return datas

# pprint.pprint(parse_single_html(htmls[0]))

all_datas = []
for html in htmls:
    all_datas.extend(parse_single_html(html))

print(all_datas)

with open("all_article_links.json", "w", encoding='utf-8') as fout:
    for data in all_datas:
        fout.write(json.dumps(data, ensure_ascii=False) + "\n")