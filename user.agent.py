import urllib.request
import urllib.parse
import string

def main():
    # base url
    url = "https://www.baidu.com/s?wd="
    url += "大数据"
    print(url)

    # ascii
    url = urllib.parse.quote(url,safe=string.printable)
    print(url)

    # headers
    header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    # request
    request = urllib.request.Request(url,headers=header)

    # get
    resp = urllib.request.urlopen(request)
    print(request.get_header("User-agent"))
    data = resp.read().decode("utf-8")
    with open("03.html","w") as f:
        f.write(data)

if __name__ == "__main__":
    main()
