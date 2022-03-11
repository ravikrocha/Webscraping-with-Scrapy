import scrapy


class RogerSpiderSpider(scrapy.Spider):
    name = 'roger_spider'
    allowed_domains = ['www.rogerebert.com']
    start_urls = [f'https://www.rogerebert.com/reviews/page/{i}?filters%5Bno_stars%5D=1&filters%5Breviewers%5D%5B%5D=50cbacd5f3b43b53e9000003&filters%5Bstar_rating%5D%5B%5D=0.0&filters%5Bstar_rating%5D%5B%5D=4.0&filters%5Btitle%5D=&filters%5Byears%5D%5B%5D=1914&filters%5Byears%5D%5B%5D=2022&sort%5Border%5D=newest' for i in range(1,327)]

    def parse(self, response):
        titles = response.xpath("//h5/a")

        for title in titles:
            title_name = title.xpath('.//text()').get()
            link = title.xpath('.//@href').get()

            yield response.follow(url=link,callback = self.parse_title)

    def parse_title(self,response):
        title = response.xpath("//h1[@class='page-content--title']//text()").get()
        review = response.xpath('//section[@class="page-content--block_editor-content js--reframe"]//text()').getall()



        yield{
            'Title': title,
            'Review': review
        }