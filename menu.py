import funzioni

def menu():

    while True:
        scelta_categoria=int(input("\nChe categoria vuoi selezionare?\n1.Circuiti,\n2.Scuderie,\n3.Piloti,\n4.Gara,\n5.uscire,\n(inserire numero): "))
        if scelta_categoria==1:
            nome_circuito = input("inserisci il nome del circuito: ")
            funzioni.Albo_oro_circuito(nome_circuito)

        elif scelta_categoria==2:
            scelta=int(input("quale statistica vuoi vedere?:\n1.Piloti per scuderia,\n(inserire numero): "))
            if scelta == 1:
                nome_scuderia = input("inserisci il nome della scuderia: ")
                funzioni.Piloti_per_scuderia(nome_scuderia)

        elif scelta_categoria==3:
            scelta=int(input("quale statistica vuoi vedere?:\n1.Percentuale vittorie e podi del pilota,\n(inserire numero): "))
            if scelta == 1:
                nome_pilota = input("inserisci il nome del pilota: ")
                cognome_pilota = input("inserisci il cognome del pilota: ")
                funzioni.Percentuale_vittorie_pilota(nome_pilota,cognome_pilota)

        elif scelta_categoria==5:
            print("uscita dal programma")
            break

menu()