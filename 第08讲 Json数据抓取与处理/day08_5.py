"""
以下代码由 新雨 编写
"""

"""
json格式的转换
"""
import json  # json库是自带的，不需要安装

# 将json字符串转换成字典或者列表

# 1、读取文件中的json字符串
with open('douban.json', 'r', encoding='utf-8') as file:
    json_string = file.read()

print(json_string)

# 2、将读取的json字符串转换成列表或字典
data = json.loads(json_string)
# print(type(data[0]))
print(data)
# print(type(data))

# 将列表或者字典转换成json字符串, ensure_ascii=False是用于设置不对中文进行转义
json_str = json.dumps(data)
print(json_str)
json_str = json.dumps(data, ensure_ascii=False)
# print(type(json_str))
print(json_str)