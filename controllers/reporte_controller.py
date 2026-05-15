from flask import Blueprint

reporte_bp = Blueprint('reporte', __name__)

@reporte_bp.route('/reportes')
def ver_reportes():
    return "<h1>Reportes de Ventas</h1><p>Gráficos y estadísticas de Ferrocontrol.</p>"
