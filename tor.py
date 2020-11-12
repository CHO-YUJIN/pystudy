"""
import requests 
import re 
from bs4 import BeautifulSoup
from selenium import webdriver

headers = {"Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}

browser = webdriver.TheHiddenWiki()
browser.get("http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page")

url = http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

for i in range(1,50) :
    category = soup.find_all("li", attrs={"class":"toclevel-1 tocsection-{}".format(i)})
    title = category.a.get_text()
    link = category.a["href"]
    print(title, link)
    """

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import csv
import re
import requests
from bs4 import BeautifulSoup

# 동적 사이트 크롤링을 위한 추가
chrome_options = Options()
chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)
url = 'http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page'
driver.get(url)

# bs4
res = driver.page_source
soup = BeautifulSoup(res, "html.parser")

# 파일에 저장
filename = "tor_onion_address.csv"
f = open(filename,"w",encoding="utf8",newline="")
writer = csv.writer(f)

# 주소 가져오는 함수
def hidden_address():
    hidden_menus = soup.find_all("a",attrs={"class":"external text"})
    for hidden_menu in hidden_menus:
        hidden = hidden_menu.get('href')
        # csv파일에 넣기
        writer.writerow([hidden])
    f.close()

# 주소 가져오는 함수 실행
hidden_address()

# 끝나면 창 닫기
driver.close()