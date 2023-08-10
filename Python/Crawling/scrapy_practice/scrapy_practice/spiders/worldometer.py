import scrapy

class WorldometersSpider(scrapy.Spider):
    name = 'worldometer'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # a 요소 확인
        countries = response.xpath('//td/a')

        # 반복문
        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # 절대경로
            # absolute_url = f'https://www.worldometers.info/{link}'  # 방법 1
            # absolute_url = response.urljoin(link)  # 방법 2
            # yield scrapy.Request(url=absolute_url)  # sending a request with the absolute url

            # 상대경로
            yield response.follow(url=link, callback=self.parse_country, meta={'country':country_name})

    # Getting data inside the "link" website
    def parse_country(self, response):
 
        country = response.request.meta['country']
        rows = response.xpath("(//table[contains(@class,'table')])[1]/tbody/tr")  
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            # Return data extracted
            yield {
                'country':country,
                'year': year,
                'population':population,
            }





    """ def -2 
    def parse(self, response):

        countries = response.xpath('//td/a')
        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            yield {
                'country_name' : country_name, 
                'link' : link
                            }
    """

    """ def - 1
    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a/text()').getall()

        yield {
            'titles' : title, 
            'countries' : countries,
        }
    """
