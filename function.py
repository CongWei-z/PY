####递归调用，注意限制
####def test():
####    print ("test")
####    test()
####
####test()
####print ("end")
##
#### 计算 f(n) = 1+2+3...+n-1+n \ f(n-1) = 1+2+3...+n-1 \ f(n) = f(n-1)+n 递归
##
##def f(n):            ##当n的值为一的时候返回数字1
##    if n ==1 :      ##递归终止的条件。
##        return 1
##    he = f(n-1)+n       ##递归，函数中继续调用f(n)方法，进行运算，直到n=1的时候，返回1带入
##    return he           ##返回he
####f(5)  
####    he =f(4)+5
####    he =f(3)+4
####    he =f(2)+3
####    he =f(1)+2
####    he =f(0)+1
####    he =f(-1)+0
####    he =f(-2)+-1  .....
##
##
##print (f(5))   #f(5)=f(4)+5 ,f(4)=f(3)+4,f(3)=f(2)+3,f(2)=f(1)+2,f(1)=1 带入
##
####f(5) = f(4)+5 =f(3)+4+5=f(2)+3+4+5 =f(1)+2+3+4+5 =1+2+3+4+5=15
##    


































##import te   ##导入自己定义的整个模块（注：同一个目录下）
##
##te.test1()     ##调用te模块里的test1的方法,需要使用模块名字
##
##调用模块中的某个方法
##from te import test2,test1    ##from 导入te模块里的某一个函数方法
##test2()
##test1()
##给方法起别名
##from te import test2 as new_test,test1 as t1## 导入te模块里的test2方法,as 改名 为new_test
##new_test()

####给模块起别名
##import te as t
##t.test1()

####两种导入方法
##import te
##from te import *     ##导入全部方法函数

##import random








##def test(n,a):                ##创建方法test(n(名字),a（年龄）)
##    d = {"name":n,"age":a}     ##创建一个字典 d，
##    return d                   ##返回字典d的值
##    
##print (test("libai",19))       ##因为有返回值，所以输出这个方法，得到有数据的字典d

##l = ["xx","22","ss","ww"]      
##def test2(l):               ##定义方法，方法里的参数是列表l
##    del(l[1])               ##删除列表里索引为1的元素（“22”）
##
##test2(l[:])                 ##使用了i[:]方法，复制了列表，从而删除的时候不会对原列表产生改变。
####test2(l)                  ##直接在原列表删除索引1的元素
##print (l) 
    
##可变个数的参数
##def test(*n):          ##  *  代表多个,可变参数，在参数前加个 *  ，（0~~无穷）n是个元祖（不可修改）
####    print(n)         ## 带 *  的参数要放在最后
##    for i in n:
##        print (i)
##
####test ()
####test (1)
##test (1,2,3)
##
##test (1,2,3,4,5,6)






##当命名一致时
##name = "全局"
##def  test():
##    name ="局部"
##    print (name)
##test()
##
##print (name)

##def test2():
##    global name    ##使用全局变量，global name
##    name ="局部"   ##把“全局”重新赋值为“局部”
##    print (name)
##test2()   
##print (name)     ##输出name的时候，值就成了“局部”



##局部变量和全局变量(作用域：起作用的地方)

##def test():          ##局部作用域，在一个函数中定义的变量，在函数外是不能使用的。
##    name = "xx"
##    print (name)
##
##test()             ##调用test方法
##print (name)        ##报错      


##name = "libai"          ##全局作用域，全局的变量，是可以在任何地方使用
##def test2():
##    print (name)
##
##test2()   






##关键字参数和位置参数

##print("hello",end = "")  ##end就是关键字字符，把不换行赋值给end
##print("world")
##
##print ("hello","world")        ##每个字符串之间用空格分开
##print ("hello","world",sep = ",")   ##sep是关键字字符，在每个输出的字符之间穿插“，”。
##print ("hello","world",sep = "@@@") ##sep是关键字字符，在每个输出的字符之间穿插“@@@”。
##print ("hello","world",sep = "@@@",end = "")   ##两个关键字参数是可以一起使用的
##print ("hello","world","libai")   

##def add(a,b):
##    print(a+b)
##    
##add(2,3)                #位置参数  规定位置赋值
##add(a=12,b=13)          ##关键字参数
##add(b=12,a=13)         ##关键字参数
##add(2,b=13)            ##关键字参数和位置参数一起使用

##def add(a,b=10):         ##给b传递默认值为10 ，带默认值的一定要定义在后面
##    print(a+b)
##
##
##add(2)              ##b有默认值的时候，调用方法的时候就可不用输入b的值
##add(2,5)            ##当给b赋值的时候，会替换默认值


##def add(a,b=2,c=3):         ##带默认值的一定要定义在后面
##    print(a+b+c)
##
##add(1)
##
##add(1,c=4)  ##当方法里的参数很多，就可以使用关键字参数修改




##none  NoneType       什么都没有，没有值的时候就会有变成none ，
def add(a,b):              
    print (a+b)         ## 没有返回值          

##res = add(3,4)
####print(res)             ##输出的时候会调用a+b的方法，但是没有return返回,所以会输出none

####def add(a,b):                 ##当有返回值的时候也可以直接调用方法，不一定要把返回值调用出来
####     print (a+b)
####     return a+b
####add(1,2)


##def hello(name):                   ##hello函数名（name型参）函数，形参不确定之后会是什么值              
##    print("hello  " + name)
##hello("siki")                     ##调用hello方法，后面加实参（“siki”），实际给的值

####
####def add(a,b):            ##a,b就是这个add函数中的两个参数
####    res = a+b
####    return res           ##返回a+b的值
######    return a+b
####
####a = add(20,9)               ##调用add方法,可以输入的实际参数
####
####print (a)             ##调用add方法，返回的是a+b的值，就是res
####print (add(1,2))




##def add():
##    a = int(input ("yi :"))
##    b = int(input ("yer :"))
##    c = a+b
##    print (c)
##
##add()

 


"""

##def MethodName():   ##MethodName函数名，自己定义 
##    Methodbody      ##  Methodbody函数体

##def test():         ##函数，多次执行的代码写入，执行函数就行
##    print("t1")
##    print("t2")
##
##test()        ##调用写完的函数


print()
len()
input()
list()

"""
