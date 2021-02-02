##print ("hello,world")
##
##a = int(input("第一个数字"))
##b = int(input("第2个数字"))
##c = a+b
##print(c) 


##import cmath
##
##a = int(input("第一个数字"))
##a_sqrt = cmath.sqrt(a)
##print(a_sqrt)


##import random
##print(random.randint(0,9))

##a = int(input("数字:"))
##
##if a>1:
##    for i in range(2,a):
##        if a%i==0:
##            print ("bushisushu")
##            break
##    else:
##        print("shi")
##else:
##    print("请输入大于1的数")


##
##a = int(input("数字:"))
##
##for j in range(0,a+1):
##    if j>1:
##        for i in range(2,j):
##            if j%i==0:
##                break
##        else:
##            print(j)
##                
   

##max1 = int(input("max:"))
##min1 = int(input("min:"))
##
##for i in range(min1,max1+1):
##    if i >1:
##        for j in range(2,i):
##            if i%j==0:
##                break
##        else:
##            print(i)
        

##for i in range (1,10):
##    for j in range(1,i+1):
##        print ("%d*%d=%d" %(i,j,i*j),end = "  ")
##
##    print()

##for i in range(1,10):
##    for j in range(1,i+1):
##        print(i,'*',j,'=',i*j,end = "")
##
##    print()







##def n(num):
##    num = int(input("数字"))
##    factorial=1
##    for i in range(1,num + 1):
##        factorial *=i
##
##    return factorial
##        
##
##
##print(n(4))


##while True:
##    a = input("数字：")
##    if str(a) == "quit":
##        break
##print(max(a))


##while True:




##while True:
##    n = int(input("shu"))
##    for i in range(0,n):
##
##        for j in range(0,n-1):
##            print ("*",end = " ")
##        print ("*")
##        



##n = int(input("shu"))
##
##for i in range(1,n+1):
##    if i%2==0:
##        print(i)
##

##while True :
##    n = int(input("shu"))
##    i = 1
##    Res = 0
##    while i<n :
##        if i % 2 == 1:
##            Res += i
##            i+=2
##    print(Res)

##13579

##for i in range(1,10):
##    for j in range(1,i+1):
##        print (j,"*",i,"=",i*j,end= " ")
##    print ()
##    



##def a(x,y):
##    if x>y:
##        ys=x
##    else:
##        ys=y
##    for i in range(1,ys+1):
##        if x%i==0 and y%i ==0:
##            a=i
##    return a
##
##
##print(a(1000,2000))
##


##最小公倍数
##def a (x,y):
##    if x>y:
##        bs=x
##    else :
##        bs = y
##    while True :
##        if bs%x == 0 and bs%y == 0:
##            a=bs
##            break
##        bs +=1
##    return a
##
##print(a(9,3))

def a (x,y):
    if x>y:
        bs = x
    else :
        bs = y
    while True :
        if bs%x == 0 and bs%y == 0:
##            a=bs
            break
        bs +=1
        print (bs)
    return bs

print(a(2,3))

        
##def add(x,y):
##    return x+y
##        
##def jian(x,y):
##    return x-y
##        
##def cheng(x,y):
##    return x*y
##        
##def chu(x,y):
##    return x/y
##
##print("选择算法：")
##print("1、加")
##print("2、减")
##print("3、乘")
##print("4、除")
##
##
##
##while True:
##    q = int(input("输入编号"))
##    if q<4 and q>0:
##        w = int(input("输入第一个数字"))
##        e = int(input("输入第二个数字"))
##    else:
##        print("输入错误，重新输入")
##        
##    if q==1:
##        print("和是",add(w,e))
##        break
##    elif q==2:
##        print("和是",jian(w,e))
##        break
##    elif q==3:
##        print("和是",cheng(w,e))
##        break
##    elif q==4:
##        print("和是",chu(w,e))
##        break


    













            

