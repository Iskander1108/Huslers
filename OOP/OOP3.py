class Tefalle:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"Включение")
        print(self.__boil())
        print(self.__done())
        print(self.turn_off())
    
    def __boil(self):
        return f"Вода на стадии кипения"
    
    def __done(self):
        return f"Вода закипела"
    
    def turn_off(self):
        return f"Выключение"
    
    def __str__(self):
        return f"Тефаль {self.name}"
    
# public turn_on
# protected _turn_on
# private __turn_on


a = Tefalle("Тефаль 1")
print(a.turn_on())