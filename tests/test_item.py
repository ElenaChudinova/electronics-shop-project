import pytest
from src.item import Item


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
