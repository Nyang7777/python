from urllib.parse import urlencode
import requests
import pandas as pd
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET

# url = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'
# response = requests.get(url)
# print(response.content)



# 공공 데이터
# /+==

# url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
# params ={'serviceKey' : '/+==', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'dataCd' : 'ASOS', 'dateCd' : 'DAY', 'startDt' : '20100101', 'endDt' : '20100601', 'stnIds' : '108' }
# response = requests.get(url, params=params)
# print(response.content)


# /+==
url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo'
params ='?'+ urlencode({'serviceKey' : '/+==', 'pageNo' : '1', 'numOfRows' : '10', 'zcode' : '11' })
requests = Request(url+params)
response_body = urlopen(requests).read()
print(response_body)
# print(response_body)
# 받은 xml을 DataFrame
root = ET.fromstring(response_body)
df = pd.DataFrame()
# 이터레이터: 순차적으로 접근할 수 있도록
for item in root.iter('item'):
    # 딕션너리
    item_dict = {}
    item_dict['충전소명'] = (item.find('statNm').text)
    item_dict['주소'] = (item.find('addr').text)
    item_dict['위도'] = (item.find('lat').text)
    item_dict['경도'] = (item.find('lng').text)
    item_dict['충전기상태'] = (item.find('stat').text)
    df = df._append(item_dict, ignore_index=True)
print(df)


