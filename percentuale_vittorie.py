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

id_pilota = 0


def Trova_id_pilota():
    global id_pilota
    global nome_pilota
    global cognome_pilota

    #cerco l'id del pilota tramite nome e cognome
    for row in drivers.itertuples():
       nome_pilota_db = row.forename
       cognome_pilota_db = row.surname

       nome_normalizzato_db = unicodedata.normalize('NFD', nome_pilota_db)
       nome_pilota_senza_accenti_db = ''.join(c for c in nome_normalizzato_db if unicodedata.category(c) != 'Mn')

       cognome_normalizzato_db = unicodedata.normalize('NFD', cognome_pilota_db)
       cognome_pilota_senza_accenti_db = ''.join(c for c in cognome_normalizzato_db if unicodedata.category(c) != 'Mn')

       if nome_pilota.lower() == nome_pilota_senza_accenti_db.lower() and cognome_pilota.lower() == cognome_pilota_senza_accenti_db.lower():
          id_pilota = row.driverId

    

def Conta_vittorie_pilota():
    global id_pilota
    global nome_pilota
    global cognome_pilota

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
    
    
def Conta_Podi():
   global id_pilota
   global nome_pilota
   global cognome_pilota

   podi = 0

   for row in results.itertuples():
      if row.driverId == id_pilota:
         if row.positionText == "1" or row.positionText == "2" or row.positionText == "3":
            podi = podi + 1
   return podi

def Conta_pole():
   global id_pilota

   pole = 0

   for row in qualifying.itertuples():
      if row.driverId == id_pilota:
         if int(row.position) == int(1):
            pole = pole + 1
   return pole


def main():
   global id_pilota
   global nome_pilota
   global cognome_pilota

   nome_pilota = input("inserisci il nome del pilota: ")
   cognome_pilota = input("inserisci il cognome del pilota: ")

   Trova_id_pilota()
   gare_vinte = Conta_vittorie_pilota()
   numero_podi= Conta_Podi()
   
   if gare_vinte[1]==0 and numero_podi >0:
      print(f"{nome_pilota} {cognome_pilota} ha corso {gare_vinte[0]} gare ma non ha mai vinto,\nma ha ottuneto {numero_podi} podi")
   elif gare_vinte[1]==0 and numero_podi==0:
      print(f"{nome_pilota} {cognome_pilota} ha corso {gare_vinte[0]} gare in F1")
   else:
      print(f"{nome_pilota} {cognome_pilota} ha corso {gare_vinte[0]} gare,\nha ottenuto {numero_podi} podi di cui {gare_vinte[1]} gare vinte,\ncon una percentuale di vittoria del {gare_vinte[2]}%.")
   
main()
   


