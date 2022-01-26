import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        #"https://wordpress.org/news/category/general/",
        #"https://wordpress.org/news/category/community/",
        #"https://wordpress.org/news/category/security/",
        #"https://wordpress.org/news/category/meta/",
        "https://wordpress.org/news/category/newsletter/interviews/",
    ]


    def getContent(self, response):
        title = response.css("h2.fancy a::text").get()
        content = response.css('div.storycontent').get()
        len = content.index('sharedaddy')-13
        content = content[:len]+"</div>"
        yield {
            'title': title,
            'content': content
        }

    def parse(self, response):
        for link in response.css('table.widefat'): 
            links = link.css('a::attr("href")').getall()
            for href in links:
                 yield scrapy.Request(href, callback=self.getContent)
