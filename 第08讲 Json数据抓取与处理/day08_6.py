"""
以下代码由 新雨 编写
"""

import requests
import json

headers = {
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Acs-Token": "1744131606814_1744206495868_fTsweUDhIb6QZyNaMSu4OqhjNL1owIJKwFcRI70Ww3WmVib9Dszzmmmz8MD/J7t/wsN8ouboGny4zuWrjGCA+/CFVpngNn8k3IpQ/TD4WtaLPz8DloQyQVKHRfe4wkQ7+ruWLEvE7Kv4nNSrfDN7C6BQiT1O3+a17JOgUHDYWHgLgSjjKTUTEE5J7g2MD0rlhEWjTZzqt1WsdyJwdPWIYwepJM8A6C3uKxeoeGFcr2KKXpIWJpLzbiy8qkIsjaT1e0D9FupfVRsK8nSA+0/3ZqoV6gf0mbmKwQUgrqJQpFdBJUEPFAgHbrCQARtYsIy/T5EhL+NSeUvK6EBOMeblAz3fv2Zt2olQW7OiCeB55k1+wtb1aqg5pJV/GLuPOIIqkizm5MVok1ANBDEiKr9QqPjXgMZtpsfTq7RLoatBw3EWULWK0Uw0c1JtnbSfSUw8/yACk7veD2Pu28oCF4WBLeEBnzNH0uzCKAe5S661FA/mUEq7Yu0Qu0oGs1OJcO17",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://fanyi.baidu.com",
    "Pragma": "no-cache",
    "Referer": "https://fanyi.baidu.com/mtpe-individual/multimodal?query=dog&lang=en2zh&channel=pcHeader&ext_channel=DuSearch",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "accept": "text/event-stream",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "REALTIME_TRANS_SWITCH": "1",
    "FANYI_WORD_SWITCH": "1",
    "HISTORY_SWITCH": "1",
    "SOUND_SPD_SWITCH": "1",
    "SOUND_PREFER_SWITCH": "1",
    "PSTM": "1743163862",
    "BIDUPSID": "49C4A3A41437CE0EF17FAB5E8C94F80F",
    "BDUSS": "NESFowdkpmY0RmZTlNcDg4QUd2Y0RsQVYxREk0YU5Ba3N1Q2ZhV0p5RVlHQkpvSUFBQUFBJCQAAAAAAQAAAAEAAABgT0cWemxldmVsdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABiL6mcYi-pnSz",
    "BDUSS_BFESS": "NESFowdkpmY0RmZTlNcDg4QUd2Y0RsQVYxREk0YU5Ba3N1Q2ZhV0p5RVlHQkpvSUFBQUFBJCQAAAAAAQAAAAEAAABgT0cWemxldmVsdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABiL6mcYi-pnSz",
    "BAIDUID": "EACA6538F5FFA48D47ED31F507C8C8E4:SL=0:NR=10:FG=1",
    "H_WISE_SIDS": "61027_62229_62325_62343_62372_62594_62635_62674_62705_62693_62328_62801_62823_62833",
    "BDORZ": "B490B5EBF6F3CD402E515D22BCDA1598",
    "BAIDUID_BFESS": "EACA6538F5FFA48D47ED31F507C8C8E4:SL=0:NR=10:FG=1",
    "H_PS_PSSID": "61027_62325_62343_62594_62635_62328_62823_62833_62845_62862_62879_62888",
    "BA_HECTOR": "012k0ga02k2k8l048g0k0l0k2m4p7m1jvcogq22",
    "ZFY": "TZzFmXq1knXTW7qjwemNkC3ef9TXxhuDyWf:ALQcy3pI:C",
    "BDRCVFR[feWj1Vr5u3D]": "I67x6TjHwwYf0",
    "PSINO": "3",
    "delPer": "0",
    "BDRCVFR[S4-dAuiWMmn]": "I67x6TjHwwYf0",
    "Hm_lvt_64ecd82404c51e03dc91cb9e8c025574": "1741867745,1742019832,1742040139,1744206379",
    "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574": "1744206379",
    "HMACCOUNT": "9D1224DFC3F36C20",
    "smallFlowVersion": "new",
    "ab_sr": "1.0.1_YjgzZTAzZjA3ZGVhMDc1NjA0ZGVmMzY3YzRhYzAwN2NhNjc3M2VhODVjYWQzMzQwOTQzNzJmYmIzNzAxZGNiYzk3YzJjZTExNjFjNWNlNDY3Zjc1NTI2YzYxOWQyNTE5MmE2Njc2ZjU0YmIwZDBlYjQwZTY5MjBmZWY4YmJhNjFjMWQwNjg0Y2FkOWM4NjMzNzc1YWU5NWU0MGNkNzUyOA==",
    "RT": "z=1&dm=baidu.com&si=26e9f68d-a372-455c-9b34-2ed103f1a6ee&ss=m99zg5tw&sl=7&tt=64f&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=28vn"
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

# response = requests.post(url, headers=headers, cookies=cookies, data=json_data)

# 这个是requests库所拥有的功能
response = requests.post(url, headers=headers, cookies=cookies, json=data)

print(response.text)
print(response)

