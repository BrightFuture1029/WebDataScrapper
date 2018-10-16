# -*- coding: utf-8 -*-
import scrapy
import json

class ExtractscriptdetailSpider(scrapy.Spider):
    name = 'ExtractScriptDetail'

    def start_requests(self):
        with open('InitialLinks.json','r') as infile:
            contents = json.load(infile)
        i = 0

        for item in contents:
            yield scrapy.Request(url=item['HREF'], callback=self.parse)
            #i = i + 1
            if i == 10: 
                break

    def parse(self, response):
        headerDetail = response.xpath('//*[@id="nChrtPrc"]/div[4]/div[1]')
        HL52 = response.xpath('//*[@id="content_bse"]/div[3]/div[2]/div[2]')
        metaNode = response.xpath('//*[@id="mktdet_2"]')
        yield {        
        'BSE' : headerDetail.xpath('./text()[1]').extract_first().split(':')[1].strip(),
        'NSE' : headerDetail.xpath('./text()[2]').extract_first().split(':')[1].strip(),
        'ISIN' : headerDetail.xpath('./text()[3]').extract_first().split(':')[1].strip(),
        'Sector' : headerDetail.xpath('./a/text()').extract_first(),
        'Low52' : HL52.xpath('./*[@id="b_52low"]/text()').extract_first(),
        'High52' : HL52.xpath('./*[@id="b_52high"]/text()').extract_first(),        
        'MCap' : metaNode.xpath('./div[1]/div[1]/div[2]/text()').extract_first(),
        'PE' : metaNode.xpath('./div[1]/div[2]/div[2]/text()').extract_first(),
        'BookValue' : metaNode.xpath('./div[1]/div[3]/div[2]/text()').extract_first(),
        'IndustryPE' : metaNode.xpath('./div[1]/div[6]/div[2]/text()').extract_first(),
        'PriceToBookRatio' : metaNode.xpath('./div[2]/div[3]/div[2]/text()').extract_first(),                                
        'PToCRatio' : metaNode.xpath('./div[2]/div[2]/div[2]/text()').extract_first().strip(),
        'EPSTTM' : metaNode.xpath('./div[2]/div[1]/div[2]/text()').extract_first().strip(),
        'DivYield' : metaNode.xpath('./div[2]/div[4]/div[2]/text()').extract_first(),
        'FaceValue' : metaNode.xpath('./div[2]/div[5]/div[2]/text()').extract_first()
         }
        
        
        
        
        class FinancialSnap(scrapy.Item):
    name1 = scrapy.Field()
    name2 = scrapy.Field()
    name3 = scrapy.Field()
    name4 = scrapy.Field()
    name5 = scrapy.Field()

class ExtractscriptdetailSpider(scrapy.Spider):
    name = 'ExtractScriptDetail'

    start_urls = ['https://www.moneycontrol.com/india/stockpricequote/ceramicsgranite/divyashaktigranites/DG02',
                  'https://www.moneycontrol.com/india/stockpricequote/refineries/hindustanpetroleumcorporation/HPC']    
#    def start_requests(self):
#        with open('D:/Dhiraj/Python/MCDTest/InitialLinks.json','r') as infile:
#            contents = json.load(infile)
#        i = 0
#
#        for item in contents:
#            yield scrapy.Request(url=item['HREF'], callback=self.parse)
#            i = i + 1
#            if i == 10: 
#                break

    def parse(self, response):
        headerDetail = response.xpath('//*[@id="nChrtPrc"]/div[4]/div[1]')
        HL52 = response.xpath('//*[@id="content_bse"]/div[3]/div[2]/div[2]')
        metaNode = response.xpath('//*[@id="mktdet_2"]')        
        tab = response.xpath('//*[@id="findet_1"]/table')
        rows = tab.xpath('.//tr')
        a = dict()
        
        for c in rows[0].xpath('.//td')[1:]:
                a[c.xpath('.//text()').extract_first()] = FinancialSnap()

        c1 = rows[0].xpath('.//td')[1:]
        rr = 1
        for r in rows[1:]:
            cols = r.xpath('.//td')
            cc = 0
            for c in cols[1:]:
                a[c1[cc].xpath('.//text()').extract_first()]['name' + str(rr)] = c.xpath('.//text()').extract_first()
                cc = cc+1
            rr = rr + 1
        

        yield a
        #result.extend({cols[0].xpath('./text()').extract_first() : c.xpath('./text()').extract_first()})
        #yield dict(result)
        #print(result)
        
        #yield {cols[0].xpath('./text()').extract_first() : c.xpath('./text()').extract_first()}

        #yield {        
        #'BSE' : headerDetail.xpath('./text()[1]').extract_first().split(':')[1].strip(),
        #'NSE' : headerDetail.xpath('./text()[2]').extract_first().split(':')[1].strip(),
        #'ISIN' : headerDetail.xpath('./text()[3]').extract_first().split(':')[1].strip(),
        #'Sector' : headerDetail.xpath('./a/text()').extract_first(),
        #'Low52' : HL52.xpath('./*[@id="b_52low"]/text()').extract_first(),
        #'High52' : HL52.xpath('./*[@id="b_52high"]/text()').extract_first(),        
        #'MCap' : metaNode.xpath('./div[1]/div[1]/div[2]/text()').extract_first(),
        #'PE' : metaNode.xpath('./div[1]/div[2]/div[2]/text()').extract_first(),
        #'BookValue' : metaNode.xpath('./div[1]/div[3]/div[2]/text()').extract_first(),
        #'IndustryPE' : metaNode.xpath('./div[1]/div[6]/div[2]/text()').extract_first(),
        #'PriceToBookRatio' : metaNode.xpath('./div[2]/div[3]/div[2]/text()').extract_first(),                                
        #'PToCRatio' : metaNode.xpath('./div[2]/div[2]/div[2]/text()').extract_first().strip(),
        #'EPSTTM' : metaNode.xpath('./div[2]/div[1]/div[2]/text()').extract_first().strip(),
        #'DivYield' : metaNode.xpath('./div[2]/div[4]/div[2]/text()').extract_first(),
        #'FaceValue' : metaNode.xpath('./div[2]/div[5]/div[2]/text()').extract_first()
        # }
