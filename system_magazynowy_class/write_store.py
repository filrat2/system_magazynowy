# -*- coding: utf-8 -*-

# function for export/save products to *.csv file

def write_store(store, filename):
    with open(filename, 'w') as file:
        for product in store.keys():
            product_name = product
            product_price = store[product]['product_price']
            product_count = store[product]['product_count']
            file.write(f"{product_name},{product_price},{product_count}\n")
