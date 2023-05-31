# Loja de aluguel de roupa

## Description

Projeto Django de um site de aluguel de roupa.

## Instalação

Crie um arquivo .env criado com as credenciais do seu banco de dados conforme o _.env_ abaixo.

```bash
$ python -m venv /path/to/your/environment
$ pip install -r requirements.txt
```

## Rodar o app

```bash
# development
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Environment variables

Se deseja rodar sua aplicação num banco de dados que não o padrão Sqlite3. Cire um aquivo ._env_.
```bash
# .env
DB_NAME=""
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
DB_PORT=""
```

Mude a variável de banco de dados no _settings.py_ para funcionar.

```bash
#django_faculdade_site/settings.py
 DATABASES_other = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': env('DB_NAME'),
         'USER': env('DB_USER'),
         'PASSWORD': env('DB_PASSWORD'),
         'HOST': env('DB_HOST'),
         'PORT': env('DB_PORT'),
     }
 }
```

## Stay in touch

- Author - [pedromiguel-dev](http://github.com/pedromiguel-dev)
- Twitter - [Quem amou?🏳️‍🌈](https://twitter.com/PrincesaSofiaQA)
- LinkedIn - [ Pedro Miguel (ele/dele) ](https://www.linkedin.com/in/pedro-miguel-276525207/)


### License

Under MIT License.
