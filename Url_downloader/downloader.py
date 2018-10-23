import requests
from urllib import parse
def run(File):
    file = open(File)
    while 1:
        lines = file.readlines(1000)
        if not lines:
            break
        for line in lines:
            get_down(line)
def get_down(url):
    flag = -1
    raw_name = ''
    r = requests.get(url)
    raw = r.headers.__getitem__('Content-disposition')
    for i in raw:
        if flag == 1:
            raw_name += i
        if i=='"':
            flag = 1
    file_name = parse.unquote(raw_name[:-1])
    with open(file_name, "wb") as code:
        code.write(r.content)
        code.close()
    print(file_name+" 下载完成")
run('1.txt')