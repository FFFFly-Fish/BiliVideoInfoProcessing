import json
import os
import random
import time
import requests
import csv

# 请求头
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
# 若不存在文件夹则创建一个
if not os.path.exists('./DataSave'):
    os.makedirs('./DataSave')
# 创建csv并写入标题
with open('./DataSave/data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(
        ['bvid', 'title', 'duration', 'view', 'danmaku', 'reply', 'like', 'coin', 'favorite', 'share', 'cid'])


def get_url(bv):
    # global title, duration, view,danmaku, reply, like, coin, favorite, share, cid
    url = 'http://api.bilibili.com/x/web-interface/view?bvid=' + bv
    geturl = requests.get(url, headers=headers)
    content = json.loads(geturl.text)
    # print(content)
    statue_code = content.get('code')
    # print(statue_code)

    if statue_code == 0:
        cid = content['data']['cid']
        title = content['data']['title']
        duration = content['data']['duration']
        view = content['data']['stat']['view']
        danmaku = content['data']['stat']['danmaku']
        reply = content['data']['stat']['reply']
        favorite = content['data']['stat']['favorite']
        coin = content['data']['stat']['coin']
        share = content['data']['stat']['share']
        like = content['data']['stat']['share']

    # 写入信息到csv
    with open('./DataSave/data.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # bv（Bv号）,title（标题）,duration（时长/秒),view(观看次数),danmaku(弹幕条数),
        # reply(评论条数),like(点赞人数),coin(投币数),favorite(收藏人数),share(分享),cid(视频编号)
        writer.writerow([bv, title, duration, view, danmaku, reply, like, coin, favorite, share, cid])

    # print('cid:', cid)
    print('标题:', title)
    # print('时长:', duration)
    print('观看次数:', view)
    print('弹幕条数:', danmaku, '评论条数:', reply)
    print('点赞人数:', like, '投币数:', coin, '收藏人数:', favorite, '分享:', share)
    print('=========================================================')


if __name__ == '__main__':
    # 读取get_bv中获取到的bv号
    file = open('./DataSave/bvid.txt')
    bv_id = list(file)
    bv_ids = [x.strip() for x in bv_id]  # 去除换行符和空行

    # 遍历txt，获取信息
    for i in range(len(bv_ids)):
        get_url(bv_ids[i])
        time.sleep(random.uniform(0.5, 2.0))
        i += 1
