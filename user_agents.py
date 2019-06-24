import urllib.request
import urllib.parse
import string
import random


def main():
    # base url
    url = "https://www.baidu.com/s?wd="
    url += "大数据"
    print(url)

    # ascii
    url = urllib.parse.quote(url, safe=string.printable)
    print(url)

    # user agents
    user_agents = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    ]
    user_agent = random.choice(user_agents)
    print(user_agent)

    # header
    header = {
        "User-Agent": random.choice(user_agents),
    }

    # request
    request = urllib.request.Request(url, headers=header)

    # conn
    resp = urllib.request.urlopen(request)

    # save
    data = resp.read().decode("utf-8")
    with open("04.html", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
