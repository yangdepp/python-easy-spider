from urllib import request
import ssl

context = ssl._create_unverified_context()


class Spider():
    url = 'http://www.panda.tv/cate/lol'

    def __fetch_content(self):
        r = request.urlopen(Spider.url, context=context)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')

    def go(self):
        self.__fetch_content()


spider = Spider()
spider.go()
