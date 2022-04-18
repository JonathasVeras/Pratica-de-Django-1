# projeto-django1
 1° Projeto feito para praticar Django

*Ter versão atualizada do Python;
*Recomenda-se usar o Pycharm por ele facilitar o uso do ambiente virtual;
*Comando no terminal:
*Ter certeza que está em um ambiente virtual

pip install django

pip freeze > requeriments.txt (para criar o documento onde irá sinalizar as versões das dependências instaladas)

django-admin startproject django1 . (Criação do projeto, ps: O ponto no final é importante)

*Modificar na ‘settings.py’, no local “templates” na parte ‘DIRS’, colocar lá dentro ‘templates’

*Criar um app pelo terminal:
django-admin startapp core

*Modificar na ‘settings.py’, no local ‘INSTALED APPS’, colocar o nome da nova aplicação, que nesse caso seria ‘core’.

*Rodando o server (no console)
python manage.py runserver

*Criando uma views:
def index(request):
   return render(request, 'index.html')

*No projeto (que aqui é django1) iremos criar as URLs que irão direcionar para as viwes:

Ir na página urls.py e colocar:
from core.views import index
*E na parte ‘urlpatters colocar:
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', index),
   path('contact', contact),
]

Porém o recomendado seria diluir isso porque em uma aplicação muito grande isso poderia gerar confusão:

from django.contrib import admin
from django.urls import path, include
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('core.urls')),
]


E cria uma urls.py na pasta core, lá dentro coloca:
from django.urls import path
from .views import index

urlpatters = [
   path('', index)
]

ORGANIZANDO OS TEMPLATES
*Criar um novo diretorio na pasta core chamado ‘templates’, cada app deve ter seus templates. Lá cria as páginas HTML que estavam configuradas em URLS. Lá fica o HTML básico, deixando bem claro que podemos passar informações de views para os templates (Olhar no exemplo).

SOBRE MODELS
Cada aplicação tem seu models.
CRIANDO UM MODELS: Basta ir na pasta models e seguir um exemplo assim:
from django.db import models


class Product(models.Model):
   name = models.CharField('Nome', max_length=100)
   price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
   inventory = models.IntegerField('Quantidade em Estoque')

É sempre importante fazer as migrações depois que mudar algo no banco de dados, serve para gerenciar o histórico de migrações do seu banco de dados

python manage.py makemigrations

*E para executar

 python manage.py migrate

Você pode usar o DB Browser (SQLite) para checar o banco de dados.

CRIANDO UM SUPER USUÁRIO
python manage.py createsuperuser

Para fazer com que as tabelas apareçam na página, deve-se modificar a página admin.py do app dessa forma, por exemplo:
from django.contrib import admin

from .models import Product, Client

admin.site.register(Product)
admin.site.register(Client)


Indo no endereço /admin há algumas ferramentas para adicionar elementos a tabelas feitas no banco.

Para fazer com que na página fique tabelado cada elemento, deve modificar dessa forma na página admin.py:
from django.contrib import admin

from .models import Product, Client


class ProductAdmin(admin.ModelAdmin):
   list_display = ('nome', 'preço', 'estoque')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client)

