#coding:utf-8
import sys
import base64
import time

#使用方法  python tobase64  源文件名.txt 目标文件名.txt

def tobase6(usernamefile,uf64file):
    start = time.clock()
    uf = open(usernamefile)
    uf64 = open(uf64file,'w')
    uf64 = open(uf64file,'a')
    for x in uf:
        line = uf.readline()
        res = line.strip("\r\n")
        res = res.encode("utf-8")
        base64name = base64.b64encode(res)
        uf64.write(base64name.decode("utf-8") + "\n")
        #print(base64name.decode("utf-8"))
    uf.close()
    end = time.clock()
    print(end-start)
    # start = time.clock()
    # uf = open(usernamefile)
    # lines = uf.readlines()
    # for line in lines:
    #     line = line.strip()
    # uf.close()
    # end = time.clock()
    # print(end-start)

    # start = time.clock()
    # uf = open(usernamefile)
    # line = 1
    # while line:
    #     line = uf.readline()
    #     line = line.strip("\r\n")
    #     print (line)
    # uf.close()
    # end = time.clock()
    # print(end-start)

    #f = open('2.txt', 'a')
    #for i in range(500000):
    #    i = str(i)
    #    f.write(i + "\n")
    #f.close()
if __name__ == "__main__":
    tobase6(sys.argv[1],sys.argv[2])
#使用方法  python tobase64  源文件名.txt 目标文件名.txt