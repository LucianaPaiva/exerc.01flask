from flask import Flask, render_template, request

app = Flask(__name__)
lista_nomes = list()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get('nome')

    lista_nomes.append(nome)

    return """
    <script>
        alert('cadastro realizado com sucesso');
        window.location.href = '/';
    </script>
    """

@app.route("/visualizar")
def visualizar():
    return render_template('visualizar.html', lista_nomes)