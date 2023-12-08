import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["www.dmoz.org"]
    start_urls = ["https://www.dmoz.org"]

    def parse(self, response):
        pass
