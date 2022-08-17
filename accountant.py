# -*- coding: utf-8 -*-

# import needed modules
import sys

if len(sys.argv) < 2:
    print("Error! Wprowadzono zbyt mało atrybutów. "
          "Działanie programu zakończone.")
    exit()
elif sys.argv[1] == 'saldo':
    print('saldo')
elif sys.argv[1] == 'sprzedaz':
    print('sprzedaz')
elif sys.argv[1] == 'zakup':
    print('zakup')
elif sys.argv[1] == 'konto':
    print('konto')
elif sys.argv[1] == 'magazyn':
    print('magazyn')
elif sys.argv[1] == 'przeglad':
    print('przeglad')
else:
    print("Error! Wprowadzono nieprawidłową akcję. "
          "Działanie programu zakończone.")
    exit()
