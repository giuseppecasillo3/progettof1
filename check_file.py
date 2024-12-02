import pandas as pd


def check_qualifyng():
    # Carica il file CSV
    df = pd.read_csv('qualifying.csv')

    # Trova il range completo di raceId
    fullrange = set(range(1, 1145))

    # Trova i raceId presenti nel DataFrame
    present_race_ids = set(df['raceId'])

    # Trova i raceId mancanti
    missing_race_ids = fullrange - present_race_ids

    # Stampa i raceId mancanti
    print("Race IDs mancanti::", sorted(missing_race_ids))

def check_constructor_results():
    df = pd.read_csv('constructor_results.csv')
    fullrange = set(range(1, 1145))
    present_race_ids = set(df['raceId'])
    missing_race_ids = fullrange - present_race_ids
    print("Race IDs mancanti::", sorted(missing_race_ids))


def check_constructor_standings():
    df = pd.read_csv('constructor_standings.csv')
    fullrange = set(range(1, 1145))
    present_race_ids = set(df['raceId'])
    missing_race_ids = fullrange - present_race_ids
    print("Race IDs mancanti::", sorted(missing_race_ids))

def check_driver_standings():
    df = pd.read_csv('driver_standings.csv')
    fullrange = set(range(1, 1145))
    present_race_ids = set(df['raceId'])
    missing_race_ids = fullrange - present_race_ids
    print("Race IDs mancanti::", sorted(missing_race_ids))

def check_lap_rimes():
    df = pd.read_csv('lap_times.csv')
    fullrange = set(range(1, 1145))
    present_race_ids = set(df['raceId'])
    missing_race_ids = fullrange - present_race_ids
    print("Race IDs mancanti::", sorted(missing_race_ids))


def check_pit_stops():
    df = pd.read_csv('pit_stops.csv')
    fullrange = set(range(1, 1145))
    present_race_ids = set(df['raceId'])
    missing_race_ids = fullrange - present_race_ids
    print("Race IDs mancanti::", sorted(missing_race_ids))

def check_results():
    df = pd.read_csv('results.csv')
    fullrange = set(range(1, 1145))
    present_race_ids = set(df['raceId'])
    missing_race_ids = fullrange - present_race_ids
    print("Race IDs mancanti::", sorted(missing_race_ids))

def check_sprint_results():
    df = pd.read_csv('sprint_results.csv')
    fullrange = set(range(1, 1145))
    present_race_ids = set(df['raceId'])
    missing_race_ids = fullrange - present_race_ids
    print("Race IDs mancanti::", sorted(missing_race_ids))

def menu():
    while True:
        print("\nMenu:")
        print("1. Controlla 'qualifying.csv'")
        print("2. Controlla 'constructor_results.csv'")
        print("3. Controlla 'constructor_standings.csv'")
        print("4. Controlla 'driver_standings.csv'")
        print("5. Controlla 'lap_times.csv'")
        print("6. Controlla 'pit_stops.csv'")
        print("7. Controlla 'results.csv'")
        print("8. Controlla 'sprint_results.csv'")
        print("9. Esci")
        choice = input("Scegli un'opzione (1-9): ")

        if choice == '1':
            check_qualifyng()
        elif choice == '2':
            check_constructor_results()
        elif choice == '3':
            check_constructor_standings()
        elif choice == '4':
            check_driver_standings()
        elif choice == '5':
            check_lap_rimes()
        elif choice == '6':
            check_pit_stops()
        elif choice == '7':
            check_results()
        elif choice == '8':
            check_sprint_results()
        elif choice == '9':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")



menu()