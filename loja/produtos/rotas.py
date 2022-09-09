import os
from flask import redirect, render_template, url_for, flash, request, abort, session
from .forms import Addprodutos
from loja import db, app, basedir
from .models import Marca, Categoria, Produto
from werkzeug.utils import secure_filename
import secrets
from datetime import datetime
  



@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
    if 'email' not in session:
        flash(f'Realize o login!','danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getmarca = request.form.get('marca')
        marca = Marca(name=getmarca)
        db.session.add(marca)
        flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addmarca'))
    return render_template('/produtos/addmarca.html',marcas='marcas')

@app.route('/updatemarca/<int:id>', methods=['GET', 'POST'])
def updatemarca(id):
    if 'email' not in session:
        flash(f'Realize o login!','danger')
        return redirect(url_for('login'))
    updatemarca=Marca.query.get_or_404(id)
    marca = request.form.get('marca')
    if request.method == 'POST':
        updatemarca.name= marca
        flash(f'A marca foi atualizada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('marcas'))

    return render_template('/produtos/updatemarca.html',title='Atualizar Marca', updatemarca=updatemarca)

@app.route('/updatecat/<int:id>', methods=['GET', 'POST'])
def updatecat(id):
    if 'email' not in session:
        flash(f'Realize o login!','danger')
        return redirect(url_for('login'))
    updatecat=Categoria.query.get_or_404(id)
    categoria = request.form.get('categoria')
    if request.method == 'POST':
        updatecat.name= categoria
        flash(f'A categoria foi atualizada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('categorias'))

    return render_template('/produtos/updatemarca.html',title='Atualizar Categoria', updatecat=updatecat)

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if 'email' not in session:
        flash(f'Realize o login!','danger')
        return redirect(url_for('login'))

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
    if 'email' not in session:
        flash(f'Realize o login!','danger')
        return redirect(url_for('login'))

    marcas = Marca.query.all()
    categorias = Categoria.query.all()
    form = Addprodutos(request.form)
    if request.method == 'POST':

        name= form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        weight= form.weight.data
        description= form.description.data
        marca= request.form.get('marca')
        categoria= request.form.get('categoria')

        addpro = Produto(name=name,price=price,discount=discount,stock=stock,weight=weight,description=description,marca_id=marca,categoria_id=categoria)
        db.session.add(addpro) 
        flash(f'O produto {name} foi adicionado com sucesso')
        db.session.commit()
        return redirect(url_for('admin'))
    
    return render_template('/produtos/addproduto.html',title='Cadastrar Produtos', form=form, marcas=marcas, categorias=categorias)

@app.route('/updateproduto/<int:id>', methods=['GET', 'POST'])
def updateproduto(id):
    if 'email' not in session:
        flash(f'Realize o login!','danger')
        return redirect(url_for('login'))
    
    marcas = Marca.query.all()
    categorias = Categoria.query.all()
    produto = Produto.query.get_or_404(id)
    marca= request.form.get('marca')
    categoria= request.form.get('categoria')
    form= Addprodutos(request.form)
    if request.method == 'POST':
        produto.marca_id = marca
        produto.categoria_id = categoria

        produto.name = form.name.data
        produto.price = form.price.data
        produto.description = form.description.data
        produto.stock = form.stock.data
        produto.weight = form.weight.data
        produto.discount = form.discount.data

        db.session.commit()
        flash(f'O produto foi atualizado com sucesso','success')
        return redirect(url_for('admin'))

    form.name.data = produto.name
    form.price.data = produto.price
    form.description.data = produto.description
    form.stock.data = produto.stock
    form.weight.data = produto.weight
    form.discount.data = produto.discount


    return render_template('/produtos/updateproduto.html',title='Atualizar Produtos', form=form, marcas=marcas, categorias=categorias, produto=produto)
