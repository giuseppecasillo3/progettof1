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


def Cerca_ID_circuito(nome_pista):
    id_pista=0
    for row in circuits.itertuples():
        nome_completo_ricerca=row.name
        if nome_pista.lower() in nome_completo_ricerca.lower():
                nome_completo = nome_completo_ricerca
                id_pista=row.circuitId
    if id_pista==0:
        return id_pista, nome_pista
    else:
        return id_pista, nome_completo


def Conta_vittorie_per_circuito(id_pista):

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
        print(f"\n{nome_pilota} {cognome_pilota} ({wins})")


def Cerca_ID_scuderia(nome_scuderia):
    id_scuderia=0
    for row in constructors.itertuples():
        if nome_scuderia.lower() == row.name.lower():
            id_scuderia=row.constructorId
    return id_scuderia


def Cerca_piloti_per_scuderia(id_scuderia):
    

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
        print(f"\n{nome_pilota} {cognome_pilota} ({race})")

def Cerca_ID_pilota(nome_pilota,cognome_pilota):
    id_pilota=0
    #cerco l'id del pilota tramite nome e cognome
    for row in drivers.itertuples():
       nome_pilota_db = row.forename
       cognome_pilota_db = row.surname

       nome_normalizzato_db = unicodedata.normalize('NFD', nome_pilota_db)
       nome_pilota_senza_accenti_db = ''.join(c for c in nome_normalizzato_db if unicodedata.category(c) != 'Mn')

       cognome_normalizzato_db = unicodedata.normalize('NFD', cognome_pilota_db)
       cognome_pilota_senza_accenti_db = ''.join(c for c in cognome_normalizzato_db if unicodedata.category(c) != 'Mn')

       if nome_pilota.lower().strip() == nome_pilota_senza_accenti_db.lower().strip() and cognome_pilota.lower().strip() == cognome_pilota_senza_accenti_db.lower().strip():
          id_pilota = row.driverId
    return id_pilota

def Conta_vittorie_pilota(id_pilota):
    
    wins = 0
    race = 0
    # conto gare corse e vittorie
    for row in results.itertuples():
        if row.driverId == id_pilota:
            race = race +1 
            if row.positionText == "1":
             wins = wins + 1
             
    if race == 0:
       percentuale_vittorie = 0
    elif race > 0 and wins == 0:
       percentuale_vittorie = 0
    elif race > 0 and wins > 0:
        #calcolo percentuale e riduco il numero delle cifre dopo la virgola
        percentuale_vittorie= (wins * 100)/race
        percentuale_vittorie= round(percentuale_vittorie, 3)

    return race, wins, percentuale_vittorie
    
def Conta_Podi(id_pilota):

   podi = 0

   for row in results.itertuples():
      if row.driverId == id_pilota:
         if row.positionText == "1" or row.positionText == "2" or row.positionText == "3":
            podi = podi + 1
   return podi

def Percentuale_vittorie_pilota(nome_pilota, cognome_pilota):
    id_pilota= Cerca_ID_pilota(nome_pilota,cognome_pilota)
    if id_pilota==0:
        print("pilota non trovato")
    else:
        gare_vinte = Conta_vittorie_pilota(id_pilota)
        numero_podi= Conta_Podi(id_pilota)
    
        if gare_vinte[1]==0 and numero_podi >0:
            print(f"\n{nome_pilota} {cognome_pilota} ha corso {gare_vinte[0]} gare ma non ha mai vinto,\nma ha ottuneto {numero_podi} podi")
        elif gare_vinte[1]==0 and numero_podi==0:
            print(f"\n{nome_pilota} {cognome_pilota} ha corso {gare_vinte[0]} gare in F1")
        else:
            print(f"\n{nome_pilota} {cognome_pilota} ha corso {gare_vinte[0]} gare,\nha ottenuto {numero_podi} podi di cui {gare_vinte[1]} gare vinte,\ncon una percentuale di vittoria del {gare_vinte[2]}%.")

def Piloti_per_scuderia(nome_scuderia):
    id_scuderia= Cerca_ID_scuderia(nome_scuderia)
    if id_scuderia==0:
        print("Scuderia non trovata")
    else:
        Cerca_piloti_per_scuderia(id_scuderia)

def Albo_oro_circuito(nome_pista):
    id_pista, nome_completo = Cerca_ID_circuito(nome_pista)
    if id_pista==0:
        print("circuito non trovato")
    else:   
        print(f"\nAlbo d'oro del circuito {nome_completo}")
        Conta_vittorie_per_circuito(id_pista)