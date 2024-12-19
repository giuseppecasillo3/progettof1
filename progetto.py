import pandas as pd
import matplotlib.pyplot as plt

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

# Funzione per visualizzare i punti accumulati da una scuderia su un circuito specifico nel tempo
def grafico_punti_scuderia(constructor_id, circuit_id):
    # Filtra le gare per il circuito specifico
    circuit_races = races[races['circuitId'] == circuit_id]
    
    points_by_season = []

    # Per ogni gara del circuito, calcola i punti accumulati dalla scuderia in quella stagione
    for index, race in circuit_races.iterrows():
        race_id = race['raceId']
        year = race['year']
        
        # Filtra i risultati della scuderia per la gara specifica e somma i punti
        constructor_results_race = results[(results['raceId'] == race_id) & (results['constructorId'] == constructor_id)]
        if not constructor_results_race.empty:
            total_points = constructor_results_race['points'].sum()

            # Aggiungi l'anno e i punti totali alla lista
            points_by_season.append((year, total_points))

    # Ordina i punti per anno
    points_by_season.sort()
    
    if not points_by_season:
        print("Nessun dato disponibile per la scuderia e il circuito specificati.")
        return

    # Separiamo gli anni e i punti per creare il grafico
    years, points = zip(*points_by_season)
    
    # Print dei punti per ogni anno
    print("Punti accumulati per ogni anno:")
    for year, point in points_by_season:
        print(f"Anno {year}: {point:.2f} punti")
    
    # Creazione del grafico
    plt.figure(figsize=(10, 6))
    plt.plot(years, points, marker='o', linestyle='-', color='green')
    plt.xlabel('Anno')
    plt.ylabel('Punti')
    plt.title(f"Punti accumulati nel tempo per la scuderia {constructor_id} sul circuito {circuit_id}")
    plt.grid(True)
    plt.show()

# Funzione per calcolare i punti di una scuderia nei diversi anni e tracciarne il grafico

def grafico_punti_totali_scuderia(constructor_id):
    punti_per_anno = []

    # Ciclo attraverso gli anni unici nelle gare
    for year in races['year'].unique():
        gare_anno = races[races['year'] == year]
        # Filtra i risultati della scuderia per le gare di quell'anno
        punti_anno = results[(results['raceId'].isin(gare_anno['raceId'])) & (results['constructorId'] == constructor_id)]
        
        if not punti_anno.empty:
            # Calcola la somma dei punti per quell'anno
            somma_punti = punti_anno['points'].sum()
            punti_per_anno.append((year, somma_punti))
    
    # Ordina i dati per anno
    punti_per_anno.sort()

    # Se ci sono dati da visualizzare
    if punti_per_anno:
        # Estrai gli anni e i punti
        anni, punti = zip(*punti_per_anno)

        # Creazione del grafico
        plt.figure(figsize=(10, 6))
        plt.plot(anni, punti, marker='o', linestyle='-', color='purple')
        plt.xlabel('Anno')
        plt.ylabel('Punti Totali')
        plt.title(f"Punti totali della scuderia {constructor_id} nel tempo")
        plt.grid(True)
        plt.show()
    else:
        print(f"Nessun dato disponibile per la scuderia {constructor_id}")

# Funzione per calcolare la media dei pit stop di un pilota nei diversi anni e tracciarne il grafico
def grafico_media_pit_stop(driver_id):
    media_pit_stop_per_anno = []

    for year in races['year'].unique():
        gare_anno = races[races['year'] == year]
        pit_stop_anno = pit_stops[(pit_stops['raceId'].isin(gare_anno['raceId'])) & (pit_stops['driverId'] == driver_id)]
        pit_stop_media = pit_stop_anno['milliseconds'].mean()/1000
        media_pit_stop_per_anno.append((year, pit_stop_media))

    media_pit_stop_per_anno.sort()

    anni, medie = zip(*media_pit_stop_per_anno)

    # Creazione del grafico
    plt.figure(figsize=(10, 6))
    plt.plot(anni, medie, marker='o', linestyle='-', color='orange')
    plt.xlabel('Anno')
    plt.ylabel('Media Pit Stop')
    plt.title(f"Media dei pit stop per il pilota {driver_id} nel tempo")
    plt.grid(True)
    plt.show()

