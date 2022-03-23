from bs4 import BeautifulSoup
import requests

url = 'http://www.weather.com.cn/weather/101280101.shtml'
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, "lxml")
list = soup.find('ul', class_="t clearfix")
tem = list.find('p', class_="tem").find('i').text
print(tem)
