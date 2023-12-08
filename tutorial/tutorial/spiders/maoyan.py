import scrapy
from tutorial.items import TutorialItem


class MaoyanSpider(scrapy.Spider):
    name = "maoyan"
    allowed_domains = ["www.maoyan.com"]
    start_urls = ["https://www.maoyan.com"]
    offset = 0  # 查询字符串参数

    def parse(self, response):
        # 基准xpath，匹配电影信息的dd节点对象列表
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        # 给items.py 中的类：Maoyan100Item（）实例化
        item = TutorialItem()
        for dd in dd_list:
            item['name'] = dd.xpath('./a/@title').get().strip()  # 1.6以后版本使用   原来用 extract_first()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()
            yield item
        if self.offset < 90:  # 判断条件
            self.offset += 10
            url = 'https://maoyan.com/board/4?offset=' + str(self.offset)
            # 把url交给secheduer入队列
            # response会自动传给 callback 回调的 parse()函数
            # Scrapy.request()向url发起请求，并将响应结果交给回调的解析函数
            yield scrapy.Request(url=url, callback=self.parse)
