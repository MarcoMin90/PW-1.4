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
