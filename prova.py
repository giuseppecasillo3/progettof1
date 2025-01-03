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



# Funzione per calcolare la durata di gara per ogni anno per un circuito e pilota specifici
def durata_gara(driver_id, circuit_id):
    # Filtra le gare che si sono svolte sul circuito specifico
    circuit_races = races[races['circuitId'] == circuit_id]

    # Lista per memorizzare le durate delle gare (anno, durata totale in secondi)
    race_durations = []

    # Itera su ogni gara del circuito (ogni riga del DataFrame filtrato)
    for index, race in circuit_races.iterrows():
        # Estrai l'ID della gara e l'anno
        race_id = race['raceId']
        year = race['year']
        
        # Filtra i tempi di giro per la gara specifica e il pilota specifico
        driver_lap_times = lap_times[(lap_times['raceId'] == race_id) & (lap_times['driverId'] == driver_id)]

        # Controlla se esistono dati per i tempi di giro del pilota in quella gara
        if not driver_lap_times.empty:
            # Somma tutti i tempi di giro del pilota in millisecondi e converti in secondi
            total_race_time = driver_lap_times['milliseconds'].sum() / 1000

            # Aggiungi una tupla contenente l'anno della gara e la durata totale alla lista
            race_durations.append((year, total_race_time))
            # Ordina le durate per anno
            race_durations.sort()

    # Restituisci la lista delle durate di gara
    return race_durations

# Funzione per visualizzare la durata della gara nel tempo per un circuito e un pilota specifici
def grafico_durata_gara(driver_id, circuit_id):
    # Calcola le durate di gara per ogni anno
    race_durations = durata_gara(driver_id, circuit_id)
    
    if not race_durations:
        print("Nessun dato disponibile per il pilota e il circuito specificati.")
        return
    
    # Separiamo gli anni e le durate per creare il grafico
    years, durations = zip(*race_durations)
    
    # Print delle durate per ogni anno
    print("Durata della gara per ogni anno:")
    for year, duration in race_durations:
        print(f"Anno {year}: {duration:.2f} secondi")
    
    # Creazione del grafico
    plt.figure(figsize=(10, 6))
    plt.plot(years, durations, marker='o', linestyle='-', color='blue')
    plt.xlabel('Anno')
    plt.ylabel('Durata della gara (secondi)')
    plt.title(f"Durata della gara nel tempo per il pilota {driver_id} sul circuito {circuit_id}")
    plt.grid(True)
    plt.show()




# nome_pilota = input("Inserisci il nome del pilota: ").strip()
# cognome_pilota = input("Inserisci il cognome del pilota: ").strip()
# nome_pista = input("Inserisci il nome del circuito: ").strip()


# driver_id = cerca_id_pilota(nome_pilota, cognome_pilota)
# circuit_id = cerca_id_circuito(nome_pista)

# if driver_id is not None and circuit_id is not None:
#     grafico_durata_gara(driver_id, circuit_id)
# else:
#     print("Impossibile generare il grafico. Controlla che pilota e circuito esistano nei dati.")