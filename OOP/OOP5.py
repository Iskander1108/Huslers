# ПОЛИМОРФИЗМ

class Transport:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def speed(self):
        return "Какая то скорость"


    def __str__(self) -> str:
        return f"Транспорт -> {self.name} {self.year} -> года"
    
class Bmw(Transport):
    def __init__(self, name, year):
        super().__init__(name, year)

    def speed(self):
        return "280km"
    
    def __str__(self) -> str:
        return super().__str__()


class Mercedes(Transport):
    def __init__(self, name, year):
        super().__init__(name, year)

    def speed(self):
        return "250km"
    
    def __str__(self) -> str:
        return super().__str__()
    

bmw1 = Bmw("BMW", 2020)
mercedes1 = Mercedes("Mercedes", 2021)



auto_list = [bmw1, mercedes1]

for auto in auto_list:
    print(auto.speed())


    
