# 豆瓣电影海报爬取程序 Summary

## 一、项目用途
自动爬取豆瓣电影分类排行榜中指定类型电影的海报图片，支持按页数控制爬取范围，提取电影标题并对应保存海报至本地。

## 二、核心功能
1. 支持用户输入爬取页数（每页含20部电影）
2. 自动请求多页电影数据接口，解析JSON格式响应
3. 提取电影标题及海报URL，批量下载并以标题命名保存
4. 实时反馈下载成功/失败状态及原因

## 三、程序设计思路
1. **目标拆解**：通过“获取数据→提取信息→下载保存”三步实现核心需求
2. **技术选型**：
   - `requests`：发送HTTP请求获取网络数据
   - `jsonpath`：解析嵌套JSON结构，高效提取标题（`title`）和海报URL（`cover_url`）
3. **流程设计**：
   - 配置请求头模拟浏览器，避免反爬拦截
   - 按用户输入页数，通过`start`参数（每页递增20）构造分页URL
   - 循环请求每页数据，解析后提取目标信息
   - 对海报URL发起请求，获取二进制数据并保存至本地指定路径
   - 用`try-except`捕获异常，确保程序稳定运行

## 四、代码核心结构
```python
# 导入依赖
import requests
from jsonpath import jsonpath

# 配置请求头
headers = {"User-Agent": "Mozilla/5.0 (...)"}

# 获取爬取页数
pages = int(input("请输入爬取页数："))

# 循环爬取多页
for i in range(pages):
    # 构造分页URL
    url = f"https://movie.douban.com/j/chart/top_list?type=6&start={i*20}&limit=20"
    # 获取并解析JSON数据
    json_data = requests.get(url, headers=headers).json()
    
    # 提取信息并下载
    for movie in json_data:
        title = jsonpath(movie, "$.title")[0]
        poster_url = jsonpath(movie, "$.cover_url")[0]
        
        try:
            # 下载并保存海报
            with open(f"豆瓣电影/海报/{title}.jpg", "wb") as f:
                f.write(requests.get(poster_url).content)
            print(f"成功：《{title}》")
        except Exception as e:
            print(f"失败：《{title}》，原因：{e}")


