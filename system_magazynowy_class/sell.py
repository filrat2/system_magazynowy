# -*- coding: utf-8 -*-

# function for sell items from store

def sell(product_name, store, account_balance, operation_history):

    message_fail = (f"Niewystarczająca ilość produktu {product_name}."
                    " Sprzedaż towaru nie może zastać zrealizowana.")

    if (product_name in store.keys() and
            store[product_name]['product_count'] > 0):
        while True:
            try:
                product_count = int(input("Liczba sprzedawanych "
                                          "przedmiotów: "))
            except ValueError:
                print("Wprowadzony atrybut nie jest liczbą.")
                continue
            else:
                if product_count <= 0:
                    print("Liczba musi być dodatnia.")
                    pass
                elif product_count > store[product_name]['product_count']:
                    print("Na stanie znajduje się tylko "
                          f"{store[product_name]['product_count']} sztuk tego "
                          f"produktu {product_name}. Podaj inną liczbę "
                          "sprzedawanych sztuk.")
                    operation_history.append(message_fail)
                    pass
                else:
                    break

        total_purchase = store[product_name]['product_price'] * product_count

        message_sell = (f"Sprzedano {product_count} sztuk produktu "
                        f"{product_name}, którego cena za sztukę wynosi "
                        f"{store[product_name]['product_price']}. Całkowita "
                        f"kwota sprzedaży wynosi {total_purchase}.")

        if product_count <= store[product_name]['product_count']:
            store[product_name]['product_count'] -= product_count
            account_balance += total_purchase
            operation_history.append(message_sell)

    elif (product_name in store.keys() and
          store[product_name]['product_count'] == 0):
        print("Artykuł aktualnie niedostępny.")
        operation_history.append(message_fail)
    else:
        print("Brak artykułu o takiej nazwie.")
