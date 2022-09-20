# -*- coding: utf-8 -*-

# define variables
ACCOUNT_BALANCE_FILEPATH = 'account_balance.txt'
STORE_FILEPATH = 'store.csv'

store = []
operation_history = []

# %% define functions
# account balance import function


def read_account_balance():
    account_balance_open = open(ACCOUNT_BALANCE_FILEPATH)
    account_balance_str = account_balance_open.read()
    account_balance = float(account_balance_str)
    return(account_balance)

# define account balance (import from file)


account_balance = read_account_balance()

# account balance display function


def display_account_balance():
    print(account_balance)

# account balance export/save function


def write_account_balance():
    global saldo
    with open(ACCOUNT_BALANCE_FILEPATH, 'w') as file:
        file.write(f"{account_balance}")

# account balance change function


def change_account_balance():
    global account_balance

    while True:
        try:
            account_balance_change = float(input("Kwota: "))
        except ValueError:
            print("Wprowadzony atrybut nie jest liczbą.")
            continue
        else:
            if account_balance_change == 0:
                print("Wprowadzony atrybut to 0 (zero). "
                      "Brak zmiany na koncie")
                pass
            else:
                break

    user_comment = input("Komentarz do wpłaty/wypłaty: ")

    if len(user_comment) == 0:
        comment = "Nie wprowadzono komentarza do zmiany salda."
    else:
        comment = f"Komentarz do zmiany: '{user_comment}'."

    if (account_balance + account_balance_change) > 0:
        account_balance += account_balance_change

        msg_deposit_money = (f"Wpłata kwoty {account_balance_change} "
                             "na konto zakończona powodzeniem. "
                             f"Twoje saldo wynosi aktualnie {account_balance}."
                             f" {comment}")

        msg_withdraw_money = (f"Wypłata kwoty {abs(account_balance_change)} "
                              "z konta zakończona powodzeniem. Twoje saldo "
                              f"wynosi aktualnie {account_balance}. {comment}")

        if account_balance_change > 0:
            operation_history.append((msg_deposit_money))
        else:
            operation_history.append(msg_withdraw_money)

    else:
        print("Posiadasz za mało środków na koncie na wypłacenie takiej "
              f"kwoty. Twoje saldo wynosi {saldo}.")

        msg_abort = ("Wypłata środków zakończona niepowodzeniem. "
                     "Posiadasz za mało środków na koncie na "
                     f"wypłacenie kwoty {abs(account_balance_change)}. "
                     f"Twoje saldo wynosi {saldo}.")
        operation_history.append(msg_abort)

# funtion for generating reports


def generate_report():
    msg_report = "Wygenerowano raport."
    operation_history.append(msg_report)
    print("_" * 5 + "\nRaport\n")

    for operation in operation_history:
        print(operation + "\n")

    print("_" * 5 + "\nKoniec raportu\n")


# %%

# define class


class Product():

    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_file()

    def read_file(self):
        global store
        with open(self.filename, 'r') as file:
            for row in file.readlines():
                splitted_row = row.replace('\n', '').split(',')
                name = splitted_row[0]
                price = float(splitted_row[1])
                count = int(splitted_row[2])

                store_dict = {
                    'product_name': name,
                    'product_price': price,
                    'product_count': count
                    }
                store.append(store_dict)
        return(store)


'''
    def __init__(self, filename):
        self.filename = filename
        self.name = ""
        self.price = None
        self.count = None

    def set_attrs(self):

        product_name = input("Nazwa towaru: ").lower()

        while True:
            try:
                product_price = float(input("Cena: "))
            except ValueError:
                print("Wprowadzony atrybut nie jest liczbą dodatnią.")
                continue
            else:
                if product_price <= 0:
                    print("Cena produktu musi być dodatnia.")
                    pass
                else:
                    break

        while True:
            try:
                product_count = int(input("Ilość: "))
            except ValueError:
                print("Wprowadzony atrybut nie jest liczbą.")
                continue
            else:
                if product_count <= 0:
                    print("Liczba musi być dodatnia.")
                    pass
                else:
                    break

        self.name = product_name
        self.price = product_price
        self.count = product_count
'''
# %% MAIN LOOP

while True:
    command = input("Podaj komendę (saldo/konto/raport/exit): ")
    command = ''.join(filter(str.isalpha, command)).lower()

    if command == "exit":
        write_account_balance()
        break
    elif command == "saldo":
        change_account_balance()
    elif command == "konto":
        display_account_balance()
    elif command == "raport":
        generate_report()
    else:
        print("Niepoprawna komenda!\n"
              "Dozwolone komendy to 'saldo', 'konto', 'raport', 'exit'.")
        pass

# %%

obj = Product(STORE_FILEPATH)
