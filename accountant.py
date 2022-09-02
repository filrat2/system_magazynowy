# -*- coding: utf-8 -*-

ALLOWED_COMMANDS = ("sprzedaz", "zakup", "saldo", "konto", "magazyn",
                    "przeglad", "exit")

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
        break

# %% KONTO

    elif command == "konto":
        print(f"Stan konta: {saldo} zł")
        msg_konto = f"Sprawdzono stan konta. Stan konta wynosi: {saldo}"
        operation_history.append(msg_konto)

# %% MAGAZYN

    elif command == "magazyn":
        product_name = input("Nazwa towaru: ").lower()

        product_info = store.get(product_name)

        msg_magazyn1 = f"Sprawdzono stan magazynowy przedmiotu {product_name}."

        msg_magazyn2 = (f"Sprawdzono stan magazynowy przedmiotu {product_name}."
                        f" Nie ma towaru '{product_name}' w magazynie!")

        if product_info:
            print(store[product_name])
            operation_history.append(msg_magazyn1)
        else:
            print(f'Nie ma towaru "{product_name}" w magazynie!')
            operation_history.append(msg_magazyn2)

# %% SPRZEDAZ

    elif command == 'sprzedaz':
        product_name = input("Nazwa towaru: ").lower()

        if product_name in store.keys() and store[product_name]['count'] > 0:

            while True:
                try:
                    product_count = int(input("Liczba sprzedawanych "
                                              "przedmiotów: "))
                    if product_count <= 0:
                        raise ValueError()
                except ValueError:
                    print("Wprowadzony atrybut nie jest liczbą całkowitą "
                          "dodatnią.")
                    continue
                else:
                    break

            if product_count <= store[product_name]["count"]:
                store[product_name]["count"] -= product_count
                saldo += store[product_name]["price"] * product_count
            else:
                print("Niewystarczająca ilość produktu. "
                      "Na magazynie znajduje się tylko "
                      f"{store[product_name]['count']} sztuk tego produktu.")

        elif store[product_name]["count"] == 0:
            print("Artykuł aktualnie niedostępny.")
        else:
            print("Brak artykułu o takiej nazwie.")

# pytanie czy przerwać transakcję?
# ponowny input z inną ilością?

# %% ZAKUP

    elif command == "zakup":
        product_name = input("Nazwa towaru: ").lower()

        while True:
            try:
                product_price = float(input("Cena: "))
                if product_price <= 0:
                    raise ValueError()
            except ValueError:
                print("Wprowadzony atrybut nie jest liczbą dodatnią.")
                continue
            else:
                break

        while True:
            try:
                product_count = int(input("Ilość: "))
                if product_count <= 0:
                    raise ValueError()
            except ValueError:
                print("Wprowadzony atrybut nie jest liczbą całkowitą "
                      "dodatnią.")
                continue
            else:
                break

        product_total_price = (product_price * product_count)

        msg_zakup1 = ("Niewystarczające środki na koncie. Zakup towaru nie "
                      "może być zrealziowany.")

        msg_zakup2 = (f"Zakupiono {product_count} sztuk produktu "
                      f"{product_name}, którego cena za sztukę wynosi "
                      f"{product_price}. "
                      f"Całkowita kwota zakupu wynosi {product_total_price}.")

        if product_total_price > saldo:
            print("Posiadasz za mało środków na koncie na zakup takiej ilości "
                  f"towaru za {product_total_price}. Twoje saldo wynosi "
                  f"{saldo}.")
            operation_history.append(msg_zakup1)
        else:
            operation_history.append(msg_zakup2)
            saldo -= product_total_price
            if product_name in store.keys():
                store[product_name]["price"] = product_price
                store[product_name]["count"] += product_count
            else:
                store[product_name] = {"price": product_price,
                                       "count": product_count}

# %% SALDO (ZMIANA NA KONCIE)

    elif command == "saldo":
        while True:
            try:
                saldo_change = float(input("Kwota: "))
            except ValueError:
                print("Wprowadzony atrybut nie jest liczbą.")
                continue
            else:
                break

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
                  f"kwoty. Twoje saldo wynosi {saldo}.")

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
