# -*- coding: utf-8 -*-

# function for checking stock

def warehouse_checker(product_name, store, operation_history):

    product_info = store.get(product_name)

    message = f"Sprawdzono stan magazynowy przedmiotu {product_name}."

    message_no_item = (f"Sprawdzono stan magazynowy przedmiotu {product_name}"
                       f". Nie ma towaru '{product_name}' w magazynie!")

    if product_info:
        print(store[product_name])
        operation_history.append(message)
    else:
        print(f'Nie ma towaru "{product_name}" w magazynie!')
        operation_history.append(message_no_item)
