# АБСТРАГИРОВАНИЕ

from abc import ABC, abstractmethod




class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def voice(self):
        return "Какой то звук"
    


    def __str__(self):
        return f"Животному {self.name} {self.age} лет"
    
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    # def voice(self):
    #     return "Гааав"
    
    def __str__(self):
        return super().__str__()
    

dog1 = Dog("Собака", 10)
print(dog1.voice())

