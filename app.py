from flask import Flask
from controllers.usuario_controller import usuario_bp
from controllers.producto_controller import producto_bp
from controllers.reporte_controller import reporte_bp

app = Flask(__name__)

# Registrar Blueprints (Ahora sí todos están activos)
app.register_blueprint(usuario_bp)
app.register_blueprint(producto_bp)
app.register_blueprint(reporte_bp)

@app.route('/')
def home():
    return """
    <div style="text-align:center; margin-top:50px;">
        <h1>FERROCONTROL</h1>
        <p>Sistema Modular funcionando correctamente</p>
        <hr>
        <a href="/usuarios">Usuarios</a> | 
        <a href="/productos">Productos</a> | 
        <a href="/reportes">Reportes</a>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)
