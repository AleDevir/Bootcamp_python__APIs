## Comando para executar o servidor (modo debug porta=8888):
```
python app.py
```

## Documentação utilizada:


+ [Favicon](https://flask.palletsprojects.com/en/2.3.x/patterns/favicon/)

+ [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)

+ [Fetching URLs](https://docs.python.org/3/howto/urllib2.html)

+ [Development Server](https://flask-fr.readthedocs.io/server/)

+ [Custom Error Pages](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

+ [Handling Application Errors](https://flask.palletsprojects.com/en/2.3.x/errorhandling/)

+ [Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/)


## Verificação Estática de Código (pylint e mypy):
```
pylint app.py

mypy --show-error-codes --check-untyped-defs app.py

```