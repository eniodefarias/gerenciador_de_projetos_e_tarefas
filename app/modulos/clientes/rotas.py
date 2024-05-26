from . import clientes

@clientes.route('/')
def listar_clientes():
    # Lógica para listar clientes
    return 'Lista de clientes'
