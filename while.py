

##循环的嵌套
##for i in range(0,4):
##    print ("i:",i)
##    for q in range(0,5):       ##外循环每执行一次，内循环执行5次
##        print ("q:",q)

for i in range(9):
    for j in range(20):
        print ("*",end ="")
    print ()

"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##不换行
for i in range (1,11):
    print (i,end = "    ")          ##end = "/n"   end = "-"   end = "  "

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##用户输入信息，添加到字典
d = {}
while True :
    key = input("键")
    value = input ("值")
    d[key] = value
    res = input ("是否继续添加，yes/no")
    if res != "yes":
        break
print (d)       

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
## 移动数据到其他列表
l = ["11","qq","wws","ss","xxx","xxx","xxx","xxx","xxx","xxx","xxx"]
##new = []
##当while 中，访问列表是空的时候返回为False，当有数据时返回Ture
##while l :          ##判断列表是否为空还可以写成，len(l)>0 列表长度大于0
##    new.append(l.pop())    ##pop方法弹出最后一个数据并把数据删除（所以移动到新的列表中数据会倒过来）
##print (l)
##print (new)

##删除某个元素
l.remove("xxx")     ##remove 方法只能移除列表中第一个“xxx”的数据，后面的不会再删除
print (l)

while "xxx" in l:   #判断"xxx"是否存在于 l
    l.remove("xxx")   ##删除"xxx"，循环。当"xxx"不存在于l时，退出循环
print (l)


\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#####遍历字典和列表

l = ["11","qq","wws","ss","xxx"]
##for a in l:
##    print (a)

##i = 0
##while i <= len(l)-1:    ##len(l)方法知道整个列表的长度，减一就知道索引位置
##    print (l[i])  ##寻找l列表中的【i（索引位置）】元素，就可以遍历列表了
##    i +=1                 ##自增


b = {"name":"zhangsan","age":11,"2":"3"}
i = 0                    ##i从0开始，索引位置从第一个开始
keylist = list(b.keys()) ##字典b中key的集合，变成列表keylist
##len(keylist)              ##列表长度
while i<len(keylist):        ##i小于列表长度可以写成 i<=len(keylist)-1(索引从0开始，长度减去1)
    key =keylist[i]         ## 把遍历的值赋给key
    value = b[key]         ###知道key后，使用方法查询到值，赋值给values
    print (key ,value)
    i +=1                  ##每次输出完成后，i要加上1，继续循环，直到小于keys列表的长度


##b = {"name":"zhangsan","age":11,"2":"3"}
##i = 0
##keylist = list(b.keys())
##while i <len(keylist) :
##    a = list(b.keys())
##    c = list(b.values())
##    print (a[i],c[i])
##    i +=1
##    

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
####判断奇欧数
##
##while True :
##    a = int (input ("shuru "))
##    if a==0 :
##        break
##    elif a%2 == 0:
##        print("偶数")
##    else :
##        print ("奇数")
##print ("end")  
##

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#############循环的跳出
##he = 0
##a = 1
##while a<101:
##    a = int (input("shuzi "))
##    he +=a
##print (he)

##标志位
##he = 0
##a = -1
##flag = True          ##定义一个标志位，为True。
##while flag:
##    a = int (input("shuzi "))
##    he +=a
##    if a == 0 :             ##当用户输入的数字是0的时候，标志位变成False
##        flag = False
##    
##print (he)

##break
##he = 0          ##定义一个标志位，为True。
##while True:
##    a = int (input("shuzi "))
##    he +=a
##    if a == 0 :             ##当用户输入的数字是0的时候，标志位变成False
##        break
##print (he)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##得出用户输出的整数和，当输入0的时候结束计算，输出结果
he = 0                      
a = -1                            ##定义a的值，让这个循环开始运行，只要不是0就行
while a != 0 :                   ##不是0的时候开始循环，是0的时候结束循环
    a = int(input ("输入"))
    he += a
    print (he)
print ("总和是：",he)
    

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

##计算1~~100的和
##s = (1+100)*50
##print (s)
##

##he = 0                ##定义一个存储的变量，把和赋值和he
##for i in range(1,101):
##    he += i          ##第一次循环he = he+i : he = o+1;第二次he= 1+2；第三次he=3（1+2）+3;..he =（1+2..+99）+100
##print (he)

##he1 = 0   
##i = 1    
##while  i<101:    
##    he1 +=i         ## he1 = he1+i : he1 = 0+1;
##    i +=1          ## i=i+1 :i= 1+1;判断i是否小于101，然后继续循环，第二次he1= 1（he）+2（i）；
##    print (he1)   
##    print (i)
##print (he1)     

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##格式
##while True :       
##    print ("循环体")

##while False :
##    print ("循环体")

##用循环输出1~~10
##方法1
##for a in range(1,11):
##    print (a)
##方法2
##i = 1                 ##i赋值1
##while i<=10 :        ## 条件，当i的值小于或者等于10 
##    print (i)       ##输出i的值，i一开始的值是1，输出为1
##    i += 1          ##i = i+1 第一次循环，到这一步时，i的值是2，进入循环
##    ## i = 2 的时候小于10 ，继续循环，输出2 ，
##    ##然后i+=1的时候，i的值是3，继续循环直到大于10
##print (i)       ##输出循环结束后的值




"""





















