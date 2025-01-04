import pandas as pd
import numpy as np
import unicodedata

# Carica i dati CSV dalla directory corrente
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



def cerca_id_circuito(nome_pista):
    for row in circuits.itertuples():
        if nome_pista.lower() in row.name.lower():
            return row.circuitId
    return None

def trova_race_id_2(anno, id_circuito):
    for row in races.itertuples():
        if row.year == anno and row.circuitId == id_circuito:
            return row.raceId
    return None

def Trova_id_pilota(nome_pilota, cognome_pilota):
    global id_pilota
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
            return

def differenza_posizioni():
    anno = int(input("Inserisci l'anno: \n"))
    nome_pista = input("Inserisci nome del Gran Premio: \n")
    id_circuito = cerca_id_circuito(nome_pista)
    
    if not id_circuito:
        print("Circuito non trovato.")
        return

    nome_pilota = input("Inserisci nome pilota: \n")
    cognome_pilota = input("Inserisci cognome pilota: \n")
    
    # Trova id del pilota
    Trova_id_pilota(nome_pilota, cognome_pilota)
    pilota_id = id_pilota  # Ottieni id pilota

    gara_id = trova_race_id_2(anno, id_circuito)
    
    if not gara_id:
        print("Gara non trovata.")
        return

    # Filtra i risultati per la gara e il pilota specifici
    change_positions = results[(results['raceId'] == gara_id) & (results['driverId'] == pilota_id)]

    if change_positions.empty:
        print("Nessun risultato trovato per questo pilota in questa gara")
        return None  # Nessun risultato trovato per questo pilota in questa gara

    for index, result in change_positions.iterrows():
        grid = result['grid']
        position = result['position']

        # Verifica se il pilota ha completato la gara
        if position == '\\N' or pd.isna(position):  # Se la posizione è NaN o '\\N', significa che il pilota non ha finito
            print("Il pilota non ha finito la gara")
        else:
            position = int(position)  # Assicurarsi che la posizione sia un intero
            grid = int(grid)  # Assicurarsi che la griglia sia un intero

            # Confronto tra la posizione di grid e la posizione in gara
            if position < grid:  # Se la posizione in gara è migliore della posizione di partenza
                difference_positions = grid - position  # Guadagnato
                print(f"Il pilota ha guadagnato {difference_positions} posizioni")
            elif position > grid:  # Se la posizione in gara è peggiore
                difference_positions = position - grid  # Perso
                print(f"Il pilota ha perso {difference_positions} posizioni")
            else:  # Se la posizione è la stessa della qualifica
                print(f"Il pilota ha mantenuto la stessa posizione di qualifica")

differenza_posizioni()







def trova_pilota_vincitore():
    anno = int(input("Inserisci l'anno: \n"))
    nome_pista = input("Inserisci nome del Gran Premio: \n")
    id_circuito = cerca_id_circuito(nome_pista)
    if not id_circuito:
        print("Circuito non trovato.")
        return

