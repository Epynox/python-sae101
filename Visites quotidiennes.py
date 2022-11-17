import csv
import numpy
from matplotlib import pyplot as plt
from datetime import datetime
filename = "Site_IUT_pas_touche.csv"

with open(filename, encoding="utf16") as f:
    reader = csv.reader(f, delimiter=",")
    header_row = next(reader)
    toutesvisites = []
    jour_init = 30
    visites = 0
    nb_elements = 0
    for row in reader:
        nb_elements = nb_elements + 1
        if row[10] == "":
            continue
        date = datetime.strptime(row[10], "%d %B %Y %H:%M:%S")
        if date.day != jour_init:
            toutesvisites.append(visites)
            jour_init = date.day
            visites = 0
        visites = visites+1
    toutesvisites.append(nb_elements-sum(toutesvisites))
    for i in range(len(toutesvisites)):
        valeur_min = toutesvisites[i]
        valeur_max = toutesvisites[i]
    if valeur_min >= toutesvisites[i]:
        valeur_min = toutesvisites[i]
        indice_min = i+1
    if valeur_max <= toutesvisites[i]:
        valeur_max = toutesvisites[i]
        indice_max = i+1
    moyenne_visites = sum(toutesvisites)/len(toutesvisites)
    print("Le site à été visité", sum(toutesvisites), "fois")

    jours = numpy.linspace(30, 1, 30)
    fig = plt.figure("Visites quotidiennes", dpi=128, figsize=(10, 6))
    plt.plot(jours, toutesvisites, c="red", marker="x")
    plt.title("Visite quotidienne site IUT", fontsize=24)
    plt.xlabel("Jour du mois", fontsize=16)
    plt.xlabel("Nombre de visites", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)
    plt.grid(True)
    plt.show()