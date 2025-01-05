# 🏎️ Analisi Dati Formula 1

## 📝 Descrizione del Progetto
Questo progetto nasce dalla fusione tra la nostra passione per la Formula 1 e gli obiettivi formativi del corso di Data Engineering. La scelta di lavorare con i dati della Formula 1 non è stata casuale: questo sport rappresenta un perfetto caso di studio dove enormi quantità di dati vengono generate, elaborate e analizzate in tempo reale per prendere decisioni strategiche.

## 🎯 Obiettivi
Il progetto si propone di:
- Analizzare dataset storici della Formula 1
- Implementare funzionalità di ricerca e analisi avanzate
- Presentare i dati in modo intuitivo 
- Applicare i principi di Data Engineering in un contesto reale e appassionante

## 🛠️ Struttura del Progetto
Il progetto è organizzato in diversi moduli Python, ognuno con una specifica funzionalità:
- `menu.py`: Gestione del menu e delle opzioni utente
- `cerca.py`: Implementazione delle funzionalità di ricerca
- `check_file.py`: Controllo dei file dati
- Altri moduli specifici per analisi dettagliate (vittorie, pole position,durata gare etc.)

## 📊 Dataset
Il progetto utilizza dataset completi della Formula 1, includendo:
- Informazioni su piloti e costruttori
- Risultati delle gare e qualifiche
- Dati sui pit stop e tempi sul giro
- Statistiche storiche e record

## 📐 Note sui Diagrammi UML
Per quanto riguarda i diagrammi UML richiesti dal corso:

### Diagramma delle Classi
Data la natura del progetto, fortemente orientata all'elaborazione dati e alle funzioni di analisi, la rappresentazione attraverso un diagramma delle classi tradizionale risulterebbe forzata. Tuttavia, abbiamo mantenuto una struttura modulare del codice che riflette i principi della programmazione orientata agli oggetti.

### Diagramma dei Casi d'Uso
Nel diagramma dei casi d'uso abbiamo rappresentato tutte le funzionalità disponibili all'utente nel sistema. Nonostante ci siano solamente quattro possibili input (Pilota, Scuderia, Gara e Circuito), abbiamo scelto di ripetere più volte le relazioni <<include>> per ogni funzionalità. Questa decisione di design, sebbene possa sembrare ridondante, è stata presa per garantire una maggiore chiarezza e leggibilità del diagramma. In questo modo, ogni caso d'uso principale è direttamente collegato al suo caso d'uso incluso, rendendo immediatamente comprensibile il flusso di ogni funzionalità senza dover seguire relazioni multiple o intrecciate.

### Diagramma degli Stati
Sebbene il progetto non si presti naturalmente a una rappresentazione tramite diagramma degli stati classico, abbiamo cercato di modellare il flusso delle operazioni e le transizioni tra le diverse funzionalità del programma in modo da rispettare i principi fondamentali della progettazione state-based.

## 🔧 Requisiti e Installazione
I requisiti sono elencati nel file `requirements.txt`. Per installare le dipendenze necessarie:

pip install -r requirements.txt

## 🚀 Come Avviare il Programma
Per avviare il programma, eseguire il seguente comando nel terminale:

python menu.py

## 📚 Conclusioni
Questo progetto dimostra come la passione per uno sport tecnologicamente avanzato come la Formula 1 possa integrarsi perfettamente con gli obiettivi didattici di un corso di Data Engineering. La gestione e l'analisi di grandi quantità di dati, la necessità di elaborare informazioni in modo efficiente e la presentazione dei risultati in forma comprensibile sono tutti aspetti che accomunano questi due mondi.
