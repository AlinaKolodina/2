import doctest


class DirtyInSPB:
    def __init__(self, seasn: str, temperature: int):
        """
            Создание и подготова к работе объекта "Грязь в Питере"

            :param seasn: Время года
            :param temperature: Температура на улице

            Примеры:
            >>> situation = DirtyInSPB("Зима", -1)
        """
        self.contamination = 0

        if not isinstance(seasn, str):
            raise TypeError("Время года указывается в виде текста")
        if seasn not in ["Зима", "Весна", "Лето", "Осень"]:
            raise ValueError ("Такого времени года не существует")
        self.seasn = seasn

        if not isinstance(temperature, int):
            raise TypeError("Температура указывается в виде целого числа")
        self.temperature = temperature

    def jeans_contamination(self, using_jeans: int) -> None:
        """
            Функция отвечает за загрязнение джинс в баллах. Зависит от количества носок и погодных условий

            Примеры:
            >>> situation = DirtyInSPB("Зима", -1)
            >>> situation.jeans_contamination(3)
        """

        if not isinstance(using_jeans, int):
            raise TypeError("Количество носок указывается в виде целого числа")
        if using_jeans < 0:
            raise ValueError ("Количество носок не может быть отрицательным числом")
        self.using_jeans = using_jeans

        if self.seasn == 'Лето':
            self.contamination += 1 * self.using_jeans #При обычной летней погоде коэффицент загрязнения принимаем 1
        if self.seasn == 'Зима':
            if self.temperature in range (-50, 1) or self.temperature in range (10, 15) :
                self.contamination += 1 * self.using_jeans #При морозной зимней погоде или теплой зимней погоде коэффицент загрязнения принимаем 1
            else:
                self.contamination += 3 * self.using_jeans  #При температуре от 1 до 10 коэффицент загрязнения принимаем 3

    def jeans_washing(self) -> None:
        """
            Функция отвечает за то, пора ли стирать джинсы. Зависит от баллов загрязнения.

            Примеры:
            >>> situation = DirtyInSPB("Зима", -1)
            >>> situation.jeans_washing()
        """
        if self.contamination in range (1, 7):
            print("Ваши джинсы еще не грязные. Стирать не надо")
        if self.contamination > 7:
           print("Ваши джинсы грязные. Пора стирать")

class BoxOfCandies:
    def __init__(self, number_of_candies: int, stress: int):
        """
            Создание и подготова к работе объекта "Конфеты"

            :param number_of_candies: Количество конфет в коробке
            :param stress: Уровень стресса по шкале от 1 до 10

            Примеры:
            >>> candy = BoxOfCandies(25, 5)
        """
    
        if not isinstance(number_of_candies, int):
            raise TypeError("Количество конфет указывается в виде целого числа")
        if number_of_candies == 0:
            raise ValueError ("Купите конфет")
        if number_of_candies < 0:
            raise ValueError ("Количество конфет не может быть отрицательным числом")
        self.number_of_candies = number_of_candies

        if not isinstance(stress, int):
            raise TypeError("Уровень стресса указывается в виде целого числа")
        if stress > 10:
            raise ValueError ("Успокойтесь. Уровень стресса не может быть выше 10")
        if stress < 0:
            raise ValueError ("Вы слишком спокойны. Уровень стресса не может быть ниже или равен 0")
        self.stress = stress


    def tea_day(self, number_of_teatime: int) -> None:
        """
            Функция отвечает за уменьшение количества конфет в течение дня. Зависит от количества чаепитий и уровня стресса

            Примеры:
            >>> candy = BoxOfCandies(25, 5)
            >>> candy.tea_day(3)
        """
        if not isinstance(number_of_teatime, int):
            raise TypeError("Количество чаепитий указывается в виде целого числа")
        if number_of_teatime == 0:
            raise ValueError ("Попейте чаю")
        if number_of_teatime < 0:
            raise ValueError ("Количество чаепитий не может быть отрицательным числом")
        self.number_of_teatime = number_of_teatime

        #считаем, что за 1 чаепитие съедается 2 конфеты
        if self.stress in [1, 2, 3]:
            self.number_of_candies -= 2 * 1 * self.number_of_teatime #при низком уровне стресса коэффициент увеличения сладкого = 1
        if self.stress in [4, 5, 6]:
            self.number_of_candies -= 2 * 3 * self.number_of_teatime #при среднем уровне стресса коэффициент увеличения сладкого = 2
        if self.stress in [7, 8, 9, 10]:
            self.number_of_candies -= 2 * 4 * self.number_of_teatime #при высоком уровне стресса коэффициент увеличения сладкого = 4

        if self.number_of_candies < 0:
            raise ValueError ("Все конфеты съедены, сходите в магазин")
    def buy(self, number_of_buying_candies: int) -> None:
        """
            Функция отвечает за увеличение количества конфет за счет покупки.

            Примеры:
            >>> candy = BoxOfCandies(25, 5)
            >>> candy.buy(10)
        """
        if not isinstance(number_of_buying_candies, int):
            raise TypeError("Количество конфет указывается в виде целого числа")
        if number_of_buying_candies < 0:
            raise ValueError ("Количество конфет не может быть отрицательным числом")
        self.number_of_buying_candies = number_of_buying_candies

        self.number_of_candies += self.number_of_buying_candies

    def statictics(self)-> None:
        """
            Функция отвечает за вывод остатка конфет
        """
        print (f"У вас осталось {self.number_of_candies} конфет. Приятного чаепития! ")


