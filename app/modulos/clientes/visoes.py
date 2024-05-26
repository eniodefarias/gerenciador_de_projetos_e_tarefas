from flask import render_template
from . import clientes  # Importa o blueprint
from flask_login import login_required


@clientes.route('/')
@login_required
def listar_clientes():
    # Lógica para listar clientes
    return render_template('listar_clientes.html', clientes=clientes)



