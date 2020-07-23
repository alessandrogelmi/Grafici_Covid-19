from covid import Covid
import os

clear = lambda: os.system('cls')
clear()

def formatNumber(x):
    return ("{:,}".format(x)) 

covid = Covid()

print("Totale casi nel mondo: ", formatNumber(covid.get_total_confirmed_cases()))
print("Totale guariti mondo", formatNumber(covid.get_total_recovered()))
print("Totale decessi nel mondo: ", formatNumber(covid.get_total_deaths()))

print("\n------\n")

print("Totale casi attivi nel mondo: ", formatNumber(covid.get_total_active_cases()))

state=input("\nInserisci la nazione per la quale si vogliono ottenere i dati: ")
clear()
data = covid.get_status_by_country_name(state)

try:
    print("Casi confermati: ", formatNumber(data["confirmed"]))
    print("Casi attivi: ", formatNumber(data["active"]))
    print("Totale decessi: ", formatNumber(data["deaths"]))
except ValueError as e:
    print(e)
