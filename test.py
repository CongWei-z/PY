
##n = int(input("请输入一个正整数n:"))
##if n < 2:           #判断是否大于1的整数，且1不是素数
##    print("%d不是素数！"%n)
##else:
##    for i in range(2,n):
####        print ("i:",i)
####        print ("n:",n)
##        if n % i == 0:    #判断2——i是否有能被整除
##            print("%d不是素数！"%n)
##            print(i)
##            break
##        print("%d是素数！"%n)

##
##while True :
##    n = int(input("请输入一个正整数n:"))
##    for i in range(2,n):
##        if n%i == 0:
##            print ("bushisushu")
##            break
##    if n==i+1:
##        print ("shi sushu ")

##
##Number = int(input("请输入一个数字："))         # 输入一个正整数，并赋值给Number
##if Number > 1:                                 # 判断输入的正整数是否大于1
##    for i in range(2,Number):                  # 循环取出2至Number-1的正整数 i
##        if Number % i == 0:                    # 将Number与i取余，如果余数为0 ，则就可以被整除
##            print ("数字%s不是素数" % Number)
##            break                              # 不是素数，结束循环
##    else:
##        print("数字%s是素数" % Number)           # 否则就是素数，打印结果
##else:
##    print("输入的数字小于1，不合法")

##for i in range(0,6):
##    for j in range(0,20):
##        print ("*",end="")
##    print()
        

#\\\\\\\\\\\\\\\\\\\\##%s 和 %d 的用法 (s字符，d数值类型)
##a = int(input("第一个字符"))
##b = int(input("第er个字符"))
##print ('%d plus %d equals %d' % (a,b,a+b) )
##a = str(input("第一个字符"))
##b = str(input("第er个字符"))
##print ('%s plus %s equals %s' % (a,b,a+b) )

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##99乘法表
##for i in range(1,10):
##    for j in range(i,10):
####        print ("i:",i)
####        print ("j:",j)
##        print ("%d*%d=%d" %(i,j,i*j),end = "   ")
##       # print(i,"*",j,"=",i*j,end="   ")
##    print ()
####




##age = int (input("输入年龄"))
##if age <=3 :
##    print ("婴儿")
##elif age <=10 :
##    print ("小孩")
##elif age <=18 :
##    print ("少年")
##elif age <=40 :
##    print ("青年")
##elif age <=60 :
##    print ("壮年")
##else :
##    print ("老年")

####交换两个变量里的数据，创建一个临时变量，把b的值给temp,再把a的值给b，再把temp的值给a
##a = 10
##b = 5
##temp = b
##b = a
##a = temp
##print (a,b)



##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\三个数字比大小
##a = int(input ("第一个数字"))
##b = int(input ("第二个数字"))
##c = int(input ("第三个数字"))
##l = []
##l.append(a)
##l.append(b)
##l.append(c)
##l.sort()
##print (l)


##a = int(input ("第一个数字"))
##b = int(input ("第二个数字"))
##c = int(input ("第三个数字"))
##
##if a>b>c :
##    print (c,b,a)
##elif a>c>b :
##    print (b,c,a)
##elif c>a>b :
##    print (b,a,c)
##elif c>b>a :
##    print (a,b,c)
##elif b>c>a :
##    print (a,c,b)
##else :
##    print (c,a,b,)
##
##import  random                            ##import导入随机生成数字模块
##
##while True :
##    s = random.randint(0,20)
##    print (s)
##    if s==20:
##        break
##while True :
##    num = int(input("数字:"))
##    if num>s:
##        print ("大了")
##    elif num<s:
##        print ("小了")
##    else:
##        print ("ok")
##        break

##a = int(input ("第一个数字"))
##b = int(input ("第二个数字"))
##c = int(input ("第三个数字"))
##if a>b:                             ##如果a>b,那么把a的值赋予b  
##    temp = b
##    b = a  
##    a = temp
##if b>c:                          ##如果b>c,那么把b的值赋予c  (b和c相比，c一定是最大的)
##    temp = c
##    c = b
##    b = temp
##if a>b:                           ##如果a>b,那么把a的值赋予b(现在的b里的数是c，就是c和a相互比较)
##    temp = b
##    b = a 
##    a = temp
##print (a,b,c)
##
##
##
##
####\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##z = float(input ("第一条边"))
##x = float(input ("第二条边"))
##v = float(input ("第三条边"))
##
##if z+x>v and z+v>x and x+v>z :
##    print ("yes")
##else :
##    print ("no")


##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\0~~20 猜数字
##import  random                            ##import导入随机生成数字模块
##s = random.randint(0,20)
##for i in range(4):                  ##循环4次
##    num = int (input ("输入一个数字"))
##    if num>s :
##        print ("数字偏大")
##    elif num<s :
##        print ("数字偏小")
##    else :
##        print ("恭喜")
##        break
##print ("游戏结束")

















    
