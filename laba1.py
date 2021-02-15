#!/usr/bin/env python
# coding: utf-8

import urllib
from urllib.request import urlopen
from datetime import datetime

def save_1(i):
    url_part1 = 'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID='
    url_part2 = '&year1=1981&year2=2021&type=Mean'
    time = now.strftime("%d-%m-%Y %H:%M")
    url = url_part1+str(i)+ url_part2
    vhi_url = urlopen(url)
    out = open('vhi_id_' + str(i)+'_'+time +'.csv','wb')
    out.write(vhi_url.read())
    out.close()
    print ("VHI is downloaded...")
    
    
    
def save_2(i):
    url_part1 = 'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID='
    url_part2 = '&year1=1981&year2=2021&type=Mean'
    time = now.strftime("%d-%m-%Y %H:%M")
    url = url_part1+str(i)+ url_part2
    urllib.request.urlretrieve(url,'./vhi/'+'vhi_id_' + str(i)+'_'+time +'.csv')
   
for i in range (1,28):
    save_2(i)


# In[83]:


import pandas as pd  
import glob
a = '/home/ubuntu1/enviroments/my_env/vhi/'
b = '/home/ubuntu1/enviroments/my_env'

def frame(a):
    files = glob.glob(a + '*.csv')
    files.sort()
    dfs = []
    for fp in files:
        dfs.append(pd.read_csv(fp, index_col= False, header=1))
    return dfs

list1 = frame(a)

for i in range (0,27):
    list1[i].columns = ['Year','week','one','two','three','for','vhi','vhi6']
    del list1[i]['vhi6']
list1[9]



def extr(i, year):
    temp = list1[i].loc[list1[i]['Year'] == year] 
    val = temp.loc[list1[i]['vhi'] != -1]
    min = val['vhi'].min()
    max = val['vhi'].max()
    print ('max', max, 'min:', min)
extr(1,'1981'




def obl(i):
    val = list1[i].loc[list1[i]['vhi'] != -1]
    vall = val.query('vhi < 15')
    a = vall['Year'] 
    return vall, a.unique()
obl1(1)


def obl(i):
    val = list1[i].loc[list1[i]['vhi'] != -1]
    vall = val.query('vhi > 15')
    valll = vall.query('vhi < 35')
    a = valll['Year'] 
    return valll, a.unique()
obl(1)
