import csv
import numpy as np
from matplotlib import pyplot as plt
import datetime

with open("Site_IUT_pas_touche.csv", encoding="utf16") as data:
    reader = csv.reader(data, delimiter=",")
    header_row = next(reader)

    ios = 0
    mac = 0
    android = 0
    Windows = 0
    linux = 0



    for row in reader:
        if row[66] == "GNU/Linux":
            linux = linux+1

        if row[66] == "Android":
            android = android+1

        if row[66] == "Mac":
            mac = mac+1

        if row[66] == "Windows":
            Windows = Windows+1

        if row[66] == "iOS":
            ios = ios+1

    name = ['Android', 'iOS', 'Windows', 'Linux', 'Mac']
    data = [android, ios, Windows, linux, mac]

    explode = (0, 0.15, 0, 0)
    plt.pie(data, startangle=90, autopct='%1.1f%%')
    plt.axis('equal')
    plt.legend(name)
    plt.title("Systèmes d'exploitation des visiteurs du site de l'IUT")
    plt.show()
