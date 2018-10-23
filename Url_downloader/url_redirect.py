def url_redirect(url):
    counter = 0
    result = ''
    for i in url:
        if i == '/':
            counter += 1
        if counter == 8 and i!='%':
            result += i
    return 'http://www.cninfo.com.cn/cninfo-new/disclosure/fulltext/download/'+result