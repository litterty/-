import time
import base64

files1 = open('pwdfile2.txt',encoding='utf8').readlines()  #将里面文件的文件路径放入列表
print(files1)
all_dict = ['system','exec','passthru','shell_exec','ob_start','eval','assert','preg_replace','array_map','equals','request','execute']   #检测关键字
all_b64dict = []
for b in all_dict:
    b = base64.b64encode(b.encode('utf-8')).decode('ascii')  #进行base64编码转换，顺便消除前面的b
    all_b64dict.append(b)
print(all_b64dict)
for fo in files1:
    fo = fo.strip('\n')    #去掉文件路径最后面的\n
    with open(fo) as fo2:
        all_text = fo2.read()
        all_text = "".join(all_text.split())  #去掉所有空格
        all_text = all_text.lower()    #转化为小写
        print(all_text)
        for bi in all_dict:
            results = bi in all_text  #与关键字规则进行比较
            if results == True:
                print(fo)          #返回结果
                jg = open('jcjg.txt', 'a', encoding='utf8')
                jg.write(fo + '\n')   #写入jcjg.txt文件
                jg.close()
        for bo in all_b64dict:         #base64编码后检测
            results = bo in all_text
            if results == True:
                print(fo)
                jc = open('jcjg.txt', 'a', encoding='utf8')
                jc.write(fo + '\n')   #写入jcjg.txt文件
                jc.close()
print(time.asctime())
t = open('jcjg.txt', 'a', encoding='utf8')  #写入时间
t.write("运行时间为："+time.asctime() + '\n')   #写入jcjg.txt文件
t.close()