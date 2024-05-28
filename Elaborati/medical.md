**Progetto: Sistema di Accesso a file privati “medicali” gestito su blockchain**

**Obiettivo del Progetto**

Lo scopo del progetto è quello di sviluppare un sistema di accesso a file con autenticazione e controllo dei permessi e dei dati ricevuti tramite blockchain. Il sistema deve prevedere la presenza di tre attori: pazienti, medici e struttura ospedaliera. Gli studenti saranno responsabili della progettazione dell'architettura del sistema, del protocollo di comunicazione tra i nodi dell'infrastruttura e del modello di interfacciamento dei client.

**Specifiche del Progetto**

**Architettura del Sistema**: 

L'architettura del sistema dovrebbe essere gerarchica, devono essere istanziati tre contratti di tokenizzazione ERC721, uno per i gestori della struttura ospedaliera, uno per i medici ed uno per i pazienti. I gestori della struttura sanitaria sono incaricati di creare gli NFT per i medici iscritti alla loro struttura e di attribuirli agli account dei medici, i medici a loro volta devono compiere lo stesso processo con i loro pazienti. Il tutto deve essere integrato in un sistema di visualizzazione dei dati al quale possono accedere tutti gli attori: i pazienti potranno vedere solo i record inerenti al loro percorso ospedaliero, i medici potranno vedere solo i record inerenti ai pazienti in cura da loro, infine la struttura ospedaliere deve avere accesso a tutti i dati ai quali hanno accesso i medici iscritti nella loro struttura. Il controllo delle attribuzioni e degli accessi deve essere gestito con logiche di hash check attraverso l’utilizzo dei token.

**Protocollo di Comunicazione**: 

Gli studenti devono progettare un protocollo di comunicazione per lo scambio di informazioni e file tra i nodi. Questo protocollo dovrebbe supportare almeno le seguenti operazioni:

* **Registrazione**: Solo il medico deve poter iscrivere in una lista di account accreditati al suo account personale i pazienti in cura da lui, la lista deve essere associata a dei token ERC721.
* **Caricamento dei file**: Solo il medico deve poter caricare i file sul server e salvarne l’hash come uri di un NFT in modo che sia unicamente attribuibile al paziente e al medico.
* **Accesso ai file**: Ogni paziente deve poter far richiesta di accesso solo ai suoi file personali direttamente al medico, ogni medico deve poter far richiesta di accesso solo per i file inerenti i pazienti in cura da lui e dunque iscritti da lui stesso al sistema.
* **Disconnessione**: In caso di disconnessione del nodo del medico la richiesta del paziente deve essere reindirizzata al server della struttura ospedaliera.

**Modello di Interfacciamento dei Client**: 

Gli studenti devono progettare un'interfaccia utente o un'interfaccia a riga di comando unica per pazienti e medici. Questa interfaccia dovrebbe permettere agli utenti di caricare file, accedere ai file e di compiere solo le operazioni per le quali hanno il permesso, ogni operazione di verifica deve essere eseguita con interazioni con smart contract per garantire l’auditability del sistema.

**Sicurezza e Privacy**: 

Il sistema dovrebbe implementare misure di sicurezza di base, come la criptazione dei file e l'autenticazione degli utenti.

**Implementazione**: 

L'implementazione del progetto deve essere realizzata in Python e in Solidity per gli smart contract, si può simulare il tutto su rete locale Ethereum con Ganache. 

**Test**: 

Gli studenti devono fornire test appropriati per verificare la corretta funzionalità del sistema. Questi test dovrebbero coprire tutte le funzionalità chiave del sistema e dovrebbero essere automatizzati per quanto possibile.

**Consegna del Progetto**:

Gli studenti dovranno fornire il codice sorgente del progetto, la documentazione del progetto (che include la descrizione dell'architettura del sistema, del protocollo di comunicazione e del modello di interfacciamento dei client), e i test. Il tutto deve essere presentato in un formato facilmente accessibile e leggibile.
