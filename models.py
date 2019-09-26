# models.py
import flask_sqlalchemy, flask, psycopg2, flask_socketio, app


# app.app = app modules app variable
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dee:deandra3@localhost/postgres'
db = flask_sqlalchemy.SQLAlchemy(app.app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key
    text = db.Column(db.String(120))

    def __init__(self, text):
        self.text = text
        
    def __repr__(self):
        return '<Message text: %s>' % self.text 
        