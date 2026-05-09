from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY']                        = 'fasm-2026-3p'

# Define o formulário de login
class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Entrar')

@app.route("/")
def index():
    return render_template(
            'index.html',
            titulo='Loja FASM'
        )

@app.route("/produto")
def produto():
    produtos = [
        {'nome': 'Notebook', 'preco': 6499.99},
        {'nome': 'Mouse', 'preco': 75.99}
    ]

    return render_template(
            'produto.html',
            titulo='Loja FASM',
            produtos=produtos
        )

@app.route("/sobrenos")
def sobrenos():
    return render_template(
        "sobrenos.html",
        titulo="Sobre nós",
        mensagem=""
    )

# Rota Login
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # se os dados forem válidos, redireciona para index
        return render_template(
            'index.html',
            titulo='Login',
            mensagem=f"Login feito com sucesso para {form.email.data}"
        )

    return render_template(
            "login.html", 
            titulo="Login", 
            form=form
        )

if __name__ == "__main__":
    app.run(debug=True)