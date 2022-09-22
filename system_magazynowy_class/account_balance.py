# -*- coding: utf-8 -*-

# %% account balance import function


def read_account_balance(account_balance_file):
    account_balance_open = open(account_balance_file)
    account_balance_str = account_balance_open.read()
    account_balance = float(account_balance_str)
    return(account_balance)


# %% account balance export/save function


def write_account_balance(account_balance, account_balance_file):
    with open(account_balance_file, 'w') as file:
        file.write(f"{account_balance}")

# %% account balance display function


def display_account_balance(account_balance):
    print(account_balance)


# %% account balance change function


def change_account_balance(account_balance, operation_history):

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
        # return account_balance

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
              f"kwoty. Twoje saldo wynosi {account_balance}.")

        msg_fail = ("Wypłata środków zakończona niepowodzeniem. "
                    "Posiadasz za mało środków na koncie na "
                    f"wypłacenie kwoty {abs(account_balance_change)}. "
                    f"Twoje saldo wynosi {account_balance}.")
        operation_history.append(msg_fail)

    # return account_balance

# %%
