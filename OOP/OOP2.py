# НАСЛЕДОВАНИЕ , ИНКАПСУЛЯЦИЯ


class Transport:
    def __init__(self, type, name, marka, year, color, fuel, speed):
        self.type = type
        self.name = name
        self.marka = marka
        self.year = year
        self.color = color
        self.fuel = fuel
        self.speed = speed

    def _turn_on(self):
        return f"Включение транспорта {self.name}"
    
    def _turn_off(self):
        return f"Выключение транспорта {self.name}"
    
    def _drive(self):
        return f"Транспорт {self.name} едет со скоростью {self.speed} км/ч"
    
    def _stop(self):
        return f"Транспорт {self.name} остановилась"
    
    def _add_speed(self, new_speed):
        self.speed += new_speed

    def _difference_speed(self, new_speed):
        self.speed -= new_speed

    def __str__(self):
        return f"Это РД(родительский класс) класс {Transport.__name__}"
    

class Car(Transport):
    def __init__(self, type, name, marka, year, color, fuel, speed):
        super().__init__(type, name, marka, year, color, fuel, speed)

    def turn_on_car(self, key=False ):
        if key == True:
            return super()._turn_on()
        else:
            return f"Ключ не найден"
        
    def turn_off_car(self, key=False):
        if key == True:
            return super()._turn_off() 
        else:
            return f"Ключ не найден"
        
    def drive_car(self, key=False):
        if key == True:
            return super()._drive()
        else:
            return f"Ключ не найден"
        
    def stop_car(self, key=False):
        if key == True:
            return super()._stop()
        else:
            return f"Ключ не найден"
        
    def add_speed_car(self, new_speed, key=False):
        if key == True:
            return super()._add_speed(new_speed)
        else:
            return f"Ключ не найден"
        
    def difference_speed(self, new_speed, key=False):
        if key == True:
            return super()._difference_speed(new_speed)
        else:
            return f"Ключ не найден"
    
    def get_info(self):
        return f"""
            Тип транспорта: {self.type}
            Модель транспорта: {self.name}
            Марка транспорта: {self.marka}
            Год: {self.year}
            Цвет: {self.color}
            Тип топлива: {self.fuel}
            Скорость: {self.speed}
            """
    
    def __str__(self): 
        return f"Это тип транспорта {self.type} и марка {self.marka}"
    


bmw = Car("Транспорт", "BMW", "X5", 2020, "Красный", "Бензин", 200)
toyota = Car("Транспорт", "Toyota", "Corolla", 2019, "Серый", "Дизель", 180)


print(bmw.turn_on_car(key=True))
print(bmw.drive_car(key=True))
bmw.add_speed_car(30, key=True)
print(bmw.drive_car(key=True))




class Moto(Transport):
    def __init__(self, type, name, marka, year, color, fuel, speed):
        super().__init__(type, name, marka, year, color, fuel, speed)

    def turn_on_moto(self, key=False ):
        if key == True:
            return super()._turn_on()
        else:
            return f"Ключ не найден"
        
    def turn_off_moto(self, key=False):
        if key == True:
            return super()._turn_off()
        else:
            return f"Ключ не найден"
        
    def drive_moto(self, key=False):
        if key == True:
            return super()._drive()
        else:
            return f"Ключ не найден"
        
    def stop_moto(self, key=False):
        if key == True:
            return super()._stop()
        else:
            return f"Ключ не найден"
        
    def add_speed_moto(self, new_speed, key=False): 
        if key == True:
            return super()._add_speed(new_speed)
        else:
            return f"Ключ не найден"
        
    def difference_speed_moto(self, new_speed, key=False):
        if key == True:
            return super()._difference_speed(new_speed)
        else:
            return f"Ключ не найден"
        
    
    def get_info(self):
        return f"""
            Тип транспорта: {self.type}
            Модель транспорта: {self.name}
            Марка транспорта: {self.marka}
            Года: {self.year}
            Цвет: {self.color}
            Тип топлива: {self.fuel}
            Скоп: {self.speed}
            """
    
    def __str__(self):
        return f"Это тип транспорта {self.type} и марка {self.marka}"
    


honda = Moto("Транспорт", "Honda", "CBR", 2020, "Красный", "Дизель", 100)
yamaha = Moto("Транспорт", "Yamaha", "R1", 2019, "Серый", "Бензин", 120)


print(honda.turn_on_moto(key=True))
print(honda.drive_moto(key=True))
honda.add_speed_moto(30, key=True)
print(honda.drive_moto(key=True))
print(yamaha.get_info())


class Aircraft(Transport):
    def __init__(self, type, name, marka, year, color, fuel, speed):
        super().__init__(type, name, marka, year, color, fuel, speed)

    def turn_on_aircraft(self, key=False ):
        if key == True:
            return super()._turn_on()
        else:
            return f"Ключ не найден"
        
    def turn_off_aircraft(self, key=False):
        if key == True:
            return super()._turn_off()
        else:
            return f"Ключ не найден"
        
    def drive_aircraft(self, key=False):
        if key == True:
            return super()._drive()
        else:
            return f"Ключ не найден"
        
    def stop_aircraft(self, key=False):
        if key == True:
            return super()._stop()
        else:
            return f"Ключ не найден"
        
    def add_speed_aircraft(self, new_speed, key=False):
        if key == True:
            return super()._add_speed(new_speed)
        else:
            return f"Ключ не найден"
        
    def difference_speed_aircraft(self, new_speed, key=False):
        if key == True:
            return super()._difference_speed(new_speed)
        else:
            return f"Ключ не найден"
        
    def get_info(self):
        return f"""
            Тип транспорта: {self.type}
            Модель транспорта: {self.name}
            Марка транспорта: {self.marka}
            Года: {self.year}
            Цвет: {self.color}
            Тип топлива: {self.fuel}
            Скорость: {self.speed}
            """
        
    def __str__(self):
        return f"Это тип транспорта {self.type} и марка {self.marka}"
    


boeing = Aircraft("Транспорт", "Boeing", "737", 2020, "Красный", "Газ", 300)
sy = Aircraft("Транспорт", "Sy", "A380", 2019, "Серый", "Газ", 250)


print(boeing.turn_on_aircraft(key=True))
print(boeing.drive_aircraft(key=True))
boeing.add_speed_aircraft(30, key=True)
print(boeing.drive_aircraft(key=True))
print(sy.get_info())  





# class Shape:

#     def __init__(self):
#         pass

#     def area(self):
#         return 0
    
#     def perimeter(self):
#         return 0
    
#     def get_info(self):
#         return 
    

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return 2 * (self.length + self.width)
    
#     def get_info(self):
#         return super().get_info() + (f"Длина: {self.length} Ширина: {self.width}")
    

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    
#     def get_info(self):
#         return super().get_info() + f"Радиан: {self.radius}"
    

# rectangle = Rectangle(10, 20)
# circle = Circle(5)

# print(Rectangle(rectangle.get_info()))
# print(f"Площадь: {rectangle.area()}")
# print(f"Периметр: {rectangle.perimeter()}")

# print(circle.get_info())
# print(f"Площадь: {circle.area()}")
# print(f"Периметр: {circle.perimeter()}")
