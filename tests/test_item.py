import pytest
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    assert 10000 * Item.pay_rate == item.price


def test_instantiate_from_csv(item):
    assert item.instantiate_from_csv() == {'name': 'Смартфон', 'price': '100', 'quantity': '1'}


def test_string_to_number(item):
    assert item.string_to_number() == 0