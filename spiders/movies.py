# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request
from time import sleep
from scrapy.loader import ItemLoader
from m80s.items import M80SItem

class MoviesSpider(Spider):
    name = 'movies'
    allowed_domains = ['80s.tw']
    start_urls = ['http://www.80s.tw/movie/list']
    # allowed_domains = ['imdb.com']
    # start_urls = ['http://www.imdb.com/search/title?count=100&release_date=2005,2017&page=1&ref_=adv_nxt']

    def parse(self, response):
        movies = response.xpath('//*[@class="me1 clearfix"]/li/h3/a/@href').extract()
        #imovies = response.xpath('//*[@class="lister-item-header"]/a/@href').extract()
        for movie in movies:
            absolute_url = response.urljoin(movie)
            #print(absolute_url)
            #sleep(0.1)
            yield Request(absolute_url, callback=self.parse_movie)

        #process next page
        #next_page_url =  response.xpath('//*[@class="pager"]/a[text()="下一页"]/@href').extract_first()
        #inext_page_url =  response.xpath('//*[@class="nav"]/*[@class="desc"]/a[text()="Next »"]/@href').extract_first()
        #absolute_text_page_url = response.urljoin(next_page_url)
        #yield scrapy.Request(absolute_text_page_url)

    def parse_movie(self,response):

        title = response.xpath('//h1/text()').extract_first()
        year = response.xpath('//*[@class="info"]/div/span[5]/text()').extract_first()[:4]
        date = response.xpath('//*[@class="info"]/div/span[5]/text()').extract_first()
        country = response.xpath('//*[@class="info"]/div/span[2]/a/text()').extract_first()
        runtime = response.xpath('//*[@class="info"]/div/span[6]/text()').extract_first()
        language = response.xpath('//*[@class="info"]/div/span[3]/a/text()').extract_first()
        genres = response.xpath('//*[@class="info"]/div/span[1]/a/text()').extract()
        genre = response.xpath('//*[@class="info"]/div/span[1]/a/text()').extract_first()
        rate = response.xpath('//*[@id="minfo"]/div[2]/div[2]/span[1]/text()').extract()[2].rstrip()
        img = 'http:' + response.xpath('//*[@class="img"]/img/@src').extract_first()
        #desc = response.xpath('//*[@id="movie_content"]/text()').extract()[1]
        desc = response.xpath('//*[@class="info"]/span/text()').extract_first().lstrip().rstrip()
        downloadurl = response.xpath('//*[@id="myform"]/ul/li[2]/span[3]/a/@href').extract_first()

        # loder = ItemLoader(item=M80SItem(), response=response)
        # loder.add_value('title',title)
        # loder.add_value('year',year)
        # loder.add_value('date',date)
        # loder.add_value('country',country)
        # loder.add_value('runtime',runtime)
        # loder.add_value('language',language)
        # loder.add_value('genres',genres)
        # loder.add_value('genre',genre)
        # loder.add_value('rate',rate)
        # loder.add_value('img',img)
        # loder.add_value('desc',desc)
        # loder.add_value('downloadurl',downloadurl)
        #
        # return loder.load_item()

        yield {
            'title':title,
            'year':year,
            'date':date,
            'country':country,
            'runtime':runtime,
            'language':language,
            'genres':genres,
            'genre':genre,
            'rate':rate,
            'img':img,
            'desc':desc,
            'downloadurl':downloadurl
        }
