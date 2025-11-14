"""
以下代码由 新雨 编写
浏览器开发者模式要点：
1.怎么样判断数据是由 html 还是 json 传递的，
预览 html 或 json 文件；
2.如果是 json 数据，在 XHR 里面找，还可以在 JS 里找；
3.如果数据包特别多，在放大镜里搜目标数据；
4.对于浏览器开发者模式中一些会编码的数据
尝试搜一些英文单词、阿拉伯数据。
"""

import requests

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

# 定义请求网址
url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

# 发起网络请求
response = requests.get(url, headers=headers)
print(response.text)

print('=====================')

print(response.json())

print('=====================')

# response.json()是用于提取json字符串的，也只能用于提取json字符串，如果用来获取html数据就会报错。
# 如果网页返回的是json字符串，可以通过response.json()方法来将这个字符串数据转换成列表或者字典
print(type(response.json()[0]), response.json())

# 将目标数据保存到文件中
with open('douban.json', 'w', encoding='utf-8') as file:
    file.write(response.text)
