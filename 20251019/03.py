"""
https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=0&limit=20
https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=20&limit=20
https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=40&limit=20
"""

import requests

# 从键盘输入抓取的页数
pages = int(input('请输入抓取的页数：'))

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

# 循环遍历抓取的次数
for i in range(pages):
    # 定义请求网址（带分页参数，start为每页起始位置，每页取20条）
    url = f'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start={i * 20}&limit=20'

    # 发起网络请求
    response = requests.get(url, headers=headers)

    # 将目标数据保存到文件中
    with open(f'douban-{i + 1}.json', 'w', encoding='utf-8') as file:
        file.write(response.text)

