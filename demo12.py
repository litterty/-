fullname=open('pwdfile.txt',encoding='utf8').readlines()
print(fullname)
for files in fullname:#依次读入列表中的内容
    files = files.lower()   #将文件名全部转化为小写，防止有的用大小写
    if(files[-4:] == 'php\n' or files[-4:]=='jsp\n' or files[-4:]=='asp\n' or files[-5:]=='aspx\n'):  # 将读取文件名字的后三个字符与'php'匹对
        print(files)
        fout = open('pwdfile2.txt', 'a', encoding='utf8')
        fout.write(files)
        fout.close()
