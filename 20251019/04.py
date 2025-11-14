import requests
import jsonpath

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
}

# 定义请求网址
url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action='

# 发起网络请求
response = requests.get(url, headers=headers)
# print(response.text)

# 提取json数据
json_data = response.json()
# json_data = response

# # 对json数据进行筛选
# title_list = jsonpath.jsonpath(json_data, '$..title')
# print(title_list)
# url_list = jsonpath.jsonpath(json_data, '$..url')
# print(url_list)

# 将列表数据遍历成单个的字典
for data in json_data:
    # print(data)
    # 对字典数据进行筛选
    title_list = jsonpath.jsonpath(data, '$..title')[0]
    print(title_list)
    url_list = jsonpath.jsonpath(data, '$..url')[0]
    print(url_list)

