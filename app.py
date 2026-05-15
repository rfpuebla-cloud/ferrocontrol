from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración para conectar con Laragon (ajusta 'ferrocontrol_db' al nombre de tu BD)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/ferrocontrol_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "<h1>Sistema Ferrocontrol</h1><p>El servidor Flask está funcionando correctamente.</p>"

if __name__ == '__main__':
    app.run(debug=True)