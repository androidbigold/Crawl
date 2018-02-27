
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from Crawl.items import News


class NewsSpider(CrawlSpider):
    name = "News"
    allowed_domains = ["sports.sina.com.cn", "sports.sohu.com"]
    start_urls = ["http://sports.sina.com.cn/", "http://sports.sohu.com/"]
    rules = {
        Rule(LinkExtractor(allow=('http://sports.sina.com.cn/.*/doc-ifyhrxsk\d*.shtml',)), callback='sina_parse'),
        Rule(LinkExtractor(allow=('http://sports.sohu.com/\d*/[n]\d*.shtml',)), callback='sohu_parse'),
    }

    def sina_parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//head')
        items = []
        for site in sites:
            item = News()
            item['title'] = site.xpath('title/text()').extract()
            item['url'] = site.xpath('meta[@property="og:url"]/@content').extract()
            item['img'] = response.selector.xpath('//figure[@class="article-a__figure"]/img/@src').extract()
            item['content'] = response.selector.xpath('//div[@class="article-a__content"]/p/text()').extract()
            items.append(item)
        return items

    def sohu_parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//head')
        items = []
        for site in sites:
            item = News()
            item['title'] = site.xpath('title/text()').extract()
            item['url'] = site.xpath('link[@rel="canonical"]/@href').extract()
            item['img'] = response.selector.xpath('//table[@class="tableImg"]//tbody/tr/'
                                                  'td[@style="text-align: center;"]/img/@src').extract()
            item['content'] = response.selector.xpath('//div[@itemprop="articleBody"]/p/text()').extract()
            items.append(item)
        return items
