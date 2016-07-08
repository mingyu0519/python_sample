# --*-- coding:utf-8 --*--
import requests
from lxml import etree
import json
import sys
import time
from multiprocessing.dummy import Pool as ThreadPool

reload(sys)
sys.setdefaultencoding( "utf-8" )

urls = []

for i in range(1,41):
    newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
    urls.append(newpage)

def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    content_area = selector.xpath('//div[@id="j_p_postlist"]/div[@class="l_post j_l_post l_post_bright  "]')
    for each in content_area:
        jsonData = json.loads(each.attrib["data-field"])
        author = jsonData["author"]["user_name"]
        time = jsonData["content"]["date"]
        content = each.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')[0]
        # print "回帖作者：{0}".format(author)
        # print "回帖时间：{0}".format(time)
        # print "回帖内容：{0}".format(content)

time1 = time.time()
for i in urls:
    spider(i)
print "单线程耗时：{0}".format(time.time()-time1)

time3 = time.time()
pool = ThreadPool(4)
time3 = time.time()
results = pool.map(spider, urls)
pool.close()
pool.join()
time4 = time.time()
print u'并行耗时：' + str(time4-time3)
