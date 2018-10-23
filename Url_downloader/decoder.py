from urllib import parse
import requests
'''url = 'http://www.cninfo.com.cn/cninfo-new/disclosure/fulltext/download/1200020704?announceTime=2014-06-30'
cookie = 'cninfo_search_record_cookie=%E6%8A%95%E8%B5%84%E8%80%85%E5%85%B3%E7%B3%BB%E6%B4%BB%E5%8A%A8'
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
host = 'www.cninfo.com.cn'
header = {"User-Agent":useragent,'Referer':url,'Cookie':cookie,'Host':host}
r = requests.get(url)
print(r.headers)'''
print(parse.unquote('%20'))