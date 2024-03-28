from utils.utils import *


def test_get_executed_bank_operations():
    assert get_executed_bank_operations() is not None


def test_get_last_5_bank_operations():
    assert len(get_last_5_bank_operations()) == 5


def test_get_formatted_date():
    assert get_formatted_date("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_code_card_number():
    assert code_card_number("1596837868705199") == "1596 83** **** 5199"


def test_code_bank_account_number():
    assert code_bank_account_number("64686473678894779589") == "**9589"


def test_get_formatted_from_data(bank_transaction_fixture):
    assert get_formatted_from_data(bank_transaction_fixture) == "Maestro 7810 84** **** 5568"


def test_get_formatted_to_data(bank_transaction_fixture):
    assert get_formatted_to_data(bank_transaction_fixture) == "Счет **2869"
