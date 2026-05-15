from flask import Blueprint, render_template, request, redirect, url_for
# Aquí importarías tu modelo más adelante
# from models.usuario import Usuario 

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuarios')
def listar_usuarios():
    # Esta ruta servirá para ver a todos los empleados
    return "Lista de usuarios de Ferrocontrol"

@usuario_bp.route('/usuarios/nuevo', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        # Aquí irá la lógica para guardar en MySQL via Laragon
        return redirect(url_for('usuario.listar_usuarios'))
    return "Formulario de nuevo usuario"
