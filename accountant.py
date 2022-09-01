# -*- coding: utf-8 -*-

ALLOWED_COMMANDS = ("konto", "magazyn", "zakup", "saldo", "przeglad", "exit")

saldo = 1200.0
store = {
    "koszulka": {"price": 50.0, "count": 10},
    "spodnie": {"price": 120.0, "count": 5},
    "kurtka": {"price": 200.0, "count": 3}
    }

operation_history = []

# %%

while True:
    print("_" * 5)
    print(f"Dozwolone komendy: {ALLOWED_COMMANDS}")
    command = input("Wpisz komendę: ")
    command = ''.join(filter(str.isalpha, command)).lower()

    if command not in ALLOWED_COMMANDS:
        print("Niepoprawna komenda!")
        msg = "Użytkownik wprowadził niepoprawną komendę."
        operation_history.append(msg)
        continue

# %% EXIT

    elif command == "exit":
        msg_exit = "Działanie programu zakończone przez użytkownika."
        operation_history.append(msg_exit)
        break

# %% KONTO

    elif command == "konto":
        print(f"Stan konta: {saldo} zł")
        msg_konto = f"Sprawdzono stan konta. Stan konta wynosi: {saldo}"
        operation_history.append(msg_konto)

# %% MAGAZYN

    elif command == "magazyn":
        product_name = input("Nazwa towaru: ")

        product_info = store.get(product_name)

        if product_info:
            print(store[product_name])
        else:
            print(f'Nie ma towaru "{product_name}" w magazynie!')

# %% ZAKUP

    elif command == "zakup":
        product_name = input("Nazwa towaru: ")
        product_price = input("Cena: ")
        product_count = input("Ilość: ")

        product_price = float(product_price)
        product_count = int(product_count)

        product_total_price = (product_price * product_count)

        if product_total_price > saldo:
            print("Posiadasz za mało środków na koncie na zakup takiej ilości "
                  f"towaru za {product_total_price}. Twoje saldo wynosi {saldo}.")
        else:
            saldo -= product_total_price
            if product_name in store.keys():
                store[product_name]["price"] = product_price
                store[product_name]["count"] += product_count
            else:
                store[product_name] = {"price": product_price,
                                       "count": product_count}

        msg_zakup = f"Zakupiono {product_name}."
        operation_history.append(msg_zakup)

# %% SALDO (ZMIANA NA KONCIE)

    elif command == "saldo":
        saldo_change = input("Kwota: ")

        saldo_change = float(saldo_change)

        if (saldo + saldo_change) > 0:
            saldo += saldo_change

            msg_saldo_wplata = (f"Wpłata kwoty {saldo_change} "
                                "na konto zakończona powodzeniem. "
                                f"Twoje saldo wynosi aktualnie {saldo}.")

            msg_saldo_wyplata = (f"Wypłata kwoty {abs(saldo_change)} z konta"
                                 "zakończona powodzeniem. "
                                 f"Twoje saldo wynosi aktualnie {saldo}.")

            if saldo_change > 0:
                operation_history.append(msg_saldo_wplata)
            else:
                operation_history.append(msg_saldo_wyplata)

        else:
            print("Posiadasz za mało środków na koncie na wypłacenie takiej "
                  f"kwoty. Twoje saldo wynosi {saldo, 2}.")

            msg_saldo_abort = ("Wypłata środków zakończona niepowodzeniem. "
                               "Posiadasz za mało środków na koncie na "
                               f"wypłacenie kwoty {abs(saldo_change)}. "
                               f"Twoje saldo wynosi {saldo}.")
            operation_history.append(msg_saldo_abort)

# %% PRZEGLĄD (GENEROWANIE RAPORU)

    elif command == "przeglad":
        msg_przeglad = "Wygenerowano raport."
        operation_history.append(msg_przeglad)
        print("_" * 5 + "\nRaport\n")

        for operation in operation_history:
            print(operation + "\n")

        print("_" * 5 + "\nKoniec raportu\n")

# %%
