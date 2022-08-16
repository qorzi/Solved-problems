class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def details(cls, name, birth_year):
        cls.name = name
        cls.birth_year = birth_year

    def check_age(self):
        return bool(self.age > 19)

p1 = Person('룰루', 3)
p2 = Person('질럿', 100)
print(p1.name) #룰루
print(p2.age) #100
print(p1.check_age()) #False
print(p2.check_age()) #True

Person.birth_year = 2
print(Person.birth_year) #2


