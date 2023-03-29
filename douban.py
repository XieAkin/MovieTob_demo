import requests
from fake_useragent import UserAgent
import re
import json
headers = {
    'User-Agent':UserAgent().chrome
}

def get_classify():
    url = "https://movie.douban.com/chart"
    res = requests.get(url=url,headers=headers)
    data = []
    data.append(re.findall(r'<span><a href="(/typerank?.+)</a></span>',res.text))
    data.append(re.findall(r'type_name=([\u4e00-\u9fa5]{2,4})',json.dumps(data[0],ensure_ascii=False)))
    return data

def get_douban_json(id:str):
    url = f"https://movie.douban.com/j/chart/top_list?type={id}&interval_id=100:90&action=&start=0"
    res = requests.get(url=url,headers=headers)
    data_str = res.text
    data = json.loads(data_str)
    return data

if __name__ == '__main__':
    a = get_douban_json(id=11)
    for i in a:
        print(i)
    print()