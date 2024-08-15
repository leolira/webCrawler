import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector

class MySpiderSpider(scrapy.Spider):
    name = "my_spider"
    allowed_domains = ["blogbbm.com"]
    start_urls = ["https://blogbbm.com/manga/"]

    def parse(self, response):

        soup = BeautifulSoup(response.text, 'html.parser')
        manga_titles = []

        lines = soup.find_all('tr')

        links=[]

        def get_links(lines):
            for line in lines:
                links.extend(line.find_all('a', href=lambda href: href.startswith('https://blogbbm.com/manga/')))
            return(links)

        links = get_links(lines)

        def get_manga_titles(links):
            for link in links:
                manga_titles.append(link.text)
            return(manga_titles)
        
        manga_titles = sorted(get_manga_titles(links))
  
        for manga in manga_titles:
            item = {
                'title':manga
            }
            yield item