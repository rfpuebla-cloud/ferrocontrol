from flask import Flask
from controllers.usuario_controller import usuario_bp
# Nota: Asegúrate de crear estos archivos también para que no de error
# from controllers.producto_controller import producto_bp
# from controllers.reporte_controller import reporte_bp

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(usuario_bp)
# app.register_blueprint(producto_bp)
# app.register_blueprint(reporte_bp)

@app.route('/')
def home():
    return """
    <h1>FERROCONTROL</h1>
    <p>Sistema funcionando correctamente</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
