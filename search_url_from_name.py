#csvファイルの一行目の文字列をbingで検索した結果の一位のサイトのドメインを出力するプログラム。

from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import csv
from urllib.parse import urlparse
# urlが列挙されたcsvファイルを指定する
csv_reader = csv.reader(open("name.csv", "r"), delimiter=",", quotechar='"')
for row in csv_reader:

    search_name_japanese = row[0]
    url = str('https://www.bing.com/search?q=' + search_name_japanese + '&qs=n&form=QBLH&pq=' + search_name_japanese + '&sc=1-0&sp=-1&sk=&cvid=26AD2F8AFF204F3FA5060839422F1001')
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    p = urlparse(url)
    query = urllib.parse.quote_plus(p.query, safe='=&')
    url = '{}://{}{}{}{}{}{}{}{}'.format(
    p.scheme, p.netloc, p.path,
    ';' if p.params else '', p.params,
    '?' if p.query else '', query,
    '#' if p.fragment else '', p.fragment)
    response = urllib.request.urlopen(url)
    # ココらへんはお決まりのBeautifulSoupの流れ〜
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    url_class = soup.find(class_ = 'b_algo')
    if url_class is None: #なぜかうまくいかないときもあるので、回避策としてfailureと出力
        print("failure")
    else:
        url_a = url_class.find('a')
    # 以下でサブディレクトリを切り捨てる
        url = str(url_a['href'])
        if(url[:url.find('/',8)]==' '):
            print(url+"/")
        else:
            print(url[:url.find('/',8)+1])
