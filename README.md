# PW-1.4


<!DOCTYPE html>
<html lang="it">
<head>
    <!-- Impostazioni di base del documento -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Minichino - Prenotazione Online</title>

    <!-- Bootstrap per la gestione del layout e degli stili -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- jQuery per la gestione degli eventi e delle richieste asincrone -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <!-- Stili personalizzati per migliorare il layout -->
    <style>
        body {
            background-color: #f0f4f8; /* Colore di sfondo chiaro */
            color: #333; /* Colore del testo scuro */
        }

        /* Stile per le card (contenitori) delle informazioni di prenotazione */
        .card {
            border-radius: 10px;
            margin-bottom: 20px;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            background-color: #ffffff; /* Colore di sfondo delle card */
        }

        .card-header {
            font-size: 1.25rem;
            padding: 15px;
            background-color: #007bff; /* Colore di sfondo della header */
            color: white; /* Colore del testo della header */
        }

        .card-body {
            padding: 20px;
        }

        /* Aggiungi un margine superiore alla container principale */
        .container {
            margin-top: 50px;
        }

        /* Stile per i pulsanti */
        .btn {
            padding: 12px;
            font-size: 1.1rem;
        }

        /* Centra i form all'interno delle card */
        form {
            margin-top: 15px;
        }

        /* Stile per gli alert */
        .alert {
            margin-top: 20px;
        }

        /* Adatta il layout per schermi piccoli */
        @media (max-width: 768px) {
            .card {
                max-width: 100%;
                margin-bottom: 10px;
            }
        }

        /* Stile per l'intestazione dell'hotel */
        .hotel-header {
            text-align: center;
            margin-bottom: 30px;
        }

        .hotel-header img {
            max-width: 150px;
            border-radius: 50%;
            margin-bottom: 20px;
        }

        .hotel-header h1 {
            font-size: 2.5rem;
            color: #333;
        }

        .hotel-header p {
            font-size: 1.1rem;
            color: #555; /* Colore del testo più chiaro */
        }

        /* Stile per la sezione di contatto */
        .contact-section {
            background-color: #f0f4f8; /* Colore di sfondo chiaro */
            padding: 30px;
            text-align: center;
            margin-top: 50px;
            border-top: 1px solid #ddd;
        }

        .contact-section p {
            font-size: 1.1rem;
            color: #333;
        }

        .contact-section .email {
            font-size: 1.2rem;
            font-weight: bold;
            color: #007bff;
        }

        .contact-section .city {
            font-size: 1.1rem;
            color: #555;
        }

        /* Stile per la sezione privacy */
        .privacy-section {
            background-color: #f0f4f8; /* Colore di sfondo chiaro */
            padding: 20px;
            text-align: center;
            margin-top: 30px;
            border-top: 1px solid #ddd;
        }

        .privacy-section h5 {
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <!-- Intestazione con Logo e Nome dell'Hotel -->
        <header class="hotel-header">
            <h1>Hotel Minichino</h1>
            <p>Un rifugio di comfort e lusso nel cuore della città. Prenota la tua stanza per un'esperienza indimenticabile!</p>
        </header>

        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10 col-sm-12">
                <!-- Sezione Prenotazione Stanza -->
                <div class="card shadow">
                    <div class="card-header text-center">
                        <h4>Prenota una Stanza</h4>
                    </div>
                    <div class="card-body">
                        <form id="prenotazioneForm">
                            <!-- Campo per il nome e cognome del cliente -->
                            <div class="mb-3">
                                <label for="nome_cliente" class="form-label">Nome e Cognome</label>
                                <input
                                    type="text"
                                    class="form-control"
                                    id="nome_cliente"
                                    placeholder="Inserisci il tuo nome e cognome"
                                    required>
                            </div>

                            <!-- Campo per l'email del cliente -->
                            <div class="mb-3">
                                <label for="email_cliente" class="form-label">Email</label>
                                <input
                                    type="email"
                                    class="form-control"
                                    id="email_cliente"
                                    placeholder="Inserisci la tua email"
                                    required>
                            </div>

                            <!-- Selezione del tipo di stanza -->
                            <div class="mb-3">
                                <label for="stanza_id" class="form-label">Tipo di Stanza</label>
                                <select
                                    class="form-select"
                                    id="stanza_id"
                                    required>
                                    <option value="">Seleziona il tipo di stanza</option>
                                    <option value="0">Singola</option>
                                    <option value="1">Doppia</option>
                                    <option value="2">Tripla</option>
                                    <option value="3">Quadrupla</option>
                                    <option value="4">Suite</option>
                                </select>
                            </div>

                            <!-- Selezione della data di check-in -->
                            <div class="mb-3">
                                <label for="data_checkin" class="form-label">Data Check-in</label>
                                <input
                                    type="date"
                                    class="form-control"
                                    id="data_checkin"
                                    required>
                            </div>

                            <!-- Selezione della data di check-out -->
                            <div class="mb-3">
                                <label for="data_checkout" class="form-label">Data Check-out</label>
                                <input
                                    type="date"
                                    class="form-control"
                                    id="data_checkout"
                                    required>
                            </div>

                            <!-- Sezione Metodo di Pagamento -->
                            <div class="mb-3">
                                    <option value="in-sede">Pagament in Sede</option> <!-- Nuova opzione aggiunta -->
                                </select>
                            </div>

                            <!-- Checkbox per il consenso al trattamento dei dati personali -->
                            <div class="mb-3 form-check">
                                <input type="checkbox" class="form-check-input" id="consenso" required>
                                <label class="form-check-label" for="consenso">
                                    Accetto il trattamento dei dati personali e la <a href="privacy_policy.html" target="_blank">privacy policy</a>.
                                </label>
                            </div>

                            <!-- Bottone per inviare il modulo -->
                            <div class="text-center">
                                <button type="submit" class="btn btn-primary w-100">Prenota</button>
                            </div>
                        </form>

                        <!-- Area per gli alert di errore o successo -->
                        <div id="alert-container"></div>
                    </div>
                </div>

                <!-- Sezione per la cancellazione della prenotazione -->
                <div class="card shadow">
                    <div class="card-header text-center bg-danger text-white">
                        <h4>Cancella Prenotazione</h4>
                    </div>
                    <div class="card-body">
                        <form id="cancellazioneForm">
                            <!-- Campo per l'email del cliente da cancellare -->
                            <div class="mb-3">
                                <label for="email_cancellazione" class="form-label">Email</label>
                                <input
                                    type="email"
                                    class="form-control"
                                    id="email_cancellazione"
                                    placeholder="Inserisci la tua email"
                                    required>
                            </div>

                            <!-- Bottone per inviare il modulo di cancellazione -->
                            <div class="text-center">
                                <button type="submit" class="btn btn-danger btn-sm">Cancella</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Sezione Contatti -->
    <div class="contact-section">
        <p>Per qualsiasi informazione, non esitare a contattarci:</p>
        <p class="email">info@hotelminichino.it</p>
        <p class="city">Vicoletto Napoli 1, 80143 Napoli (NA)</p>
    </div>

    <!-- Sezione Privacy -->
    <div class="privacy-section">
        <h5>Trattamento dei Dati Personali e Privacy</h5>
        <p>Informiamo i nostri clienti che i dati personali forniti durante la prenotazione saranno trattati nel rispetto della normativa vigente sulla privacy.</p>
        <p>Per maggiori informazioni, consultare la nostra <a href="privacy_policy.html">Informativa sulla Privacy</a>.</p>
    </div>

    <!-- Script per Bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- Gestione della logica di invio del modulo di prenotazione -->
    <script>
        $("#prenotazioneForm").on("submit", function(e) {
            e.preventDefault();

            // Recupero dei dati dal modulo di prenotazione
            const metodoPagamento = $("#metodo_pagamento").val();
            const consenso = $("#consenso").is(":checked");

            if (!metodoPagamento) {
                mostraAlert("danger", "Devi selezionare un metodo di pagamento per procedere.");
                return;
            }

            if (!consenso) {
                mostraAlert("danger", "Devi accettare il trattamento dei dati personali per procedere.");
                return;
            }

            const prenotazione = {
                nome_cliente: $("#nome_cliente").val(),
                email_cliente: $("#email_cliente").val(),
                stanza_id: parseInt($("#stanza_id").val()),  // Converto la stanza in numero
                data_checkin: $("#data_checkin").val(),
                data_checkout: $("#data_checkout").val(),
                metodo_pagamento: metodoPagamento  // Aggiunto il metodo di pagamento
            };

            // Verifica se è stato selezionato un tipo di stanza valido
            if (isNaN(prenotazione.stanza_id)) {
                mostraAlert("danger", "Seleziona un tipo di stanza valido.");
                return;
            }

            // Chiamata AJAX per inviare i dati al server
            $.ajax({
                url: "http://127.0.0.1:5000/prenota",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify(prenotazione),
                success: function(response) {
                    mostraAlert("success", response.message);
                    $("#prenotazioneForm")[0].reset();  // Reset del modulo
                },
                error: function(xhr) {
                    mostraAlert("danger", xhr.responseJSON.message || "Errore durante la prenotazione.");
                }
            });
        });

        // Gestione della cancellazione della prenotazione
        $("#cancellazioneForm").on("submit", function(e) {
            e.preventDefault();

            const email = $("#email_cancellazione").val();

            $.ajax({
                url: "http://127.0.0.1:5000/cancella",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify({ email }),
                success: function(response) {
                    mostraAlert("success", response.message);
                    $("#cancellazioneForm")[0].reset();
                },
                error: function(xhr) {
                    mostraAlert("danger", xhr.responseJSON.message || "Errore durante la cancellazione.");
                }
            });
        });

        // Funzione per mostrare un alert con messaggio

        function mostraAlert(tipo, messaggio) {
            const alertHTML = `
                <div class="alert alert-${tipo} alert-dismissible fade show" role="alert">
                    ${messaggio}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            `;
            
            // Aggiungi l'alert al contenitore
            $("#alert-container").append(alertHTML);
            
            // Rimuovi l'alert dopo 4 secondi
            setTimeout(function() {
                $(".alert").last().alert('close');
            }, 4000);
        }
    </script>
</body>
</html>

---------------------Pagina per la protezione dei dati e la privacy-------------------
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informativa sulla Privacy - Hotel Minichino</title>
    <!-- Collega il foglio di stile di Bootstrap per un design responsivo -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* Stili personalizzati per migliorare l'aspetto della pagina */
        body {
            background-color: #f8f9fa; /* Colore di sfondo chiaro */
            color: #333; /* Colore del testo principale */
        }
        .container {
            margin-top: 50px; /* Spazio sopra il contenuto */
            margin-bottom: 50px; /* Spazio sotto il contenuto */
        }
        h1, h2, h3 {
            color: #0056b3; /* Colore blu per i titoli */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Informativa sulla Privacy</h1>
        <p>Questa informativa spiega come raccogliamo, utilizziamo e proteggiamo i dati personali degli utenti che visitano il nostro sito web.</p>

        <h2>1. Chi è il Titolare del Trattamento</h2>
        <p>Il titolare del trattamento dei dati è l'Hotel Minichino, situato in Vicoletto Napoli 1, 80143 Napoli (NA). Questo significa che siamo responsabili della gestione dei tuoi dati.</p>

        <h2>2. Quali Dati Raccogliamo</h2>
        <p>Possiamo raccogliere i seguenti tipi di dati personali:</p>
        <ul>
            <li><strong>Nome e cognome:</strong> per identificarti.</li>
            <li><strong>Indirizzo email:</strong> per comunicazioni importanti.</li>
            <li><strong>Numero di telefono:</strong> se lo fornisci, per contattarti.</li>
            <li><strong>Dettagli relativi alla prenotazione:</strong> per gestire il tuo soggiorno.</li>
        </ul>

        <h2>3. Perché Raccogliamo i Dati</h2>
        <p>Raccogliamo i tuoi dati per vari motivi, tra cui:</p>
        <ul>
            <li>Gestire le tue prenotazioni.</li>
            <li>Fornire informazioni sui servizi richiesti.</li>
            <li>Inviare offerte promozionali (solo se hai dato il consenso).</li>
            <li>Rispondere agli obblighi di legge.</li>
        </ul>

        <h2>4. Come Trattiamo i Dati e Sicurezza</h2>
        <p>Trattiamo i dati sia in forma cartacea che digitale, adottando misure di sicurezza per proteggerli da accessi non autorizzati. Ci teniamo alla tua privacy!</p>

        <h2>5. Periodo di Conservazione dei Dati</h2>
        <p>I tuoi dati saranno conservati solo per il tempo necessario a raggiungere gli scopi per cui sono stati raccolti, e comunque non oltre 10 anni.</p>

        <h2>6. Diritti degli Utenti</h2>
        <p>Hai dei diritti riguardo ai tuoi dati, tra cui:</p>
        <ul>
            <li>Accedere ai tuoi dati personali.</li>
            <li>Richiedere la correzione o la cancellazione dei tuoi dati.</li>
            <li>Limitare il trattamento dei tuoi dati.</li>
            <li>Opporsi al trattamento dei tuoi dati.</li>
            <li>Richiedere la portabilità dei tuoi dati.</li>
        </ul>

        <h2>7. Come Contattarci</h2>
        <p>Per esercitare i tuoi diritti o per maggiori informazioni sul trattamento dei dati personali, puoi contattarci via email all'indirizzo: <a href="mailto:info@hotelminichino.it">info@hotelminichino.it</a>.</p>

        <h2>8. Aggiornamenti a Questa Informativa</h2>
        <p>Ci riserviamo il diritto di modificare questa informativa. Ti informeremo di eventuali cambiamenti attraverso comunicazioni sul nostro sito.</p>

        <p>Ultimo aggiornamento: Gennaio 2025</p>
    </div>

    <!-- Script di Bootstrap per funzionalità interattive -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>


                 -----------------------------Python------------------------------
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Abilita CORS per tutte le rotte

# Configurazione del database MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/hotel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modello per la tabella Prenotazioni
class Prenotazione(db.Model):
    __tablename__ = 'prenotazioni'
    id = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(100), nullable=False)
    email_cliente = db.Column(db.String(100), nullable=False)
    stanza_id = db.Column(db.Integer, nullable=False)
    data_checkin = db.Column(db.Date, nullable=False)
    data_checkout = db.Column(db.Date, nullable=False)

# Funzione per verificare la disponibilità di una stanza
def is_room_available(stanza_id, data_checkin, data_checkout):
    prenotazioni = Prenotazione.query.filter(
        Prenotazione.stanza_id == stanza_id,
        Prenotazione.data_checkin < data_checkout,
        Prenotazione.data_checkout > data_checkin
    ).all()
    return len(prenotazioni) == 0

@app.route('/prenota', methods=['POST'])
def prenota():
    try:
        data = request.json
        nome_cliente = data['nome_cliente']
        email_cliente = data['email_cliente']
        stanza_id = data['stanza_id']
        data_checkin = datetime.strptime(data['data_checkin'], '%Y-%m-%d').date()
        data_checkout = datetime.strptime(data['data_checkout'], '%Y-%m-%d').date()

        if not is_room_available(stanza_id, data_checkin, data_checkout):
            return jsonify({'success': False, 'message': 'Stanza non disponibile'}), 409

        nuova_prenotazione = Prenotazione(
            nome_cliente=nome_cliente,
            email_cliente=email_cliente,
            stanza_id=stanza_id,
            data_checkin=data_checkin,
            data_checkout=data_checkout
        )
        db.session.add(nuova_prenotazione)
        db.session.commit()

        return jsonify({'success': True, 'message': 'Prenotazione confermata', 'prenotazione_id': nuova_prenotazione.id})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    
@app.route('/cancella', methods=['POST'])
def cancella():
    try:
        data = request.json
        email_cliente = data.get('email')  # Recupera l'email dal JSON

        if not email_cliente:
            return jsonify({'success': False, 'message': 'Email non fornita'}), 400
        
        # Cerca la prenotazione per email
        prenotazione = Prenotazione.query.filter_by(email_cliente=email_cliente).first()
        
        if prenotazione is None:
            return jsonify({'success': False, 'message': 'Prenotazione non trovata'}), 404

        # Se la prenotazione esiste, cancellala
        db.session.delete(prenotazione)
        db.session.commit()

        return jsonify({'success': True, 'message': 'Prenotazione cancellata con successo'})
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea le tabelle nel database se non esistono
    app.run(debug=True)
