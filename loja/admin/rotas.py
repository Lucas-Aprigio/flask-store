import os
from flask import render_template, session, request, url_for, flash, redirect
from .forms import LoginFormulario, RegistrationForm
from loja import app, db, bcrypt
from .models import User

@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Realize o login!','danger')
        return redirect(url_for('login'))
    return render_template('admin/index.html', title = 'Pagina administrativa')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Olá, {form.name.data}. Sua conta foi criada com sucesso!','success')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Pagina de registros")


@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginFormulario(request.form)
    if request.method == 'POST'and form.validate():
        user= User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Olá, {form.email.data}. Seja bem-vindo!','success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('E-mail ou senha incorretos. Por favor, tente novamente','danger')
    return render_template('admin/login.html', form=form, title='Pagina Login')
  