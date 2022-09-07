import os
from flask import redirect, render_template, url_for, flash, request, abort
from .forms import Addprodutos
from loja import db, app, ALLOWED_EXTENSIONS, basedir
from .models import Marca, Categoria
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config['UPLOAD_FOLDER'] = os.path.join(basedir,'static/images')

@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
    if request.method == "POST":
        getmarca = request.form.get('marca')
        marca = Marca(name=getmarca)
        db.session.add(marca)
        flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addmarca'))
    return render_template('/produtos/addmarca.html',marcas='marcas')

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == "POST":
        getmarca = request.form.get('categoria')
        cat = Categoria(name=getmarca)
        db.session.add(cat)
        flash(f'A Categoria {getmarca} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('/produtos/addmarca.html',categoria='categoria')

@app.route('/addproduto', methods=['GET', 'POST'])
def addproduto():
    marcas = Marca.query.all()
    categorias = Categoria.query.all()
    form = Addprodutos(request.form)
    if request.method=="POST":
        file = request.files['image']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('addproduto'))
        
        filename = secure_filename(file.filename)
        file.save(app.config['UPLOAD_FOLDER'], filename)
        return render_template('/produtos/addproduto.html',title='Cadastrar Produtos', form=form, marcas=marcas, categorias=categorias)    
    return render_template('/produtos/addproduto.html',title='Cadastrar Produtos', form=form, marcas=marcas, categorias=categorias)
