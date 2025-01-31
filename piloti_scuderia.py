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
    global nome_scuderia
    global id_scuderia

    for row in constructors.itertuples():
        if nome_scuderia.lower() == row.name.lower():
            id_scuderia=row.constructorId

def Cerca_piloti():
    global id_scuderia

    presenze={}

    for row in results.itertuples():
        if id_scuderia==row.constructorId:
            id_pilota= row.driverId
            if id_pilota in presenze:
                presenze[id_pilota]+=1
            else:
                presenze[id_pilota]=1

    presenze={k: v for k, v in sorted(presenze.items(), key=lambda item: item[1], reverse=True)}
    for id,race in presenze.items():
        for row in drivers.itertuples():
            if id==row.driverId:
                cognome_pilota= row.surname
                nome_pilota= row.forename
        print(f"{nome_pilota} {cognome_pilota} ({race})")
                        
                        
                    


def main():
    global nome_scuderia
    global id_scuderia

    nome_scuderia = input("Inserisci il nome della scuderia: ")

    Cerca_ID()
    Cerca_piloti()

    

main()