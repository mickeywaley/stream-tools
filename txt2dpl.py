## txt普通->DPL --> made by guihet.com ##
# @version 1.1.2
def dpl():
    filepathname = tkinter.filedialog.askopenfilename(filetypes=[("TXT通用列表","*.txt"), ("列表","*.xspf .m3u"), ("All Files","*")])
    filepath = os.path.dirname(filepathname)
    filenametmp = os.path.splitext(filepathname)[0]
    filename = os.path.split(filenametmp)[1]

    fileexttmp = os.path.splitext(filepathname)[1]
    filetmpbf = '-1'
    if fileexttmp == '.txt':
        fileone = open(filepathname, "r" ,encoding="UTF-8")
        filetmpbf = fileone.read()
    elif fileexttmp == '':
        print("用户取消打开文件")
        return
    else:
        messagebox.showinfo(title='异常',message='文件格式不支持！')
        return
    timenow = datetime.datetime.now().strftime("%m%d%H%M")
    pathdpl = filepath + '/' + filename + '-' + timenow +".dpl"
    filepot = open(pathdpl, 'w', encoding = 'UTF-8')
    filepot.write('DAUMPLAYLIST\n')
    filepot.write('playname=\n')
    filepot.write('topindex=0\n\n')

    filetmp = filetmpbf
    try:
        pa = re.compile(r'.*?,.*?$', re.M)
        fileonelist = pa.findall(filetmp)
        count = 0
        for item in fileonelist:
            zby = re.match(r'^(.*?),(.*?)$', item)
            title = zby.group(1)
            url = zby.group(2)
            filepot.write('%d*file*%s\n' % (count, url))
            filepot.write('%d*title*%s\n' % (count, title))
            filepot.write('%d*played*0\n' % count)
            count += 1
        messagebox.showinfo(title='完成',message='成功写入 dpl 文件！')
    except Exception as e:
        messagebox.showinfo(title='异常',message='写入失败！请检查源文件格式！')
    if fileexttmp == '.txt':
        fileone.close()
    else:
        pass
    filepot.close()
## END ##