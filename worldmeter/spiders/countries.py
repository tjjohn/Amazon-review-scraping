import scrapy

class CountriesSpider(scrapy.Spider):    # spider class
    name = 'countries'
    allowed_domains = ['www.amazon.in']  #  never add http
    start_urls = ['https://www.amazon.in/Redmi-Sky-Blue-64GB-Storage/product-reviews/B08697N43N/']   # add https


    def parse(self, response):  # parse method to get response from spider
        
        
        for i in response.css("[data-hook=review]"):     #attibute name and its value******
           items={}  #dictionary
              
           items['title']=i.css('[data-hook="review-title"] span ::text').get()     #extracting data from selector object
           items['review']=i.xpath('normalize-space(.//*[@data-hook="review-body"])').get()   #remove space by normalising 
           items['star']=i.css('[data-hook="review-star-rating"] span ::text').get()
           items['name']=i.css('.a-profile-name ::text').get()
            
           yield items

           next_page = response.xpath('//a[contains(text(),"Next page")]/@href').get()
           if next_page:
            yield scrapy.Request(response.urljoin(next_page))
            
