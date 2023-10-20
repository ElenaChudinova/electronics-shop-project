import pytest
from src.phone import Phone

@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
        phone.number_of_sim = 0
        phone.number_of_sim = 1.2

def test__repr__(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test__add__(phone):
    assert phone + phone == 10