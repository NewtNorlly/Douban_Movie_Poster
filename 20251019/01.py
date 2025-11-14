import requests

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 定义请求网址
url = 'https://movie.douban.com/typerank?type_name=%E6%83%85%E8%89%B2&type=6&interval_id=100:90&action='

# 发起网络请求
response = requests.get(url, headers=headers)
print(response.text)  # response中搜不到

# 将获取的数据保存成html文件
with open('douban.html', 'wb') as file:
    file.write(response.content)
# 用浏览器打开html页面，发现没有电影信息，这只是个固态页面
# 可以对html文件惊进行预览，也可以在相应里面搜
# 一般json数据大都放在Fetch/XHR中
# 假如即不在html文档里，也不再Fetch/XHR中，那就有可能在JS中
