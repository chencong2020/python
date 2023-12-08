from urllib import request
import re
import time
import random
import csv
from ua_info import ua_list


# 定义一个爬虫类
class MaoyanSpider(object):
    # 初始化
    # 定义初始页面url
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"

    # 请求函数
    def get_html(self, url):
        headers = {"User-Agent": random.choice(ua_list),
                   "Cookie": '__mta=216405929.1701851864004.1701920079142.1701929845087.6; uuid_n_v=v1; uuid=B9612E20941211EEBF0AAFDCFAC3033F709C5E1944F1440E8574E111AB2CC60D; _csrf=0af1fdcaf34f67590a9115749e339d9e9e47e392d423f2c63767bf1ed765386f; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1701851864; _lxsdk_cuid=186e95fcaa6c8-0adf49566d9fc-26031951-1bcab9-186e95fcaa7c8; _lxsdk=B9612E20941211EEBF0AAFDCFAC3033F709C5E1944F1440E8574E111AB2CC60D; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1701939353; __mta=174552989.1701929777145.1701929777145.1701939353416.2; _lxsdk_s=18c437d96d7-a22-c42-c9e%7C%7C3'}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # print(html)
        # 直接调用解析函数
        self.parse_html(html)

    # 解析函数
    def parse_html(self, html):
        # 正则表达式
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        # 生成正则表达式对象
        pattern = re.compile(re_bds, re.S)
        # r_list: [('我不是药神','徐峥,周一围,王传君','2018-07-05'),...] 列表元组
        r_list = pattern.findall(html)
        print(r_list)
        self.save_html(r_list)

    # 保存数据函数，使用python内置csv模块
    def save_html(self, r_list):
        # 生成文件对象
        with open("maoyan.csv", "a", newline="", encoding="utf-8-sig") as f:
            # 生成csv操作对象
            writer = csv.writer(f)
            # 整理数据
            for r in r_list:
                name = r[0].strip()
                print('r[1]:', r[1])
                star = r[1].strip()[3:]
                print('star:', star)
                # 上映时间：2018-07-05
                # 切片截取时间
                print('r[2]:', r[2])
                time = r[2].strip()[5:]
                # time = r[2].strip()[5:15]
                print('time:', time)
                L = [name, star, time]
                # 写入csv文件
                writer.writerow(L)
                print(name, time, star)

    # 主函数
    def run(self):
        # 抓取第一页数据
        for offset in range(0, 11, 10):
            url = self.url.format(offset)
            print(url)
            self.get_html(url)
            # 生成1-2之间的浮点数
            time.sleep(random.uniform(1, 2))


# 以脚本方式启动
if __name__ == "__main__":
    # 捕捉异常错误
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print("错误:", e)
