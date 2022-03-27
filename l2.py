import urllib.request as urllib2
import json
import csv


data = []
for i in range (1,13):
    print(i)
    for j in range(1,32):
        if(i>=10):
            url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=2021"+str(i)+str(j)+"&json"
        else:
            url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=20210"+str(i)+str(j)+"&json"
        d = urllib2.urlopen(url).read()
        data.append(json.loads(d))


data[0]
!pip3 install urllib2
fulldata = []
for d in data:
    for i in d:
        fulldata.append(i)
def save_as_csv(data,name):
    count = 0
    fname = name
    with open(fname,'w') as outf:
        outcsv = csv.writer(outf)
        for d in data:
            if count == 0:
                header = d.keys()
                outcsv.writerow(header)
                count += 1
            outcsv.writerow(d.values())
save_as_csv(fulldata,'mydata.csv')
!sudo yum install boto3
import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
!pip install boto3 
s3 = boto3.client('s3')
with open("mydata.csv", "rb") as f:
    s3.upload_fileobj(f, "sofffbucket", "kurs.csv")
with open('kurs.csv', 'wb') as f:
    s3.download_fileobj('sofffbucket', 'kurs.csv', f)
import pandas as pd
df = pd.read_csv('kurs.csv')
df.head()
df['exchangedate'] =  pd.to_datetime(df.exchangedate)
EUR = df.where(df['cc']=='EUR').sort_values(by = 'exchangedate').dropna()
USD = df.where(df['cc']=='USD').sort_values(by = 'exchangedate').dropna()
EUR[['exchangedate','rate']].where(EUR['exchangedate'].dt.day==28).dropna()
#!pip3 install matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

fig = plt.figure()

fig, ax = plt.subplots()

ax.plot(EUR['exchangedate'].where(EUR['exchangedate'].dt.day==1).dt.month,  EUR['rate'].where(EUR['exchangedate'].dt.day==1), label = 'EUR')
ax.plot(USD['exchangedate'].where(USD['exchangedate'].dt.day==1).dt.month,USD['rate'].where(USD['exchangedate'].dt.day==1),label = 'USD')
fig.set_figheight(5)
fig.set_figwidth(10)
ax.set_xlabel('month')
ax.set_ylabel('rate')
ax.legend()
loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
ax.xaxis.set_major_locator(loc)
ax.yaxis.set_major_locator(plticker.MultipleLocator(base=0.5))
plt.show()
fig = plt.figure()
fig, ax = plt.subplots()
ax.plot(EUR['exchangedate'].where(EUR['exchangedate'].dt.day==28).dropna().dt.month, EUR['rate'].where(EUR['exchangedate'].dt.day==28).dropna(), label = 'EUR') 
ax.plot(USD['exchangedate'].where(USD['exchangedate'].dt.day==28).dropna().dt.month,USD['rate'].where(USD['exchangedate'].dt.day==28).dropna(),label = 'USD') 
fig.set_figheight(10) 
fig.set_figwidth(10) 
ax.set_xlabel('month') 
ax.set_ylabel('rate') 
ax.legend() 
loc = plticker.MultipleLocator(base=1.0) 
# this locator puts ticks at regular intervals 
ax.xaxis.set_major_locator(loc) 
ax.yaxis.set_major_locator(plticker.MultipleLocator(base=0.2)) 
plt.show()
plt.savefig('per_months.png')
fig = plt.figure()

fig, ax = plt.subplots()

ax.plot(EUR['exchangedate'],  EUR['rate'], label = 'EUR')
ax.plot(USD['exchangedate'],USD['rate'],label = 'USD')

ax.set_xlabel('date')
ax.set_ylabel('rate')
ax.yaxis.set_major_locator(plticker.MultipleLocator(base=0.5)) 
ax.legend()
plt.show()
plt.savefig('during_year.png')
import boto3
s3 = boto3.client('s3')
with open("per_months.png", "rb") as f:
    s3.upload_fileobj(f, "sofffbucket", "per_months.png")
with open("during_year.png", "rb") as f:
    s3.upload_fileobj(f, "sofffbucket", "during_year.png")