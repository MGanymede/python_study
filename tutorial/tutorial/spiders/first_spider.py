import scrapy
class MySpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["shzfzl.gov.cn/"]
    start_urls = [
        "https://www.shzfzl.gov.cn/"
    ]
    def parse(self, response):
        filename = "result"
        with open(filename, 'wb') as f:
            f.write(response.body)
        pass