# Funzione per calcolare la posizione finale di un pilota nei diversi anni e tracciarne il grafico
def grafico_posizione_media(driver_id):
    posizioni_per_anno = []

    # Itera su tutti gli anni unici presenti nel file 'races'
    for year in races['year'].unique():
        # Filtra le gare per l'anno corrente
        gare_anno = races[races['year'] == year]
        
        # Filtra i risultati per il pilota e per le gare di quell'anno
        risultati_anno = results[
            (results['raceId'].isin(gare_anno['raceId'])) & 
            (results['driverId'] == driver_id)
        ]
        
        # Se ci sono risultati validi, calcola la posizione media
        if not risultati_anno.empty:
            posizione_media = risultati_anno['positionOrder'].mean()
            posizioni_per_anno.append((year, posizione_media))

    # Controllo se ci sono dati da visualizzare
    if not posizioni_per_anno:
        print(f"Nessun dato trovato per il pilota {driver_id}.")
        return

    # Ordina i risultati per anno
    posizioni_per_anno.sort()
    anni, posizioni = zip(*posizioni_per_anno)

    # Creazione del grafico
    plt.figure(figsize=(10, 6))
    plt.plot(anni, posizioni, marker='o', linestyle='-', color='red')
    plt.xlabel('Anno')
    plt.ylabel('Posizione Finale Media')
    plt.title(f"Posizione finale media per il pilota {driver_id} nei diversi anni")
    plt.gca().invert_yaxis()  # Invertiamo l'asse Y perché 1° posto è migliore
    plt.grid(True)
    plt.show()

# Funzione per tracciare l'andamento della posizione finale di un pilota su un circuito specifico negli anni
def grafico_andamento_posizione_circuito(driver_id, circuit_id):
    posizioni_circuito = []

    # Filtra le gare del circuito specifico
    circuit_races = races[races['circuitId'] == circuit_id]

    for index, race in circuit_races.iterrows():
        year = race['year']
        race_id = race['raceId']
        
        # Filtra i risultati per il pilota nella gara specifica
        risultato_pilota = results[(results['raceId'] == race_id) & (results['driverId'] == driver_id)]
        
        if not risultato_pilota.empty:
            # Prende la posizione minima per evitare errori e assicura un solo valore
            posizione_finale = risultato_pilota['positionOrder']
            posizioni_circuito.append((year, posizione_finale))

    # Ordina le posizioni per anno
    posizioni_circuito.sort()

    # Verifica se ci sono dati validi
    if not posizioni_circuito:
        print("Nessun dato disponibile per il pilota e il circuito specificati.")
        return

    # Separazione degli anni e delle posizioni
    anni, posizioni = zip(*posizioni_circuito)

    # Creazione del grafico
    plt.figure(figsize=(10, 6))
    plt.plot(anni, posizioni, marker='o', linestyle='-', color='brown')
    plt.xlabel('Anno')
    plt.ylabel('Posizione Finale')
    plt.title(f"Andamento della posizione finale del pilota {driver_id} sul circuito {circuit_id}")
    plt.gca().invert_yaxis()  # Invertiamo l'asse Y perché 1° posto è migliore
    plt.grid(True)
    plt.show()

# Richiamo delle funzioni per provarle
driver_id = 844       # Sostituisci con l'ID del pilota che vuoi analizzare
constructor_id = 1   # Sostituisci con l'ID della scuderia che vuoi analizzare
circuit_id = 1      # Sostituisci con l'ID del circuito che vuoi analizzare

# Prova della funzione per la durata delle gare
#grafico_durata_gara(driver_id, circuit_id)

# Prova della funzione per i punti della scuderia su un circuito
#grafico_punti_scuderia(constructor_id, circuit_id)

# Prova della funzione per i punti totali della scuderia
#grafico_punti_totali_scuderia(constructor_id)

# Prova della funzione per la media dei pit stop
#grafico_media_pit_stop(driver_id)

# Prova della funzione per la posizione finale media del pilota
#grafico_posizione_media(driver_id)

#prova della funzione per l'andamento della posizione finale di un piloto su un circuito
#grafico_andamento_posizione_circuito(driver_id, circuit_id)