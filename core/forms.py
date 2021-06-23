from django import forms 
from django.forms import ModelForm 
from .models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model= Categoria
        fields =['ID','Categoría']

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ['ID','Nombre de la Noticia','Cantidad de Noticias Subidas','Autor','Correo electrónico']