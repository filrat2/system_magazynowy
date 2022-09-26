# -*- coding: utf-8 -*-

# import needed functions / modules

from read_store import read_store
from write_store import write_store
from account_balance import (
    read_account_balance,
    write_account_balance,
    change_account_balance
    )
from generate_report import generate_report
from sell import sell
from buy import buy
from warehouse import warehouse_checker

# define variables

ACCOUNT_BALANCE_FILEPATH = 'account_balance.txt'
STORE_FILEPATH = 'store.csv'
operation_history = []
store = {}
read_store(store, STORE_FILEPATH)

# define account balance (import from file)
account_balance = read_account_balance(ACCOUNT_BALANCE_FILEPATH)

# %% MAIN LOOP

while True:
    command = input("Podaj komendę (sprzedaz/kupno/magazyn/saldo/konto/raport"
                    "/exit): ")
    command = ''.join(filter(str.isalpha, command)).lower()

    if command == "exit":
        write_account_balance(account_balance, ACCOUNT_BALANCE_FILEPATH)
        write_store(store, STORE_FILEPATH)
        break

    elif command == "sprzedaz":
        product_name = input("Nazwa towaru: ").lower()
        account_balance = sell(product_name, store, account_balance,
                               operation_history)

    elif command == "kupno":
        product_name = input("Nazwa towaru: ").lower()
        account_balance = buy(product_name, store, account_balance,
                              operation_history)

    elif command == "magazyn":
        product_name = input("Nazwa towaru: ").lower()
        warehouse_checker(product_name, store, operation_history)

    elif command == "saldo":
        account_balance = change_account_balance(account_balance,
                                                 operation_history)

    elif command == "konto":
        print(account_balance)

    elif command == "raport":
        generate_report(operation_history)

    else:
        print("Niepoprawna komenda!\n"
              "Dozwolone komendy to 'sprzedaz', 'kupno', 'magazyn', 'saldo', "
              "'konto', 'raport', 'exit'.")
        pass

# %%
