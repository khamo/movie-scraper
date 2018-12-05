# -*- coding: utf-8 -*-
import scrapy


class CinemaSpider(scrapy.Spider):
    name = "cinema"
    allowed_domains = ['myvue.com']
    start_urls = [
        'http://www.myvue.com/latest-movies/cinema/london-stratford',
    ]

    def parse(self, response):
        movie_names = response.css('.filmListFilmInfo h3 a::text').extract()
        for movie_name in movie_names:
            yield {
                'name': movie_name
            }
