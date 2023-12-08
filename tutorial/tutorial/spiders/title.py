import scrapy


class TitleSpider(scrapy.Spider):
    name = "title"
    # 要抓取数据的网站域名
    allowed_domains = ["c.biancheng.net"]
    # 第一个抓取的url，初始URL，被当做队列来处理
    start_urls = ["https://c.biancheng.net"]

    def parse(self, response):
        result = response.xpath('/html/head/title/text()').extract_first()
        print('-' * 30)
        print(result)
        print('-' * 30)
