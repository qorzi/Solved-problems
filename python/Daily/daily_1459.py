class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, dog_name, dog_type):
        self.dog_name = dog_name
        self.dog_type = dog_type
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
    
    def bark(self):
        print('왈왈')

    def __del__(self):
        Doggy.num_of_dogs -= 1

    @classmethod
    def get_status(self):
        print(Doggy.birth_of_dogs)
        print(Doggy.num_of_dogs)

dog1 = Doggy('초코', '시고르')
dog2 = Doggy('바나나', '믹스')

del dog1

dog2.bark()
Doggy.get_status()
print(dog2.dog_name)