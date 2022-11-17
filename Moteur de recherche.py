import csv
import numpy as np
from matplotlib import pyplot as plt
import datetime

with open("Site_IUT_pas_touche.csv", encoding="utf16") as data:
    reader = csv.reader(data, delimiter=",")
    header_row = next(reader)

    Google = 0
    Qwant = 0
    Yahoo = 0
    Ecosia = 0
    Bing = 0
    Usmb = 0
    Autre = 0



    for row in reader:
        if row[51] == "Google":
            Google = Google+1
        if row[51] == "Qwant":
            Qwant = Qwant+1
        if row[51] == "Yahoo":
            Yahoo = Yahoo+1
        if row[51] == "www.univ-smb.fr":
            Usmb = Usmb+1
        if row[51] == "Ecosia":
            Ecosia = Ecosia+1

    name = ['Google','Qwant','Yahoo','USMB','Ecosia']
    data = [Google,Qwant,Yahoo,Usmb,Ecosia]

    explode = (0, 0.15, 0, 0)
    plt.pie(data, startangle=90, autopct='%1.1f%%')
    plt.axis('equal')
    plt.legend(name)
    plt.title("Systèmes d'exploitation des visiteurs du site de l'IUT")
    plt.show()