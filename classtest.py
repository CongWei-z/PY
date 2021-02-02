

##
class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def personinfo(self):
        print("名字是：%s ，年龄是：%s ，性别是：%s " %(self.name,self.age,self.gender))





class Student(Person):
    def __init__(self,name,age,gender,college,clas):
        super().__init__(name,age,gender)
        self.college=college
        self.clas=clas
        
    def personinfo(self):
        super().personinfo()
        print("学院：%s，班级：%s "%(self.college,self.clas))

    def study(self,teacher):  ##定义方法，形参为teacher，
        teacher.teach_obj()  ## 调用形参的teach_obj()方法（在Teacher类里）
        print (teacher.name+"老师我学会了")
        
    def __str__(self):  ##“魔法”方法，必须返回字符串,直接输出的时候可以返回值
        return "名字是：%s ，年龄是：%s ，性别是：%s 学院：%s，班级：%s" %(self.name,self.age,self.gender,self.college,self.clas)

        

##p1 = Student("zhangsan","21","男","医学院","大三")
##p1.personinfo()

class Teacher(Person):
    def __init__(self,name,age,gender,college,professional):
        super().__init__(name,age,gender)
        self.college=college
        self.professional=professional

    def personinfo(self):
        super().personinfo()
        print("学院：%s，专业：%s "%(self.college,self.professional))

    def teach_obj(self):
        print("讲了面向对象")

    def __str__(self):  ##“魔法”方法，必须返回字符串,直接输出的时候可以返回值
        return "名字是：%s ，年龄是：%s ，性别是：%s 学院：%s，专业：%s" %(self.name,self.age,self.gender,self.college,self.professional)


   
    
t1=Teacher("张三","45","男","医学院","医学")
t2=Teacher("李白","56","男","计算机","c++")
t3=Teacher("杜甫","43","男","法学院","法学")

##t1.personinfo()
##t1.teach_obj()
##p1 = Student("李四","21","男","医学院","大三")

##p1.personinfo()
##
##p1.study(t1)      ##study的方法teacher的实参是t1

##print (t1)  ##自动调用了__str__方法，就等于t1.__str__(),在这可以舍去
##print (p1)

l = []
l.append(t1)
l.append(t2)
l.append(t3)

for i in l :
    print(i)





















