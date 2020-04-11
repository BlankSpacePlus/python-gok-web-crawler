import os
import requests

url = "https://pvp.qq.com/web201605/js/herolist.json"
# 获取英雄列表json文件
hero_list = requests.get(url)

hero_list_json = hero_list.json()
hero_name = list(map(lambda x: x['cname'], hero_list.json()))
hero_number = list(map(lambda x: x['ename'], hero_list.json()))


# 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        # 创建文件夹
        os.mkdir("D:/WangZheNongYao/" + hero_name[i])
        # 进入创建好的文件夹
        os.chdir("D:/WangZheNongYao/" + hero_name[i])
        i += 1
        # 据说目前王者农药没有一个英雄皮肤超过10个
        for k in range(10):
            # 拼接URL
            one_hero_link = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" + str(j) + "/" + str(j) + "-bigskin-" + str(k) + '.jpg'
            # 请求URL
            im = requests.get(one_hero_link)
            if im.status_code == 200:
                # 写入文件
                open(str(k) + '.jpg', 'wb').write(im.content)


downloadPic()
