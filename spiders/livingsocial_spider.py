from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import LivingSocialDeal

class LivingSocialSpider(BaseSpider):
    """Spider for regularly updated livingsocial.com site, San Francisco page """
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["http://www.livingsocial.com/cities/15-san-francisco"]

    deals_list_xpath = '//li[@dealid]'
    item_fields = {'title': './/a/div[@class="deal-bottom"]/h3[@itemprop]/text()',
                       'link': './/a/@href',
                       'description': './/a/div[@class="deal-bottom"]/p/text()',
                       'category': './/a/div[@class="deal-top"]/div[@class="deal-category"]/span/text()',
                       'location': './/a/div[@class="deal-top"]/ul[@class="unstyled deal-info"]/li/text()',
                       'original_price': './/a/div[@class="deal-bottom"]/ul[@class="unstyled deal-info"]/li[@class="deal-original"]/del/text()',
                       'price': './/a/div[@class="deal-bottom"]/ul[@class="unstyled deal-info"]/li[@class="deal-price"]/text()'}

