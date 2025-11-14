"""
以下代码由 柴桑 编写
"""

import requests
import json

headers = {
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    "Acs-Token": "1761069606904_1761102333032_2SbaFFmpuR5t/fgms2b6JVBUhTtvYSp8reiiO9Efz7WPSamKStOnwZSmlGl/5EtYyhI0ASXIZU77GLDze7E45bCchl3EwxkKDJm47mLPKbYEq0DBjRIL33UbPAFLCtkCyhTd2X/iiGfUUfoxFyeyUBeYAM6vVofPc9iZ4+wzHMgj6/BMbyC4NtxQPcFTZ2m8EEQLWkPoUgEoFChsggkO2Zaly3P0I5pLL/uZJIlQA8+mTRGKQtxbfZzFqx7Yv4L/lyxE4941DOUnKH5rD/G4BFfQaRN5Dp6+30bQCejIOKItbY7l2I2jzsX2zGYs2VzIXCMyY416qTc6n2B4wUsIFvixhqIiBBmQRJnTehZ3gvu7aMya1WMF86hlNJYA+JE9x9NRnknt0mJbjpesV1SgzeOY7dmJyfwiqc9zsilqLUPmEDiyOpotpY3dp2S4fVFnQppEjEIbVZh+rDf4u8WX8hrBrVMoy6BrLk/5SosGnXMNADuLojzNzC/ESU6gxqp9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "DNT": "1",
    "Origin": "https://fanyi.baidu.com",
    "Referer": "https://fanyi.baidu.com/mtpe-individual/transText?query=cat%0A&lang=en2zh",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
    "accept": "text/event-stream",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

cookies = {
    "BAIDUID": "62DAFF59561B653BA830C720B5092E25:FG=1",
    "AIT_PERSONAL_VERSION": "1",
    "AIT_ENTERPRISE_VERSION": "1",
    "BDUSS": "lzeTdZbkhEbU9ZcGx1bzRlaDVlRHRLcHVUQjlUSDI3OGFzN1dVQW5-RUVDaGRwRUFBQUFBJCQAAAAAAQAAAAEAAAAhNA2N0NzXqLzStcTAz7jJsr8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAR972gEfe9oak",
    "BDUSS_BFESS": "lzeTdZbkhEbU9ZcGx1bzRlaDVlRHRLcHVUQjlUSDI3OGFzN1dVQW5-RUVDaGRwRUFBQUFBJCQAAAAAAQAAAAEAAAAhNA2N0NzXqLzStcTAz7jJsr8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAR972gEfe9oak",
    "BIDUPSID": "62DAFF59561B653BA830C720B5092E25",
    "PSTM": "1761027519",
    "H_PS_PSSID": "63145_64977_65248_65454_65452_65502_65361_65539_65569_65588_65607_65602_65663_65682_65702_65756_65731_65759_65771_65804_65853",
    "BDORZ": "FFFB88E999055A3F8A630C64834BD6D0",
    "H_WISE_SIDS": "63145_64977_65248_65454_65452_65502_65361_65539_65569_65588_65607_65602_65663_65682_65702_65756_65731_65759_65771_65804_65853",
    "BAIDUID_BFESS": "62DAFF59561B653BA830C720B5092E25:FG=1",
    "ZFY": "cBZJK8hjU5H:BLH:BY7JX86HSeWtCaKu89eIZYJnEBovM:C",
    "BAIDU_WISE_UID": "wapp_1761027928264_686",
    "ariaappid": "c890648bf4dd00d05eb9751dd0548c30",
    "ariauseGraymode": "false",
    "arialoadData": "false",
    "BA_HECTOR": "a18la12h20aha025ag8ka10hak24al1kfegg224",
    "RT": "\"z=1&dm=baidu.com&si=f0b51c10-33d9-4f5d-87e7-1fe709c110ef&ss=mh1efl1e&sl=2&tt=392z&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf\"",
    "ab_sr": "1.0.1_ZmViZGRkMmJkOTViNjkwYWI3MWQwM2M4MzFlM2I1YjMxYWZjMWNhMTRhN2Q2YWFkZjlhN2E3MWI5MjFhNzcxYzAxNzYxMjA2NWRlZjNkZDA2ZTg0YjBjNWE0YjIyMWZkYjM3MmFlNzdmMWIxMDJhZGM3MWNlZjMxMjc0MTRkNTU5MmZkZDhkYmUxYWUyMDFmNzMxMzQzYWI1YjQ1ZDYwZg=="
}

url = "https://fanyi.baidu.com/ait/text/translate"

data = {
    "query": "dog",
    "from": "en",
    "to": "zh",
    "reference": "",
    "corpusIds": [],
    "needPhonetic": False,
    "domain": "common",
    "milliTimestamp": 1744206496167
}

# 将定义的表单字典参数转换成json字符串
json_data = json.dumps(data)

# response = requests.post(url, headers=headers, cookies=cookies, data=data)  # 得不到想要的结果
# 如果传送字典，那么服务器一定会当作爬虫处理，那你就得转成json数据
# response = requests.post(url, headers=headers, cookies=cookies, data=json_data)

# 这个是requests库所拥有的功能
response = requests.post(url, headers=headers, cookies=cookies, json=data)

print(response.text)
print(response)
