from flask import Blueprint, render_template

producto_bp = Blueprint('producto', __name__)

@producto_bp.route('/productos')
def listar_productos():
    # Aquí irá la lógica para consultar los productos en la base de datos de Laragon
    return "<h1>Inventario de Ferrocontrol</h1><p>Lista de productos disponibles.</p>"
