## 3장 데이터 소스의 저장과 가공(P98(118))
### 3-1 웹의 다양한 데이터 형식
- XML/JSON/YAML/CSV/TSV/엑셀/PDF
- 텍스트와 바이너리 데이터 : 텍스트(일반적인 자연 언어:한국어,영어,일본어), 숫자 등, 바이너리(일반적인 텍스트 에디터로 열 수 없음, 시각적으로 의미를 알 수 없는 문자열로 되어있음.,텍스트에 비해 크기가 작음, 동영상, 이미지 크기 압축등 사용)
 - 문자 인코딩 : EUC_KR, UTF8 등 데이터가 어떻게 저장되었냐에 따라 , 출력시 문자가 깨져 있을 수 있음.
 
 filename="a.bin"
data=100
with open(filename, "wb") as f:
    f.write(bytearray([data]))
# hexdump a.bin  윈도우 에서는 hexdump.exe 가 없음.    


#### XML(Extensible Markup Language) 분석
- 텍스트 기반, 데이터를 태그로 감싸 마크업하는 범용적인 형식, 마크업( 태그 등을 이용하여 문서나 데이터의 구조를 명기하는 언어의 한 가지이다.태그는 원래 텍스트와는 별도로 원고의 교정부호와 주석을 표현하기 위한 것이였으나 용도가 점차 확장되어 문서의 구조를 표현하는 역할을 하게 되었다. 이러한 태그 방법의 체계를 마크업 언어라 한다.) 계측 구조로 표현

# 날씨 분류하기
# 추가로 해야 될 것 : 바로 xml 읽어서 처리하는 것, 날씨에 대하여 시각화 하는 것 추가 필요.
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# 파일이 없으면 다운로드 , 있으면 다운로드 하지 않음
savename = "forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, "html.parser")
    
    
info = {}
for location in soup.find_all("location") :
    name = location.find('city').string
    weather = location.find('wf').string
    if not(weather in info):
        info[weather]=[]
    info[weather].append(name)

for wether in info.keys():
    print("+", weather)
    for name in info[weather]:
        print("| - ", name)
        

#### JSOM(JavaScript Object Notation) 분석
: 텍스트 기반으로 하는 가벼운 데이터 형식, 자바스크립트에서 사용하는 캑체 표기 방법을 기반, 다양한 소프트웨어와, 프로그램밍 언어끼리
    데이트를 교환할 때 사용, 구조가 단순, 많은 웹 API들이 JSON형식으로 데이터를 제공함 
    http://json.org
    
"""GitHub 최근 프로젝트 정보 : https://api.github.com/repositories
   리포지토리의 이름 소유자 추출"""
import urllib.request as req
import os.path, random
import json

# json 파일 로컬에 저장
url ="https://api.github.com/repositories"
savename = "repo.json"
if not os.path.exists(url):
    req.urlretrieve(url,savename)
    
    
# json 파일 로드 및 출력
items = json.load(open(savename, "r", encoding="utf-8"))
for item in items:
    print(item["name"] + " - " + item["owner"]["login"])    
    

### CSV/TSV분석 P114(136)
: CSV는 단순하고 ,엑셀로 쉽게 많을수 있으며, 수많은  데이터베이스와 데이터 도구 등에서 CSV 형식 지원

import csv, codecs

#CSV 파일 읽기
filename ="list-euckr.csv"
fp = codecs.open(filename, "r", "euc_kr")

#한 줄씩 읽어 드리기
reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader :
    print(cells[1], cells[2])
    
    
#CSV 저장
with codecs.open("test.csv", "w", "euc_kr") as fp :
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID","이름","가격"])
    writer.writerow(["1001","SD 카드",300000])
    writer.writerow(["1002","키보드",21000])
    writer.writerow(["1003","마우스",15000])
    
# Pandas 이용해 보기
# 행정구역 및 인구현황 엑셀(http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1041)
import pandas as pd

