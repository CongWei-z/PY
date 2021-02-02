##z = {"name":"zhangsan ","age ":19,"hobby":"play","xb":"难"}
##
##print (z.keys())
##print (z.values())
##print (z.items())
##
##key = list(z.keys())
##print (key)




##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##判断字典里是否存在某个值或是键（返回的是布尔类型（True/False））
#stu1 = {'name':'zhangsan','ages':'18','gender':'男'}
##res1 = 'gender' in stu1.keys()  ##'gender'是否是stu1的字典里的键：使用keys（）方法，调出stu1里的键的合集
##print (res1)                     ##输出True
##res2 = 'gender' not in stu1.keys()
##print (res2)
##res3 = 'zhangsan' in stu1.values()
##print (res3)
##
##res4 = 'gender' in stu1    ##不写keys/values时，默认判断的是keys
##print (res4)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##检查key是否存在,输出的时候不会报错
##stu1.setdefault('name','xixi')    ##当key的值存在：name是key值，那么name里原来是zhangsan，xixi不会覆盖zhangsan。
##print (stu1['name'])             ## 输出原先的值（zhangsan），表示字典里存在name这个键
##stu1.setdefault('hobby','qq')   ##当key的值不存在：hobby是key值，hobby不存在与字典中，那么就会给hobby的值存储一个数据“qq”
##print (stu1['hobby'])          ## 输出创建的值“qq”，表示字典中不存在hobby这个键


##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##遍历字典的三种方式（1、key, 2. value,3.key:vlaue）
##stu1 = {'name':'zhangsan','ages':'18','gender':'男'}
##print (stu1.keys())  ##字典的keys方法，取得所有的key的集合
##for k in stu1.keys():
##    print (k)        ##for循环，遍历所有的key
##keys = list(stu1.keys())  ##list 方法把输出的key集合变成列表
##print (keys)

##print (stu1.values())           ##字典的values方法，取得所有的value的集合
##for e in stu1.values():         ##for循环，遍历所有的value
##    print (e)
##values = list(stu1.values())    ##list 方法把输出的value集合变成列表
##print (values)

##print (stu1.items())  ##字典的items方法，取得所有的键值对集合，输出的是元组（不可修改）
##for w in stu1.items():         ##for循环，遍历所有的键值对（元组类型）
##    print (w)                  ##  w是个元组，可以调用元组的方法
##    print (w[0],w[1])          ## w[0]单独输出key,w[1]单独输出value
##items = list (stu1.items())
##print (items)
##
##for a,b in stu1.items() :       ##字典的items方法，for循环，定义变量a(key),b(values)
##    print (a,b)                 ##输出变量a(key),b(values)，同上，更简洁



##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##字典和集合的判断(==   !=) 会按照顺序来比较，当第一个元素和第一个元素不匹配的时候就会
##l1 = ["zhang","wang"]
##l2 = ["zhang","wang"]      
##print (l1==l2)          ##(长度和内容)是一样的就是会返回True

##l1 = ["zhang","wang","1"]
##l2 = ["zhang","wang"]
##print (l1==l2)           ##(长度和内容)不是一样的就是会返回False

##l1 = ["zhang","wang"]
##l2 = ["zhang","wang"]
##print (l1!=l2)          ##(长度和内容)不是一样的就是会返回True

##l1 = ["zhang","wang","1"]
##l2 = ["zhang","wang"]
##print (l1!=l2)         ##(长度和内容)是一样的就是会返回False

##l1 = ["zhang","wang"]  ##按照顺序来比较，当l1第一个元素和l2第一个元素不匹配的时候就会
##l2 = ["wang","zhang"]  ##顺序不正确就会输出False
##print (l1==l2)     

##stu1 = {'name':'zhangsan','ages':'18','gender':'男'} 
##stu2 = {'name':'zhangsan','ages':'18','gender':'男'}
##print (stu1==stu2)  

##stu1 = {'ages':'18','name':'zhangsan','gender':'男'}  ##字典不会判断顺序，判断：个数和键值对
##stu2 = {'name':'zhangsan','ages':'18','gender':'男'}
##print (stu1==stu2)       ##(个数和键值对)一样就会返回True


##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##一个班级的数据：名字，年龄，性别，用列表定义，列表和字典的嵌套使用
##列表和字典的嵌套使用，
stu = [{'name':'zhangsan','ages':'18','gender':'女'},  ##索引值=学号
       {'name':'李四','ages':'29','gender':'男'},
       {'name':'王五','ages':'10','gender':'男'},
       {'name':'xxxxx','ages':'48','gender':'女'},]

print (stu[0]['gender']) ##输出 学号为1的学生的性别  列表名[索引（学号）][字典里的gender值（年龄）]

##stu1 = {'name':'zhangsan','ages':'18',
##        'gender':'男','hobby':["篮球","足球","画画"]}##兴趣使用列表，含有多个兴趣爱好
####print (stu1['hobby'][1])             ##输出字典里的兴趣，第二个兴趣    

##bir = {"zhang":"1.2", "wang":"3.14",}
##
##print ("生日是：",bir["zhang"])


##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
##
##l = ["xx","zz","qq","vv","qwewqewqewqe","ewqewqedsadas",   ##列表可以换行
##     "sadsadasda","dasdasdadasdasd","dasdasdwdasdadawd"]
##
##print (l)

##i = "qweqwesadsakdhasjdklsajkdj\          ##连续字符“\”,尾部加"\"
##ksajdkljakjskhjsahdsajdkljsa\
##kdjksjdsajdlhf\
##jbvcdsbjdhflsajkdaj\
##widhidfhshdklasjdahfiohdhasih"
##
##print (i)



##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\##增删改字典
##stu1 = {'name':'zhangsan','age':17,'gender':'男'}
##stu1['rank']=3                 ##增加键值对
##
####stu2 = {}         ##添加空字典
##stu1 ['age'] = 18        ##修改年龄为18
##print (stu1)
##
##
##del(stu1['age'])       ##删除age的键值对
##del stu1['rank']         ##删除rank的键值对
##print (stu1)


##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\####字典  key-value

####names = ["zhangsan","lisi","wangwu","zhao"]   ##区别：列表里存储的都是同一种类的信息
##
##stu1 = {'name':'zhangsan','age':17,'gender':'男'}  ##键值对，冒号后面是信息（格式{'key':'value'}）
##
##
##print (stu1['name'])          ##查询格式 
##print (stu1['age'])  
##print (stu1['gender'])  
##























