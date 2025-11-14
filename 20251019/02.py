import requests

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
}

# 定义请求网址
url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action='

# 发起网络请求
response = requests.get(url, headers=headers)
print(response.text)
print("========================")
print(response.json())
print(type(response.json()))
print(type(response.json()[0]))
# response.json()是用于提取json字符串的，也只能用于提取json字符串，如果用来获取html数据就会报错。
#如果网页返回的是json字符串，可以通过response.json()方法来将这个字符串数据转换成列表或者字典

# 将获取的数据保存成html文件
# with open('douban1.html', 'wb') as file:
with open('douban1.json', 'wb') as file:
    file.write(response.content)
# json数据不能保存到html文件中，会显示乱码
# 除了英文之外的其它语言的字符，比如中文、韩文，有可能会进行编码，此时可以搜搜索对应的英文文本或阿拉伯数字

