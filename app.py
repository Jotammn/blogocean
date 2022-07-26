from flask import Flask

app = Flask("hello")
@app.route("/hello")
@app.route("/")
def hello():
    return "Hello World"

@app.route("/meucontato")
def meuContato():
    return """<html>
    <head>
    <title> Contatos </title>
    </head>
    <body>
    <a href="https://www.oceanbrasil.com/"> Isso é um link </a>
    <h1>Jota </h1> 
    <h2>telex@gmail.com </h2>
    <h3>13985652577</h3>
    </body>
    </html>"""