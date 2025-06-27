from flask import Flask 

app = Flask(_name_)

@app.route('/')

def home():
    return "<h1>Mi primera pagina web con Flask!</p>"

if __name__ == '_main_':
    app.run(debug=True)



