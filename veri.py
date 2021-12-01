import sqlite3
import requests
from bs4 import BeautifulSoup
isimler=[]


bag=sqlite3.connect("Futbolcular.db")
imlec=bag.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS futbolcular(İsim TEXText,Yas INT Ülke TEXT,Ayak TEXT,Fiyat INT,Mevki TEXT)")

url="https://www.transfermarkt.com.tr/super-lig/marktwerte/wettbewerb/TR1"
r=requests.get(url)

soup=BeautifulSoup(r.content,"html.parser")
isim=soup.find_all("a")
print(isim)

# imlec.execute("INSERT INTO futbolcular VALUES() ")