# -*- coding: utf-8 -*-

# function for import store stock from *.csv file

def read_store(store, filename):
    with open(filename, 'r') as file:
        for row in file.readlines():
            splitted_row = row.replace('\n', '').split(',')
            name = splitted_row[0]
            price = float(splitted_row[1])
            count = int(splitted_row[2])

            store_dict = {
                'product_price': price,
                'product_count': count
                }
            store[name] = store_dict
    return(store)
