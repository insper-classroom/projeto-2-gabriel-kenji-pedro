from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string('''
        <h1>Bem-vindo ao Servidor Flask!</h1>
        <p>Este é um exemplo de servidor Flask simples.</p>
    ''')
    
if __name__ == '__main__':
    app.run(debug=True)