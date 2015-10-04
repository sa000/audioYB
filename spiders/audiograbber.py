# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from audioYB.items import AudioybItem
import re
import youtube_dl   
class audioYBSpider(scrapy.Spider):
    name = "audioYB"
    allowed_domains = ["youtube.com"]
    start_urls = (
        'https://www.youtube.com/playlist?list=PLbFrQnW0BNMURpRox1K0buigypjtCvAlE',
    )

    def parse(self, response):
        hxs=HtmlXPathSelector(response)
        print "bitch"
        links= hxs.xpath('//*[@id="pl-load-more-destination"]/tr/td/a')
        for link in links:
            item=AudioybItem()
            name=link.xpath('text()').extract()
            wlink=link.xpath('@href').extract()
            #item=ClassItem()
            #item['major']=re.compile('>(.*?)<').search(major).group(1)
            #item['urlLink']=re.search('\w*\.html', major).group(0)
            #urlLink=re.search('\w*\.html', major).group(0)
            youtubelink='http://www.youtube.com'+wlink[0]
            print 'hello'
            item['yblink']=str(youtubelink)
            item['ybname']=name
            print name
            print "READ ME"
            print youtubelink
            yield item
        





