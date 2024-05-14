class Person:
    def __init__(self,name):
        self.name = name
    def get_info(self):
        print("Аты:",self.name)

class Employee(Person):
    def job(self,job_name):
        print("Аты:",self.name,"Жұмысы:",job_name)

employe_obj = Employee("Miras")
employe_obj.job("Miko")




class Figura:
    def __init__(self, color):
        self.color = color

    def get_info(self):
        print("Color:", self.color)


class Triangle(Figura):
    def __init__(self, color, p1, p2, p3):
        Figura.__init__(self, color)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.perimeter = self.p1 + self.p2 + self.p3

    def get_info(self):
        print("Цвет:", self.color, "Периметр:", self.perimeter)


triangle = Triangle("Красный", 3, 2, 4)
triangle.get_info()
