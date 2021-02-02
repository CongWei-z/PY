import os
##print(os.getcwd())   ##工作目录
##
##os.chdir("c:\\Windows")  ##修改工作目录
##print(os.getcwd()) 
##print(os.getcwd())

##os.makedirs("xx1/xx2")  ##在当前工作目录里创建文件夹
##print(os.getcwd())
##os.makedirs("C:/Users/zhangyinghao/Desktop/py/xx3")##绝对路径创建文件夹

##with open('game.txt',encoding="utf-8") as file: ##默认读取文件
##    c = file.read()
##    
##    print(c)

##with open('game.txt',encoding="utf-8") as file:
##    for line in file:
##        print(line.rstrip())        #角色\n ,  print 自带换行 rstrip消除换行


##with open("game.txt",encoding="utf-8") as file:
##    l = file.readlines()         ##file里的方法.readlines，把读取的数据变成列表
##for i in l:
##    print(i.rstrip())
##


##with open("game.txt","w",encoding="utf-8") as file:   ##“w”写入覆盖 
##    file.write("www.baidu.com")

##with open("game.txt","a",encoding="utf-8") as file:   ##“ “a” append,在文字末端追加字符串
##    file.write("\n66666666")  ##添加\n换行
##   

##with open('game.txt',"r",encoding="utf-8") as file: ##读取文件 
##    print(file.read())

##异常处理
##print(2+"sda")


try:                ##当不出现异常时候正常输出
##    print(2+"sda")
    print(2+2)
except TypeError:
    print("异常了")
##else:             
##    print("")

print("end")















