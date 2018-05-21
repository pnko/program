
# coding: utf-8

# # Excel 데이터 sqlite DB 저장하기

# # 1. excel 데이터 가져오기/ 데이터프레임으로 데이터 생성하기

# In[7]:


import sqlite3
import pandas as pd


# In[8]:


input_file = "/Users/kim/Downloads/실시간 수도정보 수위(시간)2018-04-27.xlsx"
data_frame = pd.read_excel(input_file, sheetname='1시간 수위')
data_sum = data_frame.loc[:,['자료 수집 TAG 설명','발생일시','유량']]
data_sum['발생일'] = data_sum['발생일시'].astype(str).str.slice(0, 8)
data_sum = data_sum.groupby(['자료 수집 TAG 설명','발생일'])['유량'].mean().reset_index()
data_sum.rename(index=str, columns={"자료 수집 TAG 설명": "a", "발생일": "b", "유량": "c"})
data_sum.columns = ['clear_well', 'check_date','value']
data_sum.head(6)


# # 2. 데이터 저장(sqlite) - Summary 데이터 저장 

# In[9]:


con = sqlite3.connect('Suppliers.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS kwater
				(clear_well VARCHAR(100), 
				check_date VARCHAR(100),
				value FLOAT);"""
c.execute(create_table)
con.commit()
data_sum.to_sql('kwater', con, flavor='sqlite', schema=None, if_exists='replace', 
                 index=True, index_label=None, chunksize=None, dtype=None)

con.close()


# In[6]:


#kwater = pd.read_sql_query("select * from kwater limit 5;", con)

