from tkinter import *
import tkinter.scrolledtext as tkscrolled
from tkinter import messagebox
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from covid import Covid
import numpy

root = Tk()
root.geometry("380x310")
root.title("Grafico Dati Covid-19")


def showData():
    covid = Covid()
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    try:
        root.update()
        countries = entry.get("1.0", END)
        country_names = countries.strip()       #strip rimuove spazi iniziali e finali
        country_names = country_names.splitlines()

        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            root.update()
        for y in cases:
            confirmed.append(y["confirmed"])
            active.append(y["active"])
            deaths.append(y["deaths"])
            recovered.append(y["recovered"])
        
        confirmed_patch = mpatches.Patch(color="green", label="Confermati")
        recovered_patch = mpatches.Patch(color="red", label="Guariti")
        active_patch = mpatches.Patch(color="blue", label="Attivi")
        deaths_patch = mpatches.Patch(color="Black", label="Decessi")

        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])

        x = numpy.arange(4)
        bar_width=0.15
        for x in range(len(country_names)):
            plt.bar(x, confirmed[x], width=bar_width, color="green", zorder=2)
            plt.bar(x + bar_width, active[x], width=bar_width, color="blue", zorder=2)
            plt.bar(x + bar_width*2, recovered[x], width=bar_width, color="red", zorder=2)
            plt.bar(x + bar_width*3, deaths[x], width=bar_width, color="black", zorder=2)
            
        plt.xticks(numpy.arange(len(country_names)) + bar_width*1.5, country_names)
        plt.title("Casi attuali COVID-19")
        plt.xlabel("Nomi nazioni")
        plt.ylabel("Casi in milioni")
        plt.show()
    except Exception as e:
        messagebox.showerror(title="Errore", message="Inserisci i dati correttamente")
        print(e)


Label(root, text="Dati Covid-19", font="Consolas 13 bold").pack()
Label(root, text="Inserisci i nomi delle nazioni separandole andando a capo:").pack()
entry = tkscrolled.ScrolledText(root, width=50, height=12, wrap=WORD)
entry.pack(padx=10, pady=5)
Button(root, text="Ottieni dati", command=showData).pack(pady=5)

if __name__ == "__main__":
    root.mainloop()