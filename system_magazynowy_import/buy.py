# -*- coding: utf-8 -*-

# function to buy items for your store

def buy(product_name, store, account_balance, operation_history):

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

    product_total_price = (product_price * product_count)

    message_fail = ("Niewystarczające środki na koncie. Zakup towaru nie "
                    "może być zrealziowany.")

    message_buy = (f"Zakupiono {product_count} sztuk produktu "
                   f"{product_name}, którego cena za sztukę wynosi "
                   f"{product_price}. "
                   f"Całkowita kwota zakupu wynosi {product_total_price}.")

    if product_total_price > account_balance:
        print("Posiadasz za mało środków na koncie na zakup takiej ilości "
              f"towaru za {product_total_price}. Twoje saldo wynosi "
              f"{account_balance}.")
        operation_history.append(message_fail)
    else:
        operation_history.append(message_buy)
        account_balance -= product_total_price
        if product_name in store.keys():
            store[product_name]['product_price'] = product_price
            store[product_name]['product_count'] += product_count
        else:
            store[product_name] = {'product_price': product_price,
                                   'product_count': product_count}
    return account_balance
