from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def inicial():
    return render_template('template.html')


@app.route('/exemplos')
def exemplos():
    return render_template('exemplos.html')


@app.route('/exercicios')
def exercicios():
    return render_template('exercicios.html')

@app.route('/exemplos/texto')
def texto():
    return render_template('texto.html')

@app.route('/exemplos/midia')
def midia():
    return render_template('midia.html')

@app.route('/exemplos/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/exemplos/divs')
def divs():
    return render_template('divs.html')

@app.route('/exemplos/texto_css')
def texto_css():
    return render_template('texto_css.html')












if __name__ == '__main__':
    app.run(debug=True)