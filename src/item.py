import csv

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
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def set_name(self):
        return self.__name

    @set_name.setter
    def set_name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]


    def instantiate_from_csv(self):
        with open('src/items.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            for read in reader:
                return read

    def string_to_number(self):
        return int()

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

