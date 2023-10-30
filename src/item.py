import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else "InstantiateCSVError: Файл item.csv поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity


        Item.all.append((self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только объекты классов с родительским классом Item")

    @property
    def set_name(self):
        return self.__name

    @set_name.setter
    def set_name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, file):
        try:
            cls.all.clear()
            with open(os.path.join(os.path.dirname(__file__), file), 'r', encoding='windows-1251') as csv_file:
                reader = csv.DictReader(csv_file)
                items = list(reader)
            for item in items:
                name, price, quantity = item['name'], item['price'], item['quantity']
                if name or price or quantity == '':
                    raise InstantiateCSVError('Файл item.csv поврежден')
                cls(name, float(price), int(quantity))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')


    @staticmethod
    def string_to_number(price):
        return int(float(price))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return self.price * self.pay_rate
