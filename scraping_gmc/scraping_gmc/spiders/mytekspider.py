import scrapy
import re
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from scrapy.crawler import CrawlerProcess
import pypyodbc as odbc
scraped_products = []
def connection() : 
    DRIVER_NAME = "SQL SERVER" 
    SERVER_NAME = "ryann\SQLEXPRESS" 
    DATABASE_NAME = "gomycode2" 
    connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME}; 
    Trust_Connection=yes; 
    """   
    conn=odbc.connect(connection_string)
    cursor = conn.cursor()
    return conn,cursor


class MytekScraper:
    def __init__(self):
        self.start_url = "https://www.mytek.tn"
        self.seen_products = set()

    def start_scraping(self):
        process = CrawlerProcess()
        process.crawl(self.MytekspiderSpider)
        process.start()

    class MytekspiderSpider(scrapy.Spider):
        name = "mytekspider"
        allowed_domains = ["www.mytek.tn"]
        start_urls = ["https://www.mytek.tn"]
        seen_products = set()
        def parse(self, response):
            categories = response.css('li.rootverticalnav')
            for cat in categories :
                sub_cats = cat.css('.grid-item-6.clearfix')

                for sub_cat in sub_cats :
                    sub_subcats = sub_cat.css('.category-item a')
                    for sub_sub in sub_subcats :
                        name = sub_sub.css('span::text').get()
                        href = sub_sub.attrib['href']
                        yield scrapy.Request(href, callback=self.parse_subcat,meta ={'sub_category' : name })
        def parse_subcat(self,response) :
            category = response.url.split('/')[3]
            #subcat = re.sub(r'\?p=\d+', '', response.url.split('/')[5].replace('.html',''))
            subcat = response.css('.page-title-wrapper ::text').get()
            all_products = response.css('li.product-item')
            with ThreadPoolExecutor(max_workers=4) as executor:
                for prod in all_products :
                    future = executor.submit(self.process_item,prod,category,subcat)
                    yield future.result()
            if(len(response.css('li.pages-item-next')) > 0) :
                next_page = response.css('li.pages-item-next')[0]
                next_page_ee  = next_page.css('a.next::attr(href)').get()
                if next_page_ee is not None :
                    yield response.follow(next_page_ee,callback = self.parse_subcat)
        def process_item(self,prod,category,subcat) :

            product = dict()
            product['category'] = category.lower().strip()
            product['sub_category'] = subcat.lower().strip()
            product['provider'] = 'mytek'
            product['name']=prod.xpath('.//a[@class="product-item-link"]/text()').get()
            #product['category'] = category
            #product['sub_category'] = subcat
            product['reference'] = prod.css('div.skuDesktop::text').get()
            product['image_link'] = prod.css('.product-image-wrapper img::attr(src)').get()
            price_tag = prod.xpath('.//span[@data-price-type="finalPrice"]/span[@class="price"]/text()').get()
            availability_tag = prod.css('div.stock')
            product['availability'] = availability_tag.css('span::text').get()
            #product['price'] = float(price_tag.replace('\xa0DT', '').replace(',','.'))

            if product['name'] :
                res_ref = re.search(r'\[(.*?)\]', product['reference'])
                product['reference'] = res_ref.group(1)
                if res_ref:
                    product['name'] = product['name'].replace(' & ',' ').replace(' / ',' ').replace(" \\ ",' ').replace(' - ',' ').replace(' , ',' ').replace('\n',' ').replace('\r',' ').strip()
                product['reference'] = product['reference'].replace('.','-')
                if(product['reference'].strip().startswith('BU')) :
                    product['reference'] = product['reference'].replace('BU-','')
                product['price'] =float(price_tag.replace('\xa0', '').replace('\u202f', '').replace(',','.').replace('DT',''))
                unwanted_subcategories = ['clavier - souris - tapis', 'clavier & souris', 'souris & tapis', 'clavier - souris - tapis - casque']



                brand_alt = prod.css('.testLp4x.prdtBILCta a img')
                if brand_alt :
                    product['brand'] = brand_alt.attrib['alt']
                else :
                    product['brand'] = None
                old_price = prod.xpath('.//span[@data-price-type="oldPrice"]/span[@class="price"]/text()')
                if(old_price) :
                    product['old_price'] = float(old_price.get().replace('\xa0', '').replace('\u202f', '').replace(',','.').replace('DT',''))

                    product['on_discount'] = True
                else :
                    product['on_discount'] = False
                    product['old_price'] = None
                if (product['reference'], product['name']) not in self.seen_products and product['sub_category'] not in unwanted_subcategories:
                    self.seen_products.add((product['reference'], product['name']))

                    product['name'] = product['name'].strip()
                    scraped_products.append(product)
                    return product


scraper = MytekScraper()
scraper.start_scraping()

df = pd.DataFrame(scraped_products)
df.to_csv("something.csv")
