**Progetto: Simple marketplace creazione di marketplace in Web3 per gestione token**

**Obiettivo del Progetto**

Lo scopo del progetto è quello di sviluppare un marketplace per la visualizzazione vendita e iscrizione di token, ERC20 e ERC721. Il client del sistema può sia iscrivere token nel marketplace che visualizzare le “collezioni” che possiede. Gli studenti saranno responsabili della progettazione dell'architettura del sistema, della scrittura dei contratti e della scrittura delle interazioni con Web3.

**Specifiche del Progetto**

**Architettura del Sistema**: 

L'architettura del sistema deve permettere a chiunque di iscrivere nel marketplace i propri token, di acquistare token fungibili o non dal marketplace stesso, e di visualizzare la propria collezione personale. Le transazioni di acquisto devono essere effettuate in Ether e solo all’avvenuta cristallizzazione della transazione nel blocco deve seguire il trasferimento dei token acquistati.

**Interazioni **: 

Gli studenti devono progettare un protocollo di comunicazione per lo scambio di informazioni e file tra i nodi. Questo protocollo dovrebbe supportare almeno le seguenti operazioni:

* **Registrazione**: Chiunque deve poter chiamare questa funzione andando ad iscrivere nel marketplace solo i token contracts di cui è owner, inoltre deve poter decidere la quantità o quali dei token da lui creati possano essere venduti nel marketplace.
* **Visualizzazione del marketplace**: Chiunque deve poter interrogare il marketplace per la visualizzazione dei prodotti in vendita con il relativo costo, deve essere previsto un metodo di visualizzazione condizionata (e.g. il client deve poter richiedere la visualizzazione dei soli ERC721 o anche dei singoli token appartenenti ad un contratto).
* **Visualizzazione della collezione personale**: Chiunque deve poter interrogare il marketplace per ricevere la lista dei token in suo possesso.
* **Acquisto**: Chiunque deve poter comprare i prodotti in vendita e la transazione in ether deve avvenire a favore del proprietario della collezione stessa.
* **Eliminazione**: In caso di richiesta da parte del proprietario del contratto iscritto al marketplace il contratto in questione e quindi tutti i prodotti in vendita nel marketplace associato ad esso vanno eliminati.

**Modello di Interfacciamento dei Client**: 

Gli studenti devono progettare un'interfaccia utente o un'interfaccia a riga di comando unica. Questa interfaccia deve permettere di svolgere le interazioni sopra elencate andando a triggerare le corrette funzioni dei contratti standardizzati ERC20 e ERC721.

**Sicurezza e Privacy**: 

Il sistema dovrebbe implementare tutta la logica di backhand su blockchain e usare il frontend solo per visualizzare i dati richiesti dall’utente.

**Implementazione**: 

L'implementazione del progetto deve essere realizzata in Python e in Solidity per gli smart contract, si può simulare il tutto su rete locale Ethereum con Ganache. 

**Test**: 

Gli studenti devono fornire test appropriati per verificare la corretta funzionalità del sistema. Questi test dovrebbero coprire tutte le funzionalità chiave del sistema e dovrebbero essere automatizzati per quanto possibile.

**Consegna del Progetto**:

Gli studenti dovranno fornire il codice sorgente del progetto, la documentazione del progetto (che include la descrizione dell'architettura del sistema, del protocollo di comunicazione e del modello di interfacciamento dei client), e i test. Il tutto deve essere presentato in un formato facilmente accessibile e leggibile.
