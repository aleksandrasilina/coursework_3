import pytest

bank_transaction = {
    'date': '2019-11-19T09:22:25.899614',
    'description': 'Перевод организации',
    'from': 'Maestro 7810846596785568',
    'id': 154927927,
    'operationAmount': {
        'amount': '30153.72',
        'currency': {
            'code': 'RUB',
            'name': 'руб.'
        }
    },
    'state': 'EXECUTED',
    'to': 'Счет 43241152692663622869'
}


@pytest.fixture
def bank_transaction_fixture():
    return bank_transaction.copy()