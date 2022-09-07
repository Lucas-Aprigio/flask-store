import os
from flask import render_template, session, request, url_for, flash, redirect
from .forms import LoginFormulario, RegistrationForm
from loja import app, db, bcrypt
from .models import User

@app.route('/')

def home():
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
        return redirect(url_for('home'))
    return render_template('admin/registrar.html', form=form, title="Pagina de registros")


@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginFormulario(request.form)
    return render_template('admin/login.html', form=form, title='Pagina Login')
  