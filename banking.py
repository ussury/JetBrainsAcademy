import random
import sqlite3


def create_card_bd():
    connect = sqlite3.connect('card.s3db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS card (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0
    )""")
    connect.commit()
    connect.close()


def insert_data_card(number, pin, balance):
    connect = sqlite3.connect('card.s3db')
    cursor = connect.cursor()

    cursor.execute("INSERT INTO card(number, pin, balance) VALUES (?, ?, ?)",
                   (number, pin, balance))

    connect.commit()
    connect.close()


def select_card_data():
    connect = sqlite3.connect('card.s3db')
    cursor = connect.cursor()
    cursor.execute("select * from card")
    result = cursor.fetchall()
    connect.close()
    return result


def start_menu():
    data = ''
    while data != '0':
        data = input(f'1. Create an account\n'
                     f'2. Log into account\n'
                     f'0. Exit\n')

        if data == '1':
            print()
            return create_account()
        if data == '2':
            print()
            return log_in()
    print('\nBye!')
    return


def create_card_number():
    number_card = '400000' + str(random.randint(100000000, 1000000000))
    number_card_list = list(number_card)
    new_number_card = ''
    number_sum = 0
    for (index, elem) in enumerate(number_card_list):
        if index % 2 == 0:
            elem = str(int(elem) * 2)
        if int(elem) > 9:
            elem = str(int(elem) - 9)
        new_number_card += elem
        number_sum += int(elem)

    last_digit = 0
    while (number_sum + last_digit) % 10 != 0:
        last_digit += 1

    result_number_card = number_card + str(last_digit)

    return result_number_card


def create_account():
    card_number = create_card_number()
    pin = str(random.randint(1000, 10000))
    insert_data_card(card_number, pin, 0)
    print(f'Your card has been created\n'
          f'Your card number:\n'
          f'{card_number}\n'
          f'Your card PIN:\n'
          f'{pin}\n')
    start_menu()


def log_in():
    check_card = input('Enter your card number: ')
    check_pin = input('Enter your PIN: ')
    data_card = select_card_data()
    for item in data_card:
        if (item[1] == check_card) and (item[2] == check_pin):
            print('\nYou have successfully logged in!\n')
            return sub_menu(item[3])
    print('\nWrong card number or PIN!\n')
    return start_menu()


def sub_menu(value):
    data = ''
    while data != '0':
        data = input(f'1. Balance\n'
                     f'2. Log out\n'
                     f'0. Exit\n')
        if data == '1':
            print(f'\nBalance: {value}\n')
        if data == '2':
            print(f'\nYou have successfully logged out!\n')
            data = '0'
            start_menu()

    return


create_card_bd()
start_menu()

