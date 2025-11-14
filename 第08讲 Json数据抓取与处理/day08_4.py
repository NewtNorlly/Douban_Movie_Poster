"""
以下代码由 新雨 编写
"""

import requests
from jsonpath import jsonpath

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

# 定义请求网址
url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

# 发起网络请求
response = requests.get(url, headers=headers)
# print(response.text)

# 提取json数据
json_data = response.json()

# # 对json数据进行筛选
# title_list = jsonpath(json_data, '$..title')
# print(title_list)
# url_list = jsonpath(json_data, '$..url')
# print(url_list)

# 将列表数据遍历成单个的字典
for data in json_data:
    # 对字典数据进行筛选
    # print(data)
    title_list = jsonpath(data, '$..title')[0]
    print(title_list)
    url_list = jsonpath(data, '$..url')[0]
    print(url_list)
