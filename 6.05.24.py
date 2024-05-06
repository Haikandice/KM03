class  A : #класс аты
    attr = 'Helo world' #атребуты
    def hello(self): # метод
        print(self.attr)

obj1 = A()
hello = obj1.hello()
print(hello)



class Person:
    def __init__(self,name,age,surname=""):
        self.name = name
        self.age = age
        self.surname = surname


    def my_medhod(self):
        if self.surname:
            print('Менің аты жөнім ' +self.name ,self.surname,"Жасым", self.age)
        else:
            print('Менің аты жөнім ' +self.name, "Жасым: " + str(self.age))


p1 = Person("Miko",16 , "bekesh")
p1.my_medhod()
p2 = Person("Miko",16)
p2.my_medhod()


class Car:
    def __init__(self,marka,model,god=""):
        self.marka = marka
        self.model = model
        self.god = god

    def info(self):
            print("Марка", self.marka ,"Модель",self.model ,"Год", str(self.god))

p3 = Car("Bmw","e34" , "1994")
p3.info()

