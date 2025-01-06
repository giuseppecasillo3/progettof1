from funzioni import *
from progetto import*
from cerca import *
from pole_winner import *
from posizioni_guadagnate import *


def menu_scuderia():
    while True:
        print("\nMenu:")
        print("1. Piloti che hanno corso nella scuderia")
        print("2. Andamento punti scuderia su un circuito specifico")
        print("3. Andamento punti scuderia nelle stagioni")
        print("4. Torna indietro")
        print("5. Esci")
        scelta = int(input("\nInserisci il numero corrispondente all'operazione desiderata: "))
        if scelta == 1:
                nome_scuderia = input("inserisci il nome della scuderia: ").strip()
                Piloti_per_scuderia(nome_scuderia)
        elif scelta == 2:
            nome_scuderia = input("Inserisci il nome della scuderia: ").strip()
            nome_pista = input("Inserisci il nome del circuito: ").strip()
            circuit_id = Cerca_ID_circuito(nome_pista)
            constructor_id = Cerca_ID_scuderia(nome_scuderia)
            if constructor_id is not None and circuit_id is not None:
                grafico_punti_scuderia(constructor_id, circuit_id)
            else:
                print("Scuderia o circuito non trovato.")
        elif scelta == 3:
            nome_scuderia = input("Inserisci il nome della scuderia: ").strip()
            constructor_id = Cerca_ID_scuderia(nome_scuderia)
            if constructor_id is not None:
                grafico_punti_totali_scuderia(constructor_id)
            else:
                print("Scuderia non trovata.")
        elif scelta == 4:
            menu()
        elif scelta == 5:
            exit()

def menu_piloti():
    while True:
        print("\nMenu:")
        print("1. Percentuale vittorie e podi del pilota")
        print("2. Andamento durata gara nel tempo per un pilota e un circuito specifici")
        print("3. Andamento durata pit stop nel tempo per un pilota")
        print("4. Andamento posizione finale nel tempo per un pilota su un circuito specifico")
        print("5. Andamento posizione media pilota nel tempo")
        print("6. Torna indietro")
        print("7. Esci")
        scelta = int(input("Inserisci il numero corrispondente all'operazione desiderata: "))
        if scelta == 1:
                nome_pilota = input("inserisci il nome del pilota: ").strip()
                cognome_pilota = input("inserisci il cognome del pilota: ").strip()
                Percentuale_vittorie_pilota(nome_pilota,cognome_pilota)
        elif scelta == 2:
            nome_pilota = input("Inserisci il nome del pilota: ").strip()
            cognome_pilota = input("Inserisci il cognome del pilota: ").strip()
            nome_pista = input("Inserisci il nome del circuito: ").strip()
            driver_id = cerca_id_pilota(nome_pilota, cognome_pilota)
            circuit_id = cerca_id_circuito(nome_pista)

            if driver_id is not None and circuit_id is not None:
                grafico_durata_gara(driver_id, circuit_id)
            else:
                print("Impossibile generare il grafico. Controlla che pilota e circuito esistano nei dati.")
                  

        elif scelta == 3:
            nome_pilota = input("Inserisci il nome del pilota: ").strip()
            cognome_pilota = input("Inserisci il cognome del pilota: ").strip()
            driver_id = Cerca_ID_pilota(nome_pilota,cognome_pilota)
            if driver_id is not None:
                grafico_media_pit_stop(driver_id)
            else:
                print("Pilota non trovato.")
        elif scelta == 4:
            nome_pilota = input("Inserisci il nome del pilota: ").strip()
            cognome_pilota = input("Inserisci il cognome del pilota: ").strip()
            nome_pista = input("Inserisci il nome del circuito: ").strip()
            driver_id = cerca_id_pilota(nome_pilota, cognome_pilota)
            circuit_id = cerca_id_circuito(nome_pista)
            if driver_id is not None:
                grafico_andamento_posizione_circuito(driver_id, circuit_id)
            else:
                print("Pilota non trovato.")
        elif scelta == 5:
            nome_pilota = input("Inserisci il nome del pilota: ").strip()
            cognome_pilota = input("Inserisci il cognome del pilota: ").strip()
            driver_id = Cerca_ID_pilota(nome_pilota,cognome_pilota)
            if driver_id is not None:
                grafico_posizione_media(driver_id)
            else:
                print("Pilota non trovato.")
        elif scelta == 6:
            menu()
        elif scelta == 7:
            exit()


def menu_gare():
    while True:
        print("\nMenu:")
        print("1. Vittoria partendo dalla Pole Position")
        print("2. Delta posizioni di un pilota in una gara")
        print("3. Vincitore di una gara")
        print("4. Torna indietro")
        print("5. Esci")
        scelta = int(input("Inserisci il numero corrispondente all'operazione desiderata: "))
        if scelta == 1: 
            anno = int(input("Inserisci l'anno: \n"))
            nome_pista = input("Inserisci nome del Gran Premio: \n")
            pole_winner(anno,nome_pista)
        elif scelta == 2:
            anno = int(input("Inserisci l'anno: \n"))
            nome_pista = input("Inserisci nome del Gran Premio: \n")
            nome_pilota = input("Inserisci nome pilota: \n")
            cognome_pilota = input("Inserisci cognome pilota: \n")
            differenza_posizioni(anno,nome_pista,nome_pilota,cognome_pilota)
        elif scelta == 3:
            anno = int(input("Inserisci l'anno: \n"))
            nome_pista = input("Inserisci nome del Gran Premio: \n")
            vincitore_gara(anno,nome_pista) 
        elif scelta == 4:
            menu()
        elif scelta == 5:
            exit()

def menu_circuiti():
    while True:
        print("\nMenu:")
        print("1. Albo d'oro di un circuito")
        print("2. Torna indietro")
        print("3. Esci")
        scelta = int(input("Inserisci il numero corrispondente all'operazione desiderata: "))
        if scelta == 1:
            nome_circuito = input("Inserisci il nome del circuito: ").strip()
            Albo_oro_circuito(nome_circuito)
        elif scelta == 2:
            menu()
        elif scelta == 3:
            exit()


def menu():

    while True:
        scelta_categoria=int(input("\nChe categoria vuoi selezionare?\n1.Circuiti,\n2.Scuderie,\n3.Piloti,\n4.Gara,\n5.uscire,\n(inserire numero): "))
        if scelta_categoria==1:
            menu_circuiti()

        elif scelta_categoria==2:
            menu_scuderia()
            
        elif scelta_categoria==3:
            menu_piloti()
        
        elif scelta_categoria==4:
            menu_gare()

        elif scelta_categoria==5:
            print("uscita dal programma")
            exit()

menu()