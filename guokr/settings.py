# -*- coding: utf-8 -*-

# Scrapy settings for guokr project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'guokr'

SPIDER_MODULES = ['guokr.spiders']
NEWSPIDER_MODULE = 'guokr.spiders'
ITEM_PIPELINES = {
	'guokr.pipelines.GuokrPipeline'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'guokr (+http://www.yourdomain.com)'
