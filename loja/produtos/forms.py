from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField,StringField,BooleanField, TextAreaField, FloatField, validators



class Addprodutos(Form):
    name = StringField('Nome:', [validators.DataRequired()]) 
    price = IntegerField('Preço:', [validators.DataRequired()])
    weight = FloatField('Peso em kg:', [validators.DataRequired()])
    discount = IntegerField('Desconto:', [validators.DataRequired()])
    stock = IntegerField('Estoque:', [validators.DataRequired()])
    description = TextAreaField('Descrição:', [validators.DataRequired()])
    image = FileField('Imagem:',validators=[FileRequired(),FileAllowed(['jpg','png','gif','jpeg'])])
