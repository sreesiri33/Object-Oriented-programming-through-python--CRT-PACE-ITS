class employee1():
    def name(self):
        print("Sreesiri is my name")
    def salary(self):
        print("300000 is my salary")
    def age(self):
        print("19 is my age")
class employee2():
    def name(self):
        print("vaishnavi is her name")
    def salary(self):
        print("300000 is her salary")
    def age(self):
        print("18 is her age")
def func(obj):
    obj.name()
    obj.salary()
    obj.age()
obj_emp1 = employee1()
obj_emp2 = employee2()
func(obj_emp1)
func(obj_emp2)
