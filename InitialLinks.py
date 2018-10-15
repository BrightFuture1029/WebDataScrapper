# -*- coding: utf-8 -*-
import scrapy


class InitiallinksSpider(scrapy.Spider):
    name = 'InitialLinks'

    def parse(self, response):
        nodes = response.xpath('//*[@id="mc_content"]/section/section/div[1]/div[2]/div/div/div[2]/table/tbody/tr[*]/td[1]/span[1]/a')
        for aNode in nodes:
            yield {
                'ScriptName' : aNode.xpath('./text()').extract_first(),
                'HREF' : aNode.xpath('./@href').extract_first()
            }

