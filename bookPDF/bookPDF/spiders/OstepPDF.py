import scrapy
from bookPDF.items import BookpdfItem


class PDFSpider(scrapy.Spider):
    name = 'pdf'

    start_urls = ['http://pages.cs.wisc.edu/~remzi/OSTEP/']

    def parse(self, response):

        trs = response.css('tr td')

        # 加入0页
        item0 = BookpdfItem()
        item0['title'] = '0'
        item0['file_urls'] = ['http://pages.cs.wisc.edu/~remzi/OSTEP/preface.pdf']
        yield item0
        for link in trs:
            title = str(link.css('small::text').extract_first()).strip()
            if title.isdigit():
                url = 'http://pages.cs.wisc.edu/~remzi/OSTEP/' + link.css('a::attr(href)').extract_first()
                # 3这里有个小bug 修复即可
                if title == '3':
                    url = 'http://pages.cs.wisc.edu/~remzi/OSTEP/dialogue-virtualization.pdf'
                item = BookpdfItem()
                item['title'] = title
                item['file_urls'] = [url]
                yield item
