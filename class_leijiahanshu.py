
##格式    类就是模板，包含属性和方法
##class xx:
##    def __init__(self,xx,xx):



####class Dog ():   ##class类，Dog 类名字（自己定义名称，类名首字母大写）
####   ## __init__    表示类里有多少变量
#########初始化方法      把self当做自身
####    def __init__(self,name,age,color):  ##必须类里的函数第一个参数是“self”
####        self.name = name          ##使用self.name添加name到类Dog中,名字赋值给自身
####        self.age = age            ##使用self.age添加age到类Dog中
####        self.color = color 
######添加一些行为
####    def sit(self):
####        print (self.name+"坐下")
####
####    def roll_over(self):
####        print(self.name+"打滚")
####
####
####

######实际狗的名字，对象名也是个变量名
####
####dog1 = Dog("大白",2,"黑色")
####
####dog2 = Dog("ss",2,"白色")
####
####
####print(dog1.name)
####print(dog2.name) 
####
####dog1.sit()
####dog2.sit()
####
####dog1.roll_over()
####dog2.roll_over()

########*****************##实例**************************

####class Car():
####    def __init__(self,maker,model,year):
####        self.maker = maker
####        self.model = model
####        self.year = year
####        self.mileage = 0    ##历程默认为0
####
####    def describle(self):   #定义方法，输出之前设置的参数
####        print (self.maker+" "+self.model+" "+self.year)
####        
####    def get_mileage(self):   ##调用mileage方法，查询车跑了多少公里
####        print ("这个车已经跑了"+str(self.mileage)+"公里")
####
####    def set_mileage(self,mileage): ##修改历程参数，修改的数字不能小于当前的数字（mileage形参）
####        if self.mileage<mileage:    ##self.mileage默认值是0，mileage 是修改的值
####           self.mileage = mileage  ##把刚刚修改的值 赋值给定义的值
####           
####    def add_mileage(self,mileage):  ##增加里程数
####        if mileage>=0:              ##当里程数不为0
####            self.mileage += mileage  ##self.mileage = self.mileage + mileage
####
####        
####car1 = Car("大众","桑塔纳","1999") ##定义车辆名称xxx（car1）属（包括，maker,model,year）
####
####car1.describle()      ##定义车辆，调用类的里方法，xxx.方法名（）
####car1.get_mileage()
######if car1.mileage <100:  ##修改 ，不推荐
######    car1.mileage = 100
####
####car1.set_mileage(100)  ##调用修改方法
####car1.set_mileage(10)   ##设置了条件，修改的数字不能小于当前的数字，输出历程只能输出之前的值
####car1.get_mileage()     ##输出修改后的里程数
####
####
####car1.add_mileage(10)
####car1.get_mileage()


##\\\\\\\\\\\\\\\\\\\\\继承\\\\\\\\\\\\\\\\\\\\

##class Person():
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##
##    def eat(self):
##        print (self.name + "吃饭")
##        
##    def sleep(self):
##        print (self.name + "睡觉")
##
##
####让Teacher继承Person
##class Teacher(Person):
##    def __init__(self,name,age,subject,clas):
##        super().__init__(name,age)    ##调用父类的初始化方法
##        self.subject = subject
##        self.clas = clas
##
##    
##    def sub(self):
##        print(self.name+"老师在"+self.clas+"上"+self.subject+"课")
##
##    #重写父类的方法
##    def eat(self):
##        print(self.name + "食堂吃饭")
##        
##    
##people1 = Person("李白",56)
##
##people1.eat()
##people1.sleep()
##
##t1 = Teacher("杜甫",34,"数学","高二一班")
##t1.eat()
##t1.sub()

##把一个类变成另一个类的属性

##import weapon
##from weapon import *
##
##class Role():
##    def __init__(self,name,lv,role_type,damage,buttet_count):   
##        self.name = name
##        self.lv = lv
##        self.role_type = role_type
##        self.Weapon =Weapon(damage,buttet_count)
####        self.damage = damage
####        self.buttet_count = buttet_count
##
##    def walk(self):
##        print(self.name+"走路")
##        
##    def attack(self):
##        self.Weapon.attack()
####        self.buttet_count -=1
####        print("发射子弹，攻击力是%d，剩余子弹%d" %(self.damage,self.buttet_count))
##
##r1 = Role("libai","90","战士",999,90)
##r1.walk()
##r1.attack()


































