import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.groupon.com/landing/deal-of-the-day']
    start_urls = ['http://www.groupon.com/landing/deal-of-the-day/']

    def parse(self, response):
        products = response.xpath("//div[@class='grpn-dc-caption']")
        for product in products:
            yield{
                "title": product.xpath("//div[@class='grpn-dc-title']").get(),    
                "price": product.xpath("//span[@class='wh-dc-price-discount c-txt-price']").get(),
                "product_sold": product.xpath("//div[@class='grpn-total-ratings']").get()
            }
        pass
