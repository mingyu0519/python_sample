# --*-- coding:utf-8 --*--
import requests
from lxml import etree
import json
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

def spider(url):
    html = requests.get(url)
    area = etree.HTML(html.text)
    content_area = area.xpath('//*[@class="l_post j_l_post l_post_bright  "]')
    for each in content_area:
        jsonData = json.loads(each.attrib["data-field"])
        author = jsonData["author"]["user_name"]
        time = jsonData["content"]["date"]
        # content = each.xpath('')[0]
        print "回帖作者：{0}".format(author)
        print "回帖时间：{0}".format(time)
        # print content.text

spider('http://tieba.baidu.com/p/3522395718?pn=1')
