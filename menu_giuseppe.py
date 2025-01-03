from progetto import*
from funzioni import*

def menu_piloti():
    while True:
        print("Menu:")
        print("2. Andamento durata gara nel tempo per un pilota e un circuito specifici")
        print("3. Andamento durata pit stop nel tempo per un pilota")
        print("4. Andamento posizione finale nel tempo per un pilota su un circuito specifico")
        print("5. Andamento posizione media pilota nel tempo")
        print("6. Torna indietro")
        print("7. Esci")
        scelta = int(input("Inserisci il numero corrispondente all'operazione desiderata: "))

        if scelta == 2:
            nome_pilota = input("Inserisci il nome del pilota: ").strip()
            cognome_pilota = input("Inserisci il cognome del pilota: ").strip()
            nome_pista = input("Inserisci il nome del circuito: ").strip()
            driver_id = Cerca_ID_circuito(nome_pista)
            circuit_id = Cerca_ID_pilota(nome_pilota,cognome_pilota)
            if driver_id is not None and circuit_id is not None:
                grafico_durata_gara(driver_id, circuit_id)
            else:
                print("Pilota o circuito non trovato.")
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
            driver_id = Cerca_ID_pilota(nome_pilota,cognome_pilota)
            circuit_id = Cerca_ID_circuito(nome_pista)
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
            pass
        elif scelta == 7:
            break
        else:
            print("Scelta non valida. Riprova.")

def menu_scuderia():
    while True:
        print("Menu:")
        print("2. Andamento punti scuderia su un circuito specifico")
        print("3. Andamento punti scuderia nelle stagioni")
        print("4. Torna indietro")
        print("5. Esci")
        scelta = int(input("Inserisci il numero corrispondente all'operazione desiderata: "))
        if scelta == 2:
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
            pass
        elif scelta == 5:
            break
        