'''
API Flask Rick & Morty

Para executar a aplicação:
$ python app.py

Documentação

Favicon:
https://flask.palletsprojects.com/en/2.3.x/patterns/favicon/


Jinja2:
https://jinja.palletsprojects.com/en/3.1.x/


Fetching URLs
https://docs.python.org/3/howto/urllib2.html


Development Server:
https://flask-fr.readthedocs.io/server/


Custom Error Pages:
https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/


Handling Application Errors
https://flask.palletsprojects.com/en/2.3.x/errorhandling/

Quickstart
https://flask.palletsprojects.com/en/1.1.x/quickstart/
'''

import os
from typing import Any
import json
import urllib.request
from flask import Flask, render_template, send_from_directory, redirect
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    '''
    favicon:
    https://flask.palletsprojects.com/en/2.3.x/patterns/favicon/
    '''
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon'
    )


@app.route('/')
def home():
    '''
    Página principal
    '''
    return render_template('home.html')

#####################################################
####           APIs   RICK  &  MORTY             ####
#####################################################

def get_json_data_for(url: str) -> dict[str, Any]:
    '''
    Retorna os dados da URL informada.
    https://docs.python.org/3/howto/urllib2.html
    https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
    '''
    with urllib.request.urlopen(url) as response:
        response_data = response.read()
        data = json.loads(response_data)
        return data


@app.route('/api/personagens/<int:page>')
def api_personagens(page: int) -> dict[str, Any]:
    '''
    Personagens
    '''
    return get_json_data_for(f"https://rickandmortyapi.com/api/character?page={page}")


@app.route('/api/personagem/<int:idt>')
def api_personagem(idt: int) -> dict[str, Any]:
    '''
    Personagem
    '''
    return get_json_data_for(f"https://rickandmortyapi.com/api/character/{idt}")


@app.route('/api/episodios/<int:page>')
def api_episodios(page: int) -> dict[str, Any]:
    '''
    Episódios
    '''
    return get_json_data_for(f"https://rickandmortyapi.com/api/episode?page={page}")


@app.route('/api/episodio/<int:idt>')
def api_episodio(idt: int) -> dict[str, Any]:
    '''
    Episódio
    '''
    return get_json_data_for(f"https://rickandmortyapi.com/api/episode/{idt}")


@app.route('/api/localizacoes/<int:page>')
def api_localizacoes(page: int) -> dict[str, Any]:
    '''
    Localizações
    '''
    return get_json_data_for(f"https://rickandmortyapi.com/api/location?page={page}")


@app.route('/api/localizacao/<int:idt>')
def api_localizacao(idt: int) -> dict[str, Any]:
    '''
    Localização
    '''
    return get_json_data_for(f"https://rickandmortyapi.com/api/location/{idt}")


#####################################################
####        PÁGINAS   RICK  &  MORTY             ####
#####################################################

@app.route('/personagens')
def personagens_sem_pagina():
    '''
    Personagens
    '''
    return redirect('/personagens/1')


@app.route('/personagens/<int:page>')
def personagens(page: int):
    '''
    Personagens
    '''
    data = api_personagens(page)
    return render_template('personagens.html', dados=data, page=page)


@app.route('/personagem/<int:idt>')
def personagem(idt: int):
    '''
    Personagem
    '''
    print(f"Personagem ID={idt}")
    return '<h1 style="color: red;">Fazer a renderização da página com informações de um personagem.<h1/>'


@app.route('/episodios')
def episodios_sem_pagina():
    '''
    Episódios
    '''
    return redirect('/episodios/1')


@app.route('/episodios/<int:page>')
def episodios(page: int):
    '''
    Episódios
    '''
    print(f"Episódios PAGE={page}")
    return '<h1 style="color: red;">Fazer a renderização da página com informações dos episódios.<h1/>'


@app.route('/personagens_do_episodio/<int:idt>')
def personagens_do_episodio(idt: int):
    '''
    Episódio de identificador informado.
    '''
    print(f"Episódio ID={idt}")
    return '<h1 style="color: red;">Fazer a renderização da página com as informações de um episódio e seus personagens.<h1/>'



@app.route('/localizacoes')
def localizacoes_sem_pagina():
    '''
    Localizações
    '''
    return redirect('/localizacoes/1')


@app.route('/localizacoes/<int:page>')
def localizacoes(page: int):
    '''
    Localizações
    '''
    print(f"Localizações PAGE={page}")
    return '<h1 style="color: red;">Fazer a renderização da página com as informações das localizações.<h1/>'


@app.route('/residentes_da_localizacao/<int:idt>')
def residentes_da_localizacao(idt: int):
    '''
    residentes de identificador informado.
    '''
    print(f"Localização ID={idt}")
    return '<h1 style="color: red;">Fazer a renderização da página com as informações de uma localização e seus residentes (personagens).<h1/>'



#####################################################
####           TRATAMENTO  DE  ERROS             ####
#####################################################

@app.errorhandler(404)
def page_not_found(exeption):
    '''
    Página não encontrada
    status code = 404
    https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
    '''
    print(f"type(exeption)={type(exeption)}")
    print(str(exeption))

    return render_template('erro.html', msg='Página não encontrada!'), 404


@app.errorhandler(500)
def page_error(exeption):
    '''
    Erro inesperado
    status code = 500
    https://flask.palletsprojects.com/en/2.3.x/errorhandling/#further-examples
    '''
    print(f"type(exeption)={type(exeption)}")
    print(str(exeption))

    return render_template('erro.html', msg='Ops! Ocorreu um erro inesperado.'), 500


@app.errorhandler(Exception)
def handle_exception(exception: Exception):
    '''
    Captura as exceções
    https://flask.palletsprojects.com/en/2.3.x/errorhandling/
    '''
    if isinstance(exception, HTTPException):
        return exception
    return render_template("erro.html", msg=str(exception)), 500


if __name__ == "__main__":
    # Modo debug reinicia automaticamente o servidor a cada alteração.
    # Development Server:
    # https://flask-fr.readthedocs.io/server/
    app.run(debug=True, port=8888)
