import os

def get_filelist(dir):
    for home,dir,files in os.walk(dir):
        for filename in files:
            fullname = os.path.join(home, filename)
            fout = open('pwdfile.txt', 'a', encoding='utf8')
            fout.write(fullname+'\n')
            fout.close()
if __name__ == "__main__":
    ml = os.getcwd()
    get_filelist(ml)