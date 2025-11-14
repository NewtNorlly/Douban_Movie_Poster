"""
以下代码由 新雨 编写
"""

import requests

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

# 定义请求网址
url = 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action='

# 发起网络请求
response = requests.get(url, headers=headers)
print(response.text)

# 将获取的数据保存成html文件
with open('douban.html', 'wb') as file:
    file.write(response.content)
