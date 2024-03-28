import json
from datetime import datetime


def get_executed_bank_operations():
    """
    Загружает список выполненных банковских операций из файла
    """
    executed_bank_operations = []
    with open('C:/Users/A/PycharmProjects/coursework_3/utils/data/operations.json', 'r') as file:
        for operation in json.load(file):
            if operation.get("state") == "EXECUTED":
                executed_bank_operations.append(operation)
        return executed_bank_operations


def get_last_5_bank_operations():
    """
    Возвращает 5 последних выполненных операций
    """
    operations_sorted_by_data = sorted(get_executed_bank_operations(), key=lambda x: x["date"], reverse=True)
    return operations_sorted_by_data[:5]


def get_formatted_date(date):
    """
    Возвращает дату в формате ДД.ММ.ГГГГ
    """
    transaction_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return transaction_date.strftime("%d.%m.%Y")


def code_card_number(card_number):
    """
    Возвращает номер карты в формате  XXXX XX** **** XXXX
    """
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def code_bank_account_number(bank_account_number):
    """
    Возвращает номер счета в формате **XXXX
    """
    return "**" + bank_account_number[-4:]


def get_formatted_from_data(transaction_data):
    """
    Возвращает отформатированные данные, откуда был сделан перевод
    """
    formatted_from_data = ""

    if transaction_data.get("from"):
        from_data_list = transaction_data.get("from").split()

        for i in from_data_list:
            if len(i) == 16:
                formatted_from_data += code_card_number(i)
            elif len(i) == 20:
                formatted_from_data += code_bank_account_number(i)
            else:
                formatted_from_data += i + " "
    return formatted_from_data


def get_formatted_to_data(transaction_data):
    """
    Возвращает отформатированные данные, куда был сделан перевод
    """
    return "Счет " + code_bank_account_number(transaction_data.get("to")[-20:])


def print_formatted_bank_operations():
    """
    Выводит на экран список из 5 последних выполненных клиентом операций в формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    """
    last_5_operations = get_last_5_bank_operations()
    for operation in last_5_operations:
        formatted_date = get_formatted_date(operation["date"])
        formatted_from_data = get_formatted_from_data(operation)
        formatted_to_data = get_formatted_to_data(operation)

        print(f"{formatted_date} {operation["description"]}\n"
              f"{formatted_from_data} -> {formatted_to_data}\n"
              f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")