class Morning:
    def __init__(self, actions: list, sun: bool):
        """
            Создание и подготова к работе объекта "Утро"

            :param actions: Список ОПЦИОНАЛЬНЫХ действий, которые необходимо выполнить утром до выхода из дома
            :param sun: Темно/светло ли на улице утром (True/False)

            Примеры:
            >>> morning = Morning(["завтрак", "душ", "макияж"], True)
        """
        spisok_opt = {
            "завтрак": 10,
            "душ": 15,
            "макияж": 15,
            "зарядка": 10,
            "сбор сумки": 5,
        }
        spisok_essential = {
            "утренние процедуры": 10,
            "одевание": 10,
            "заправка кровати": 2,
        }

        self.base_time = sum(spisok_essential.values())
        self.add_time = 0
        self.opt_time = 0

        if not isinstance(actions, list):
            raise TypeError("Напишите свои опциональные действия перед выходом в формате списка")
        for i in actions:
            for j in spisok_essential.keys():
                if i == j:
                    raise ValueError("Одно из действий является обязательным. Напишите действия, кроме (утренние процедуры, одевание, заправка кровати)")
            if i not in spisok_opt.keys():
                raise ValueError("Такими вещами утром не занимаются. Пересмотрите свои жизненные принципы")
        self.actions = actions

        if not isinstance(sun, bool):
            raise ValueError("Напишите темно/светло ли утром в формате True/False")
        self.sun = sun

        for i in actions:
            for j in spisok_opt.keys():
                if i == j:
                    self.opt_time += spisok_opt[i]

    def pets(self, pet: str) -> None:
        """
            Функция отвечает за утренний уход за домашними животными. Необходимо ввести тип животного или "-" если животных нет.

            Примеры:
            >>> morning = Morning(["завтрак", "душ", "макияж"], True)
            >>> morning.pets("собака")
        """
        spisok_pets = {
            "кошка": 3,
            "собака": 15,
            "птица": 2,
            "рыбки": 2,
        }
        if not isinstance(pet, str):
            raise TypeError("Введите информацию о животных в виде строки. Введите - если животных нет ")
        if pet not in spisok_pets.keys():
            raise ValueError ("Такое дома не держат. Пересмотрите свои жизненные принципы")
        self.pet = pet

        for i in spisok_pets.keys():
            if self.pet == i:
                self.add_time += spisok_pets[i]

    def sun_(self) -> None:
        """
            Функция отвечает за "прихождение в себя" утром в заивисимости от того, темно или светло утром

            Примеры:
            >>> morning = Morning(["завтрак", "душ", "макияж"], True)
            >>> morning.sun_()
        """

        if self.sun == True: #утром светло, легче встать
            self.add_time += 0
        else:
            self.add_time += 7

    def summary(self) -> str:
        """
            Функция выдает, сколько времени необходимо утром на сборы.
        """

        print (f"Вам необходимо {self.base_time + self.add_time + self.opt_time} минут на сборы")

if __name__ == "__main__":
    candy1 = BoxOfCandies(50, 10)
    candy1.tea_day(3)
    candy1.buy(3)
    candy1.statictics()

    situation1 = DirtyInSPB("Лето", 10)
    situation1.jeans_contamination(2)
    situation1.jeans_washing()

    morning = Morning(["завтрак", "душ", "макияж"], True)
    morning.pets("собака")
    morning.sun_()
    morning.summary()

    doctest.testmod()
