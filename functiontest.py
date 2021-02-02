##def display_message():
##    print ("句子")
##
##display_message()
##
##def favorite_book(title):
##    print ("my fav book is ",title)
##
##favorite_book("简")


##def make_shirt(size,zi):
##    print ("大小是",size,"ziyangshi",zi)
##
##make_shirt("L","红色")
##make_shirt(size="L",zi="红色")


##def make_shirt(size,zi="i love pyth"):
##    print ("大小是",size,"ziyangshi",zi)
##
##make_shirt("L")
##make_shirt(size="zhong")
##make_shirt(size="zhong",zi="8888888888")

##def des_city(cs,guojia="zhongg "): ##有默认值的要放在最后
##    print (cs,"in",guojia)
##
##des_city("hangzhou")
##des_city("shenghai")
##des_city("beijing")
##des_city("shouer","hanghuo")

##
##def city_country(name,country):
##    return name+"在"+country
##    
##print(city_country("北京","中国"))


##def make_album(name,zj_name,song_number=0):
##    i ={}
##    i["name"] = name
##    i["zj_name"] = zj_name
##    if song_number!=0 :
##        i["song_number"] = song_number
##    return i
##
##print(make_album("周杰伦","稻香"))
##print(make_album("周杰伦","稻香","5"))


####def long_inp():
####    a = str(input("输入："))
####    b = len(a)
####    if b<6 :
####        print ("小于5个字符")
####    else:
####        print ("大于5个字符")
####
####long_inp()


##def long_inp(a):
##    
####    if len(a)>5:
####        return True
####    else:
####        return False
##    return len(a)>5
##print (long_inp([1,3]))




##s ='www.baidu.com'
##for i in s:
##    print(i)
##


##def t1(t):
##    i = False
##    for s in t :             ##遍历所有元素
##        if s.strip()=="":    #strip方法查看所有元素前后是否有空格，\n,\t
##            i=True
##            break
##    return i
##
##print (t1("daad"))
##    
        


##str = "    eee eee eee    ee"
##print(str.strip(""))



##def t2(t):
##    while len(t)>2:  #循环：当长度大于2的时候，做删除，删除第3个字符
##        del(t[2])
##    return t
##
##i =["22","11","aa","ss","dd"]
##t2(i)
##print(i)


    
##    lenght=len(t)
##    if lenght>3:
##        q=t[0:2]
##    else:
##        return False
##    return q
##print(t2("12"))


##def t3(t):
##    newl = []
##    for i in range(0,len(t)):  #遍历列表的长度
##        if i%2==1:                       #索引值求余数，余数为1 ，为奇数
##            newl.append(t[i])       #把索引是奇数的添加到新的列表
##    return newl
####    q = []
####    q=(t[1::2])
####    return q
##
##a=["22","qq","ww","ee","rr"]
##print (a)
##print (t3(a))


##t=["22","qq","ww","ee","rr"]
##print(t[::2])




##def t4(d):
##    for k in d.keys():  #遍历字典d的所有key
##        v=d[k]         
##        if len(v)>2: 
##            d[k] = v[0:2] 
##    return d
##
##print(t4({"name":"libai","hobby":["play","do","no"]}))


  
#斐波那契数列F[n]=F[n-1]+F[n-2](n>=3,F[1]=1,F[2]=1)
# 1 1 2 3 5 8 11 19....后面的数是前面两个数的和

##def f(n):
##    if n==1 or n ==2:
##        return 1
##    res = f(n-1)+f(n-2)
##    return res
##print (f(5))






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
##    return he            ##返回he
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























