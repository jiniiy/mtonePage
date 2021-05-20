import urllib.request
from bs4 import BeautifulSoup


class sakuraClass:
    def __init__(self, name, time, link):
        self.name = name
        self.time = time
        self.link = link


def getPytonFunc():
    url = "http://sakura-com.com/sakura-corporate/category/mtone/page"
    postNum = 1
    list = []
    try:
        for i in range(100):
            newUrl = url+str(postNum)
            # req = urllib.request.Request(newUrl)
            sourcecode = urllib.request.urlopen(newUrl).read()
            soup = BeautifulSoup(sourcecode, "html.parser")
            postNum = postNum+1
            for href in soup.find("div", class_="col-md-12 mainarea").find_all("article"):
                name = href.find('h3', class_='list-title post_ttl').text
                time = href.find('span', class_='post_time').text
                link = href.find("a")["href"]
                list.append(sakuraClass(name, time, link))
                print(href.find("div", {"class": "post_thumb"})["style"])
    except:
        return list
    return list


listed = getPytonFunc()
for sakura in listed:
    print(sakura.name, sakura.time, sakura.link)
