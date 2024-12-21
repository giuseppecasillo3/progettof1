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
        nome_completo_ricerca =[]
        nome_completo_ricerca.append(row.name)

        for i in nome_completo_ricerca: 
            if nome_pista.lower() in i.lower():
                nome_completo = i
                id_pista=row.circuitId
        
        
    

def Conta_vittorie():
    global id_pista

    lista_id=[]

    for row in races.itertuples():
        if id_pista==row.circuitId:
            id_gara=row.raceId
            for row in results.itertuples():
                if id_gara==row.raceId and row.positionText == "1":
                    id_pilota= row.driverId
                    if id_pilota not in lista_id:
                        lista_id.append(id_pilota)
                        for row in drivers.itertuples():
                            if id_pilota==row.driverId:
                                cognome_pilota= row.surname
                                nome_pilota= row.forename
                                wins = 0
                                for row in results.itertuples():
                                    if id_pilota==row.driverId and row.positionText == "1":
                                        wins = wins + 1
                                print(f"{nome_pilota} {cognome_pilota} ({wins})")



        

def main():
    global nome_pista
    global nome_completo

    nome_pista= input("Inserisci il nome del circuito: ")

    Cerca_ID()
    print(nome_completo)
    Conta_vittorie()

main()
