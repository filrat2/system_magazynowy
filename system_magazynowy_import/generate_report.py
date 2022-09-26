# -*- coding: utf-8 -*-

# function for generating reports for current program working session


def generate_report(operation_history):
    msg_report = "Wygenerowano raport."
    operation_history.append(msg_report)
    print("_" * 5 + "\nRaport\n")

    for operation in operation_history:
        print(operation + "\n")

    print("_" * 5 + "\nKoniec raportu\n")
