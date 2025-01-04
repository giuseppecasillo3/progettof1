def trova_race_id_2(anno, nome_pista):
    # Cerca l'ID del circuito
    id_circuito = cerca_id_circuito(nome_pista)
    for row in races.itertuples():
        if row.year == anno and row.circuitId == id_circuito:
            print(row.raceId)
            return row.raceId

anno = int(input("Inserisci l'anno della gara: ").strip())
nome_pista = input("Inserisci il nome del circuito: ").strip()

race_id = trova_race_id_2(anno, nome_pista)