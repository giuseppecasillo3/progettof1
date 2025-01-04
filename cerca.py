import pandas as pd
import matplotlib.pyplot as plt
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

def cerca_id_pilota(nome_pilota, cognome_pilota):
    for row in drivers.itertuples():
        nome_normalizzato_db = unicodedata.normalize('NFD', row.forename)
        nome_pilota_senza_accenti_db = ''.join(c for c in nome_normalizzato_db if unicodedata.category(c) != 'Mn')

        cognome_normalizzato_db = unicodedata.normalize('NFD', row.surname)
        cognome_pilota_senza_accenti_db = ''.join(c for c in cognome_normalizzato_db if unicodedata.category(c) != 'Mn')

        if nome_pilota.lower() == nome_pilota_senza_accenti_db.lower() and cognome_pilota.lower() == cognome_pilota_senza_accenti_db.lower():
            return row.driverId
    return None

def cerca_id_circuito(nome_pista):
    for row in circuits.itertuples():
        if nome_pista.lower() in row.name.lower():
            return row.circuitId
    return None


def cerca_id_scuderia(nome_scuderia): 
    for row in constructors.itertuples():
        if nome_scuderia.lower() == row.name.lower():
            return row.constructorId
    return None