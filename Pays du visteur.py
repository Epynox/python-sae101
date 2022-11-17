import csv
import numpy as np
from matplotlib import pyplot as plt
import datetime

with open("Site_IUT_pas_touche.csv", encoding="utf16") as data:
    reader = csv.reader(data, delimiter=",")
    header_row = next(reader)

    France = 0
    Usa = 0
    Maroc = 0
    Suisse = 0
    Autre = 0



    for row in reader:
        if row[86] == "France":
            France = France+1

        if row[86] == "Usa":
            Usa = Usa+1

        if row[86] == "Maroc":
            Maroc = Maroc+1

        if row[86] == "Suisse":
            Suisse = Suisse+1


    name = ['France', 'Usa', 'Maroc', 'Suisse']
    data = [France, Usa, Maroc, Suisse]

    explode = (0, 0.15, 0, 0)
    plt.pie(data, startangle=90, autopct='%1.1f%%')
    plt.axis('equal')
    plt.legend(name)
    plt.title("Systèmes d'exploitation des visiteurs du site de")
    plt.show()