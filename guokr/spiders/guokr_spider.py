#encoding:utf-8
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from guokr.items import guokrItem
from guokr.chenge import chengecode

class guokrSpider(CrawlSpider):
	name = "guokr"
	allowed_domains = ["guokr.com"]
	start_urls = [
	"http://www.guokr.com/"
	]
	rules = (
		Rule(LinkExtractor(allow=r"article/439\d+/"),callback='parse_guokr',follow=True),
	)

	def parse_guokr(self,response):		
		item = guokrItem()
		item['url'] = response.url
		item['name'] = response.xpath("//h1[@id='articleTitle']/text()").extract()
		return item
		
