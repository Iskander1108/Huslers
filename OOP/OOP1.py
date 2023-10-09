# OOP



# class Car :
#     def __init__(self, name, kaleso, engine, door, okna):
#         self.name = name
#         self.kaleso = kaleso
#         self.engine = engine
#         self.door = door
#         self.okna = okna
    
#     def turn_on(self, key = False):
#         if key:
#             return "Зажигание"
#         else:
#             return "Встанте ключ"
    
#     def start(self):
#         return "Запуск"
    
#     def turn_off(self):
#         return "Отключаюсь"
    
#     def __str__(self):
#         return self.name

# car1 = Car("BMW", 4, "makvin", 2, 4) 
# car2 = Car("Yamaha", 2, "yamaha", None, 1)

# print(car1.turn_on())
# print(car1.start())
# print(car1.turn_off())
# print(car1)




# class Country:
#     def __init__(self, title, population, president, capital, ploshat, language):
#         self.title = title
#         self.population = population
#         self.president = president
#         self.capital = capital
#         self.ploshat = ploshat
#         self.language = language
    
#     def get_title(self):
#         return self.title
    
#     def get_info(self):
#         return f"""
#         Страна: {self.title}
#         Популяция: {self.population}
#         Президент: {self.president}
#         Столица: {self.capital}
#         Площадь: {self.ploshat}
#         Язык: {self.language}"""
    
#     def __str__(self):
#         return f"Страна: {self.title}"
    

# ru = Country("Russia", 146000000, "Vladimir Putin", "Moscow", 17000, "Ru")
# kz = Country("Kazakhstan", 18500000, "К.Ж. Токаев", "Astana", 27000, "Kz")
# kg = Country("Kyrgyzstan", 4300000, "C. Жапаров", "Bishkek", 20000, "Kg")

# ru.president = "В. В. Путин"

# country = [ru, kz, kg]
# for i in country:
#     print(i.president)


# class Book:
#     def __init__(self, title, author, genre, pages):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.pages = pages
    
#     def get_info(self):
#         return f"""
#     Название: {self.title}
#     Автор: {self.author}
#     Жанр: {self.genre}
#     Страницы: {self.pages}"""

#     def change_author(self, new_author):
#         self.author = new_author
#         return f"Изменен автор на {new_author}"
    
#     def add_pages(self, new_pages):
#         self.pages += new_pages
#         return f"Добавленно {new_pages} странниц"
    
#     def __str__(self):
#         return f"Книжка: {self.title}"
    

# book1 = Book("Капля", "Михаил Лермонтов", "Роман", 400)
# book2 = Book("Три мушкетера", "Михаил Лермонтов", "Роман", 600)
# book3 = Book("Двенаки", "Михаил Лермонтов", "Роман", 500)
    

# book1.change_author("М.Лермонтов")
# book1.add_pages(100)
# print(book1.get_info())




# class CaffeinatedBeverage:
#     def __init__(self, name, caffeinat, volume):
#         self.name = name
#         self.caffeinat = caffeinat
#         self.volume = volume
    

#     def get_info(self):
#         return f"""
#         Название напитка: {self.name}
#         Кофеин: {self.caffeinat}
#         Объем: {self.volume}"""


#     def change_name(self, new_name):
#         self.name = new_name
#         return f"Измененно Название напитка: {new_name}"

#     def add_caffeine(self, coffeine_amount):
#         self.caffeinat += coffeine_amount
#         return f"Добавленно {coffeine_amount} кафеина"
    
#     def add_volume(self, volume_amount):
#         self.volume += volume_amount
#         return f"Добавленно {volume_amount} объема"
    
#     def __str__(self):
#         return f"Напиток: {self.name}"
    
# beverage1 = CaffeinatedBeverage("Латте", 100, 400)
# beverage2 = CaffeinatedBeverage("Капучино", 200, 500)

# print(beverage1.get_info())
# print(beverage1.change_name("RAF"))
# print(beverage1.add_caffeine(50))
# print(beverage1.add_volume(100))
# print(beverage1.get_info())





# class Phone:
#     def __init__(self, brand, model, storage_capacity, is_smartphone):
#         self.brand = brand
#         self.model = model
#         self.storage_capacity = storage_capacity
#         self.is_smartphone = is_smartphone 

#     def get_info(self):
#         return f"""
#         Марка: {self.brand} 
#         Модель: {self.model}
#         Память: {self.storage_capacity}GB
#         Смартфон: {self.is_smartphone}"""
    
#     def change_model(self, new_model):
#         self.model = new_model
#         return f"Измененна модель: {new_model}"
    
#     def upgrade_storage(self, new_storage):
#         self.storage_capacity += new_storage
#         return f"Добавленно {new_storage} памяти"
    
#     def __str__(self):
#         return f"Телефон: {self.brand} {self.model} {self.storage_capacity}GB"
    
# phone1 = Phone("Samsung", "Galaxy S10", 128, True)
# phone2 = Phone("Xiaomi", "Redmi Note 9", 256, False)

# print(phone1.get_info())
# print(phone1.change_model("Galaxy S23 ULTRA"))
# print(phone1.upgrade_storage(128))
# print(phone1.get_info())

# print(phone2)
    


class Car:
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
    
    def get_info(self):
        return f"""
        Марка: {self.make}
        Модель: {self.model}
        Год: {self.year}
        Тип топлива: {self.fuel_type}"""
    
    def change_model(self, new_model):
        self.model = new_model
        return f"Измененна модель: {new_model}"
    
    def update_year(self,new_year):
        self.year = new_year
        return f"Обновлен Год: {new_year}"
    
    def change_fuel_type(self, new_fuel_type):
        self.fuel_type = new_fuel_type
        return f"Изменен тип топлива: {new_fuel_type}"
    
    def __str__(self):
        return f"Машина: {self.make} {self.model} {self.year} {self.fuel_type}"
    
car1 = Car("Audi", "A4", 2020, "Дизель")
car2 = Car("BMW", "M5", 2021, "Бензин")

print(car1.get_info())
print(car1.change_model("A6"))
print(car1.update_year(2022))
print(car1.change_fuel_type("Бензин"))
print(car1.get_info())

print(car2.get_info())
     
