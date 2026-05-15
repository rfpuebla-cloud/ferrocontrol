from flask import Blueprint, render_template

venta_bp = Blueprint('venta', __name__)

@venta_bp.route('/ventas')
def listar_ventas():
    # En el futuro, aquí traerás los datos de MySQL
    # Por ahora, enviamos la vista que creamos antes
    return render_template('ventas/index.html')

@venta_bp.route('/ventas/nueva')
def nueva_venta():
    return "<h1>Formulario de Nueva Venta</h1><p>Aquí se elegirán los productos.</p>"
