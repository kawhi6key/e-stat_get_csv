import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


# 令和２年度地域保健・健康増進事業報告 > 健康増進編 > 市区町村表
r2_url = "https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450025&tstat=000001030884&cycle=8&tclass1=000001164286&tclass2=000001164291&tclass3=000001164293&tclass4val=0"
# 令和元年度地域保健・健康増進事業報告 > 健康増進編 > 市区町村表
r1_url = "https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450025&tstat=000001030884&cycle=8&tclass1=000001155266&tclass2=000001155275&tclass3val=0"
# 平成30年度地域保健・健康増進事業報告 > 健康増進編 > 市区町村表
h30_url = "https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450025&tstat=000001030884&cycle=8&tclass1=000001142306&tclass2=000001142315&tclass3val=0"
# 平成29年度地域保健・健康増進事業報告 > 健康増進編 > 市区町村表
h29_url = "https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00450025&tstat=000001030884&cycle=8&tclass1=000001126815&tclass2=000001126824&tclass3val=0"


# csvフォルダ下でcsvを格納するフォルダ名を指定する
datalist = {"2020":r2_url, "2019":r1_url, "2018":h30_url, "2017":h29_url}

for key, value in datalist.items():
    folderName = key
    url = value

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # フォルダを作成
    os.makedirs(f'csv/{folderName}', exist_ok=True)

    # csvの取得
    links = soup.find_all("a", class_='stat-dl_icon')

    for link in links:
        csv_link = str("https://www.e-stat.go.jp")+str(link.get('href'))
        print(csv_link)
        df = pd.read_csv(csv_link, encoding="cp932")
        dataName = df.iloc[0,1]
        df.to_csv(f'csv/{folderName}/{dataName}.csv', encoding="cp932")