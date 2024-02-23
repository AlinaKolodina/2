class Drink:
    """Базовый класс напитки"""

    def __init__(self, name: str, volume: int) -> None:
        """
        Создание и подготовка к работе объекта "Напиток"
        :param name: название напитка
        :param volume: объем в миллилитрах

        Примеры:
            >>> dr = Drink("Coca Cola", 1000)
        """

        if not isinstance(name, str):
            raise TypeError("Название напитка должно быть строкой")
        self.name = name

        if not isinstance(volume, int):
            raise TypeError("Объем должен быть целым числом")
        if volume < 0:
            raise ValueError("Объем должен быть положительным числом")
        self.volume = volume

    def dish(self) -> str:
        """Определение по объему напитка типа посуды"""

        if self.volume < 250:
            return "Воспользуйтесь обычной чашкой"
        elif self.volume < 500:
            return "Вам нужна большая кружка"
        else:
            return "Вы куда столько пьете? Воспользуйтесь графином... или чайником..."

    def __str__(self) -> str:
        return f"Напиток - {self.name}. Объем - {self.volume}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, volume={self.volume!r})"

class HotDrink(Drink):
    """Дочерний класс для напитков - горячие напитки"""

    def __init__(self, name: str, volume: int, temp: int) -> None:
        """
                Создание и подготовка к работе объекта "Напиток"
                :param name: название напитка
                :param volume: объем в миллилитрах
                :param temp: температура в градусах

                Примеры:
                    >>> hdr = HotDrink("Кофе", 250, 20)
                """
        super().__init__(name, volume)

        if not isinstance(temp, int):
            raise TypeError("Температура напитка должна быть целым числом")
        if temp < 0:
            raise ValueError("Температура напитка должна быть положительным числом")
        self.temp = temp

    def __str__(self) -> str:
        return f"{super().__str__()}. Температура - {self.temp}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, volume={self.volume!r}, temperature={self.temp!r})"

class ColdDrink(Drink):
    """Дочерний класс для напитков - холодные напитки"""

    def __init__(self, name: str, volume: int) -> None:
        """
                Создание и подготовка к работе объекта "Напиток"
                :param name: название напитка
                :param volume: объем в миллилитрах

                Примеры:
                    >>> cdr = ColdDrink("Лимонад", 400)
                """
        super().__init__(name, volume)

    def dish(self) -> str:
        """Определение по объему напитка типа посуды"""
        #метод перегружен, так как холодные напитки чаще всего продаются в пластиковой посуде

        if self.volume < 250:
            return "Вам нужен маленький стаканчик "
        elif self.volume < 500:
            return "Вам нужна обычная бутылка"
        elif self.volume < 1000:
            return "Воспользуйтесь большой бутылкой"
        else:
            return "Вы уверены, что столько выпьете? Поищите большую бутылку"

    def __str__(self) -> str:
        return f"{super().__str__()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, volume={self.volume!r})"

if __name__ == "__main__":
    # Write your solution here
    dr = Drink("Coca Cola", 1000)
    hdr = HotDrink("Кофе", 250, 20)
    cdr = ColdDrink("Лимонад", 1500)
    print(cdr.dish())
    print(cdr)
    print(repr(hdr))
