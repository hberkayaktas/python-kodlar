#kütüphaneyi yükleme
# pip install scrapy
import scrapy




class indirimspider(scrapy.Spider):
    name = 'indirim'
    allowed_domains = ['www.akakce.com']
    start_urls = ['https://www.akakce.com/ekran-karti.html']

    def parse(self, response):
        urunler = response.xpath("//*[@id='CPL']/li[1]")
        for urun in urunler:
            yield{
                "title": urun.xpath("//*[@id='CPL']/li[1]/a/span/h3/text()").get(),
                "fiyat": urun.xpath("//*[@id='CPL']/li[1]/a/span/span[2]/span/text()").get(),
                "kac_kisitakip": urun.xpath("//*[@id='CPL']/li[1]/a/span/span[4]/text()").get()
            }

