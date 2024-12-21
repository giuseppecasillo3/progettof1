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

def differenza_posizioni(race_id, driver_id):
    change_positions= results[(results['raceId']== race_id) & (results['driverId']== driver_id)]
    
    if change_positions.empty:
        return None
    
    for index, result in change_positions.iterrows():
        grid = result['grid']
        positionOrder = result['positionOrder']

        difference_positions = positionOrder - grid


    print (difference_positions)    
    return difference_positions


differenza_posizioni(1, 20)

# def pole_winner (race_id):
#     risultato = results[results['raceId'] == race_id]
   
#     for index, race in risultato.iterrows():
    
#         grid = race['grid']
#         position = race['positionOrder']
#         driverId = race['driverId']
        

#         if race['grid'] == race['positionOrder']:
#                 print(race['driverId'], "ha vinto partendo da primo")
       
# pole_winner(20)       
            
    
def pole_winner(race_id):
   
    risultati_filtrati = results[results['raceId'] == race_id]

    
    posizione1 = risultati_filtrati[risultati_filtrati['grid'] == 1]

    for index, race in posizione1.iterrows():
        grid = race['grid']
        position = race['positionOrder']
        driverId = race['driverId']

        
        if grid == position:
            print(f"{driverId} ha vinto partendo da primo in corsa {race_id}")
        else:
            print (f"{driverId} non ha vinto la gara partendo da primo")


pole_winner(50)


  