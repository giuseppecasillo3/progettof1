import pandas as pd
import numpy as np
import unicodedata

circuits = pd.read_csv("circuits.csv")
constructor_results = pd.read_csv("constructor_results.csv")
constructors = pd.read_csv("constructors.csv")
pit_stops = pd.read_csv("pit_stops.csv")
constructor_standings = pd.read_csv("constructor_standings.csv")
driver_standings = pd.read_csv("driver_standings.csv")
drivers = pd.read_csv("drivers.csv")
lap_times = pd.read_csv("lap_times.csv")
qualifying = pd.read_csv("qualifying.csv")
races = pd.read_csv("races.csv")
results = pd.read_csv("results.csv")
seasons = pd.read_csv("seasons.csv")

def Cerca_ID():
    global nome_pista
    global id_pista
    global nome_completo

    for row in circuits.itertuples():
        nome_completo_ricerca=row.name
        if nome_pista.lower() in nome_completo_ricerca.lower():
                nome_completo = nome_completo_ricerca
                id_pista=row.circuitId
        

def Conta_vittorie():
    global id_pista

    vittorie={}

    for row in races.itertuples():
        if id_pista==row.circuitId:
            id_gara=row.raceId
            for row in results.itertuples():
                if id_gara==row.raceId and row.positionText == "1":
                    id_pilota= row.driverId
                    if id_pilota in vittorie:
                        vittorie[id_pilota]+=1
                    else:   
                        vittorie[id_pilota]= 1

    vittorie={k: v for k, v in sorted(vittorie.items(), key=lambda item: item[1], reverse=True)}
    for id,wins in vittorie.items():
        for row in drivers.itertuples():
            if id==row.driverId:
                cognome_pilota= row.surname
                nome_pilota= row.forename
        print(f"{nome_pilota} {cognome_pilota} ({wins})")
                   

def main():
    global nome_pista
    global nome_completo

    nome_pista= input("Inserisci il nome del circuito: ")

    Cerca_ID()
    print(nome_completo)
    Conta_vittorie()

main()

