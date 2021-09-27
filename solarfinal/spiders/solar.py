import scrapy
from ..items import SolarfinalItem


class SolarSpider(scrapy.Spider):
    name = 'solar'
    custom_settings = {

        'DOWNLOAD_DELAY': 5,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 16,
        'CONCURRENT_REQUESTS_PER_IP': 16,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 5,

    }
    page_number = 2

    def start_requests(self):
        for i in range(5):
            yield scrapy.Request(url='https://www.enfsolar.com/directory/installer/United%20States?i=' + str(i))

    def parse(self, response):
        for link in response.css(".enf-list-table a::attr(href)"):
            yield response.follow(link.get(), callback=self.parse_categories)

    def parse_categories(self, response):
        items = SolarfinalItem()
        details = response.css('div.enf-company-profile-info-main.pull-left')
        for detail in details:
            company_name = details.css('h1.blue-title::text').get().strip()
            company_website = details.css(
                'table~ table+ table a::attr(href)').get()

            items['company_name'] = company_name
            items['company_website'] = company_website
            yield items

        next_page = 'https://www.enfsolar.com/directory/installer/United%20States?page=' + str(
            SolarSpider.page_number) + ''
        if SolarSpider.page_number <= 71:
            SolarSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
