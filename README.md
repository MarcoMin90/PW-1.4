#  Cosa fa questo script

Questo script è una piccola applicazione web costruita con Flask, un framework Python leggero per la creazione di API RESTful. L'applicazione permette agli utenti di prenotare stanze in un hotel e di cancellare le prenotazioni esistenti. Utilizza un database MySQL per memorizzare i dati delle prenotazioni e gestisce le richieste HTTP tramite Web API Endpoints definite nel codice.

Funzionalità Chiave
 1)  Prenotazione di una Stanza :
       Gli utenti possono prenotare una stanza fornendo i dettagli necessari.
       Viene verificata la disponibilità della stanza prima di confermare la prenotazione.
       Cancellazione di una Prenotazione :
Gli utenti possono cancellare una prenotazione esistente utilizzando l'email associata.

   2) Gestione del Database :
       Tutti i dati delle prenotazioni vengono memorizzati in un database MySQL.
      
   3) API RESTful :
        L'app espone due endpoint principali (/prenota e /cancella) per interagire con il sistema.
