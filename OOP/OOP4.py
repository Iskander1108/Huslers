#  [21.09.2023 21:43]

#ПОЛИМОРФИЗМ

# isinstance - это встроенная функция которая позволяет проверить
    # является ли объект экземпляром определенного класса

    # В нашем случае мы проверяем my_list = [dog1, dog2, cat1, cat2, baran]
    # на является ли экземпляры наследниками Animal

#ПОЛИМОРФИЗМ


class Animal:
    """Базовый класс для представления животных.

    Attributes:
        name (str): Имя животного.

    Methods:
        voise(): Возвращает звук, издаваемый животным.

    """

    def __init__(self, name) -> None:
        """
        Инициализирует новый объекет Animal.

        Args:
            name (str): Имя живетнооа.

        """
        self.name = name
        """
        Инициализирует новый объект Animal.

        Args:
            name (str): Имя животного.

        """
        self.name = name

    def voise(self) -> str:
        """
        Возвращает звук, издаваемый животным.

        Returns:
            str: Звук животного.

        """
        return 'Какой-то звук'

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Animal.

        Returns:
            str: Строковое представление объекта.

        """
        return "Я животный"


class Dog(Animal):
    """Класс для представления собаки, наследует атрибуты и методы класса Animal.

    Attributes:
        name (str): Имя собаки.

    Methods:
        voise(): Возвращает звук, издаваемый собакой.

        __str__(): Возвращает строковое представление объекта Dog.

    """

    def __init__(self, name) -> None:
        """
        Инициализирует новый объект Dog.

        Args:
            name (str): Имя собаки.

        """
        super().__init__(name)

    def voise(self) -> str:
        """
        Возвращает звук, издаваемый собакой.

        Returns:
            str: Звук собаки.

        """
        return 'Гав гав'
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Dog.

        Returns:
            str: Строковое представление объекта.

        """
        return f"Я собака {self.name}"



class Cat(Animal):
    """Класс для представления кошки, наследует атрибуты и методы класса Animal.

    Attributes:
        name (str): Имя кошки.

    Methods:
        voise(): Возвращает звук, издаваемый кошкой.

        __str__(): Возвращает строковое представление объекта Cat.

    """

    def __init__(self, name) -> None:
        """
        Инициализирует новый объект Cat.

        Args:
            name (str): Имя кошки.

        """
        super().__init__(name)

    def voise(self) -> str:
        """
        Возвращает звук, издаваемый кошкой.

        Returns:
            str: Звук кошки.

        """
        return f'{self.name} Мяу Мяу'

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Cat.

        Returns:
            str: Строковое представление объекта.

        """
        return f"Я кошка {self.name}"



class Ram:
    """Класс для представления барана.

    Attributes:
        name (str): Имя барана.

    Methods:
        voise(): Возвращает звук, издаваемый бараном.

        __str__(): Возвращает строковое представление объекта Ram.

    """

    def __init__(self, name) -> str:
        """
        Инициализирует новый объект Ram.

        Args:
            name (str): Имя барана.

        """
        self.name = name

    def voise(self) -> str:
        """
        Возвращает звук, издаваемый бараном.

        Returns:
            str: Звук барана.

        """
        return f'{self.name} Ма ма'

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Ram.

        Returns:
            str: Строковое представление объекта.

        """
        return f"Я баран {self.name}"


class Call_animal(Ram, Dog, Cat):
    """Класс для взаимодействия с разными видами животных.

    Attributes:
        name (str): Имя объекта Call_animal.

    Methods:
        interact_voise(): Взаимодействие с животными по звукам, которые они издают.

        interact_name(): Взаимодействие с животными по их именам.

        interact_count_animal(): Подсчет животных, принадлежащих к классу Animal и вне его.

    """

    def __init__(self, name) -> None:
        """
        Инициализирует новый объект Call_animal.

        Args:
            name (str): Имя объекта Call_animal.

Marselle Naz, [21.09.2023 21:43]


        """
        super().__init__(name)
        self.my_list = [Ram("Тузик"), Dog("Мухтар"), Cat("Мурзик")]
    
    def interact_voise(self) -> str:
        """Взаимодействие с животными по звукам, которые они издают."""
        for animal in self.my_list:
            print(f"Я {animal.name} и я издаю звуки {animal.voise()}")
    
    def interact_name(self) -> str:
        """Взаимодействие с животными по их именам."""
        for animal in self.my_list:
            print(f"Меня зовут {animal.name}")

    def interact_count_animal(self) -> str:
        """Подсчет животных, принадлежащих к классу Animal и вне его."""
        count_animal = 0
        count_other = 0

        for animal in self.my_list:
            if isinstance(animal, Animal):
                count_animal += 1
            else:
                count_other += 1
        return f"""
Подлежащие классу Animal: {count_animal}
Извне класса Animal: {count_other}"""



interact = Call_animal("Интерактивный Класс")
interact.interact_voise()
interact.interact_name()
print(interact.interact_count_animal())


