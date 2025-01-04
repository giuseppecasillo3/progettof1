import pandas as pd
import numpy as np

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

# Funzione per calcolare le posizioni guadagnate o perse per un pilota e una gara specifica



  
            
    
# def pole_winner():
   
#     race_id = int(input("che gara vuoi cercare?"))
   
#     risultati_filtrati = results[results['raceId'] == race_id]

    
#     posizione1 = risultati_filtrati[risultati_filtrati['grid'] == 1]

#     for index, race in posizione1.iterrows():
#         grid = race['grid']
#         position = race['positionOrder']
#         driverId = race['driverId']
        

        
#         if grid == position:
#             print(f"{driverId} ha vinto partendo da primo in corsa {race_id}")
#         else:
#             print (f"{driverId} non ha vinto la gara partendo da primo")

# pole_winner()



def trova_race_id():
        

        
        anno = int(input("Scegli l'anno:\n"))
        
        
        nome = input("Scegli il nome del circuito: \n")

        
        
      
        risultati_filtrati = races[races['year'] == anno]  
        risultati_filtrati = risultati_filtrati[risultati_filtrati['name'].str.contains(nome, case=False, na=False)]
        race_Id = risultati_filtrati['raceId']
        

    
        if risultati_filtrati.empty:
            print("Nessuna gara trovata per l'anno e il nome del circuito specificati.")
        else:
            print(race_Id)

        return risultati_filtrati

# trova_race_id()
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

def pole_winner(anno, nome_pista):

    id_circuito = cerca_id_circuito(nome_pista)
    
    if not id_circuito:
        print("Circuito non trovato.")
        return
    
    gara_id = trova_race_id_2(anno, id_circuito)
    
    if not gara_id:
        print("Gara non trovata.")
        return
    
    risultati_filtrati = results[results['raceId'] == gara_id]
    posizione1 = risultati_filtrati[risultati_filtrati['grid'] == 1]
    
    for index, race in posizione1.iterrows():
        grid = race['grid']
        position = race['positionOrder']
        driverId = race['driverId']
        
        # Trova il nome del pilota (assicurati di avere un dataframe drivers con la colonna driverId)
        driver_name = drivers[drivers['driverId'] == driverId]['forename'].values[0]+ ' ' + drivers[drivers['driverId'] == driverId]['surname'].values[0]
        
        if grid == position:
            print(f"{driver_name} ha vinto partendo da primo in griglia")
        else:
            print(f"{driver_name} non ha vinto la gara partendo da primo")

# Chiamata alla funzione