filename = "stat_104102.xls"
sheet_name = "Sheet0"
book = pd.read_excel(filename, sheetname=sheet_name, header=2)
print(book.head())
#book.rename(index=str, columns={"": "citis"})
book = book.sort_values(by="2017", ascending=False)
book = book.dropna(thresh=9) # null값 삭제
#book = book.drop(["계"]) # 계 삭제
book


book_tran = book.T
book_tran['계'] = book_tran['계'].str.replace(",","")
book_tran['계'] = book_tran['계'].astype(int)
book_tran


import seaborn as sns
sns.pointplot(x="index", y="계", data=book_tran.reset_index())

#book = book.drop(["계"]) # 계 삭제
book_stack = book.stack()
book_stack = book_stack.reset_index()
book_stack = book_stack.rename(columns={0:'value'})
print(book_stack.info())
book_stack['value'] = book_stack['value'].str.replace(",","")
book_stack.head()

#book_stack['value'] = book_stack['value'].str.replace(",","")
book_stack['value'] = book_stack['value'].astype(int)
#sns.pointplot(x="level_0", y="value", hue ="level_1", data=book_stack)


## 3-2 데이터 베이스(P129(148))
: SQLite - 가볍게 파일 하나로 사용할 수 있는 데이터베이스, 웹 브라우저 내부 및 안드로이드/IOS에서 표준으로 제공되는 데이터베이스 

    
import sqlite3

# 데이터 베이스 연결
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

# 테이블 생성하고 데이터 넣기
cur = conn.cursor()
# 여러 문장 실행시 executescript
cur.executescript("""
    DROP TABLE IF EXISTS items;
    
    CREATE TABLE items(
        item_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        price INTEGER
        ) ;

    INSERT INTO items(name, price) VALUES('Apple', 800);
    INSERT INTO items(name, price) VALUES('Orange', 780);
    INSERT INTO items(name, price) VALUES('Banana', 430);

""")
conn.commit() # 반영

# 한문장 실행시 execute
cur.execute("SELECT item_id, name, price FROM items")
# 전체를 추출할때 (fetchall), 한개씩 추출할때(fatchone)
item_list = cur.fetchall()

item_list 

for it in item_list :
    print(it)
  
  
# sqlite3 샘플 2
import sqlite3 

filepath ="test2.sqlite"
conn = sqlite3.connect(filepath)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""CREATE TABLE items(
        item_id INTEGER PRIMARY KEY,
        name TEXT ,
        price INTEGER)""")
conn.commit()

#데이터 넣기 
cur = conn.cursor()
cur.execute("INSERT INTO items (name, price) VALUES (?,?)",("Orange", 5200))
conn.commit()

cur = conn.cursor()
data = [("Mango", 7700), ("Kiwi", 4000), ("Grape", 8000),
       ("Peach",9400), ("Persimmon", 7000), ("Banana", 4000)]
cur.executemany(
        "INSERT INTO items(name, price) VALUES(?,?)", data)
conn.commit()

# 4000 - 7000원 데이터 추출하기 
cur =conn.cursor()
price_range = (4000, 7000)
cur.execute("SELECT * FROM items WHERE PRICE >= ? AND PRICE <= ?", price_range) #?로 선언하면, 두번째 값이 매개변수에서 실제 값을 지정
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)
    
   
### MySQL 사용하기
# MySQL Clint 설치 필요
import MySQLdb

# MySQL 연결
conn = MySQLdb.connect(
    user ='root',
    passwd='test-password',
    host='localhost',
    db='test')

# 커서 추출하기
cur = conn.cursor()

#테이블 생성
cur.execute('DROP TABLE items')
cur.execute("""
        CREATE TABLE items (
            item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name TEXT,
            price INTEGER
            )
""")

# 데이터 추가하기
data = [("Mango", 7700), ("Kiwi", 4000), ("Grape", 8000),
       ("Peach",9400), ("Persimmon", 7000), ("Banana", 4000)]
for i in data :
    cur.execute("INSERT INTO items(name,price) VALUES(%s, %s)", i)
    
# 데이터 추출하기
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)
    
    


