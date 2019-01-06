## DPL->txt普通 --> made by guihet.com  ##
# @version 1.1.2
def dpltotxt(livepath = '-1'):
    livestr = ''
    fileone = open(livepath, "r" ,encoding="UTF-8")
    filetmp = fileone.read()
    try:
        pa = re.compile(r'file.*?played', re.S)
        fileonelist = pa.findall(filetmp)
        count = 0
        for item in fileonelist:
            title = 'title'
            url = 'url'
            pb = re.compile(r'file.*?\n')
            fileonelistb = pb.findall(item)
            for itemb in fileonelistb:
                zby = re.match(r'file\*(.*?)\n', itemb)
                title = zby.group(1)
            pc = re.compile(r'title.*?\n')
            fileonelistc = pc.findall(item)
            for itemc in fileonelistc:
                zby = re.match(r'title\*(.*?)\n', itemc)
                url = zby.group(1)
            livestr = livestr + title + ',' + url + '\n'
    except Exception as e:
        print('提取DPL文件到字符串，错误！！')
        return '-1'
    return livestr
## END ##