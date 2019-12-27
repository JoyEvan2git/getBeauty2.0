# -*- coding: utf-8 -*-
import scrapy


class MmgetSpider(scrapy.Spider):
    name = 'mmget'
    start_urls = ['http://plmm.com.cn/xinggan//']

    def parse(self, response):
        r = response.css('.figure>a::attr(href)').extract()
        for href in r:
            try:
                href = response.urljoin(href)
                yield scrapy.Request(href,callback=self.getmm)
            except:
                continue
        next_page = response.css('span#npage>a::attr(href)').extract_first()
        print(next_page)
        if next_page:
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
    def getmm(self,response):
        h1 = response.css('h1::text').extract_first()
        data = {}
        imgs = []
        for img in response.css('a.demo-gallery__img--main::attr(href)').extract():
            img = response.urljoin(img)
            imgs.append(img)
        data[h1] = imgs
        yield data