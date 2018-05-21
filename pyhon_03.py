
# coding: utf-8

# # 네이버 금융에서 환율 정보 활용하기
# http://info.finance.naver.com/marketindex/

# #  BeautifulSoup를 이용하여 html 데이터 가져오기
# 당일 환율 정보 가져오기

# In[181]:


from bs4 import BeautifulSoup
import urllib.request as req


# In[182]:


#HTML 가져오기
url = "http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)


# In[183]:


#HTML 분석하기
soup = BeautifulSoup(res, "html.parser")
print(soup)


# In[184]:


#원하는 데이터 추출하기
price = soup.select_one("div.head_info > span.value").string
time = soup.select_one("div.graph_info > span.time").string
print("time =", time)
print("usd/krw =", price)


# # 1. 최근일 환율정보 가져오기

# In[185]:


#HTML 가져오기
url = "http://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW"
res = req.urlopen(url)


# In[186]:


#HTML 분석하기
soup = BeautifulSoup(res, "html.parser")
print(soup)


# In[187]:


date_list = soup.select("td.date")
price_list = soup.select("td.num")
#print("date =", date_list)
#print("price =", price_list)


# In[188]:


col_date = []
for a in date_list:
    date = a.string
    print("-",date)
    col_date.append(date)


# In[189]:


col_price = []
for p in price_list:
    price = p.string
    if p.string != None :
        print("-",price)
        col_price.append(price.replace(',',''))


# # 2. 데이터프레임으로 데이터 생성하기

# In[190]:


import pandas as pd


# In[203]:


data_frame = pd.DataFrame({'date':col_date, 'price':col_price})


# In[204]:


print(data_frame.head(3))
print(data_frame.dtypes)
data_frame['date'] = data_frame['date'].astype(str)
data_frame['price'] = data_frame['price'].apply(pd.to_numeric, errors='coerce')
print(data_frame.dtypes)
print(data_frame.head(3))


# # 3. 시각화 하기(일자별 환율 Trand 보기)

# In[209]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")
#ax = sns.pointplot(x="date", y="price", data=data_frame)
ax = sns.pointplot(x="date", y="price", data=data_frame.sort_values(by=['date']))
plt.show()


# # 4. 데이터 저장(sqlite)

# In[194]:


import sqlite3


# In[210]:


con = sqlite3.connect('Suppliers.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS exrate_us
				(date VARCHAR2(100), 
				price FLOAT);"""
c.execute(create_table)
con.commit()
data_frame.to_sql('exrate_us', con, flavor='sqlite', schema=None, if_exists='replace', 
                 index=True, index_label=None, chunksize=None, dtype=None)
con.close()


# In[207]:


con = sqlite3.connect('Suppliers.db')
c = con.cursor()
exrate_us = pd.read_sql_query("select * from exrate_us ;", con)
print(exrate_us.dtypes)
print(exrate_us)
con.close()

