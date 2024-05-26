from flask import render_template
from . import clientes  # Importa o blueprint

@clientes.route('/')
def listar_clientes():
    # Lógica para listar clientes
    return render_template('listar_clientes.html', clientes=clientes)
