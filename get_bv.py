import os
import random
import time
import requests

# 若不存在文件夹则创建一个
if not os.path.exists('./DataSave'):
    os.makedirs('./DataSave')

# 请求头和接口
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
url = 'https://api.bilibili.com/x/space/arc/search'

def get_bvid():
    uid = input("输入up主uid:")
    page = input("输入需要获取的页数:")

    # 遍历每一页
    for i in range(int(page)):
        param = {
            'mid': uid,  # uid
            'ps': '30',  # 每页数量
            'tid': '0',
            'pn': str(i+1),  # 当前页数
            'keyword': '',
            'order': 'pubdate',
            'jsonp': 'jsonp'
        }
        html = requests.get(url=url, headers=headers, params=param).json()

        # 从中获取bvid信息
        for content in html['data']['list']['vlist']:
            bvid = content['bvid']
            print(bvid)

            with open('./DataSave/bvid.txt', 'a') as f:
                f.write(bvid + '\n')
        time.sleep(random.uniform(0.5,2.0))

if __name__ == '__main__':
    get_bvid()





