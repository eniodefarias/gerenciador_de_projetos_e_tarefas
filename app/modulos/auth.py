from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..modelos import Usuario

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario.query.filter_by(username=request.form['username']).first()
        if usuario is not None and usuario.check_password(request.form['password']):
            login_user(usuario)
            return redirect(url_for('main.index'))
        flash('Usuário ou senha inválidos.')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
