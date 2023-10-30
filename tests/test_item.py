import pytest
from src.item import Item
from src.item import InstantiateCSVError

items_csv = "./item.csv"

@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    assert 10000 * Item.pay_rate == item.price


def test_string_to_number(item):
    assert item.string_to_number('10000') == 10000
    assert item.string_to_number('5.5') == 5

def test__repr__(item):
    assert item.__repr__() == "Item('Смартфон', 10000, 20)"

def test__str__(item):
    assert item.__str__() == 'Смартфон'

def test__add__(item):
    assert item + item == 40

def test_instantiate_from_csv_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(items_csv = "./item.csv")

def test_instantiate_from_csv_damaged():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('items_csv')

