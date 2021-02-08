import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_page_content(url):
    # 得到页面的内容
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(url,headers=headers,timeout=10)
    content = html.text
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup

def content_analysis(soup):
    # 找到完整的投诉信息框
    temp = soup.find('div', class_="tslb_b")
    # 创建DataFrame
    df = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    # 找出所有行记录
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        # 获取汽车投诉信息
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            # 投诉编号
            id = td_list[0].text
            # 投诉品牌
            brand= td_list[1].text
            # 投诉车系
            car_model = td_list[2].text
            # 投诉车型
            type= td_list[3].text
            # 问题简述
            desc= td_list[4].text
            # 典型问题
            problem= td_list[5].text
            # 投诉时间
            datetime= td_list[6].text
            # 投诉状态
            status = td_list[7].text

            # 数据字典
            temp = {}
            temp["id"] = id
            temp["brand"] = brand
            temp["car_model"] = car_model
            temp["type"] = type
            temp["desc"] = desc
            temp["problem"] = problem
            temp["datetime"] = datetime
            temp["status"] = status
            df = df.append(temp, ignore_index=True)
    return df

# 创建DataFrame
result = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
# 请求URL
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
page_num = 20
for i in range(page_num):
    url = base_url + str(i + 1) + ".shtml"
    soup = get_page_content(url)
    df = content_analysis(soup)
    result = result.append(df)
    result= result.reset_index(drop=True)
    print(result)

# 数据保存到EXCEL中
result.to_excel("result.xlsx")
