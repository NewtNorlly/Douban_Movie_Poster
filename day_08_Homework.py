"""
以下代码由 柴桑 编写，笔者要爬取豆瓣电影分类排行榜 - 科幻片的网页海报
抓取豆瓣电影榜单的电影数据，并使用 jsonpath 筛选电影信息。
代码截图：
效果截图：
"""

# 我要导入请求库和宅森库
import requests
from jsonpath import jsonpath

# 这是我的请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

# 从键盘输入抓取的页数
pages = int(input('请输入抓取的页数：'))

# 循环遍历抓取的次数
for i in range(pages):
    # 定义请求网址
    # url = f'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start={i * 20}&limit=20'
    url = f'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start={i * 20}&limit=20'

    # 发起网络请求
    response = requests.get(url, headers=headers)

    # 提取json数据
    json_data = response.json()

    # 将列表数据遍历成单个的字典
    for data in json_data:
        # 对字典数据进行筛选
        # print(data)
        title_list = jsonpath(data, '$..title')[0]
        url_list = jsonpath(data, '$..cover_url')[0]
        print(title_list)
        print(url_list)
        try:
            image_response = requests.get(url_list, headers=headers)
            # 这是向海报链接连接发起网络请求，获取预览图数据
            # with open(f'./豆瓣科幻片海报/{title_list}.jpg', 'wb') as f:
            # with open(f'./豆瓣情色片海报/{title_list}.jpg', 'wb') as f:
            with open(f'豆瓣电影\豆瓣情色片海报\{title_list}.jpg', 'wb') as f:
                f.write(image_response.content)
            # 以二进制的格式保存预览图，以对应的电影名称给每个图片命名
            print('歐耶，你下載成功啦！', title_list, url_list)
        # 我还得知道，有没有下载成功？
        except Exception as e:
            print(f"图片 {title_list} 下载失败，错误信息: {e}")


