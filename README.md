# Flask — Bloco 1: Iniciante

Projeto desenvolvido nas **Aulas 1 a 4** do Curso de Flask — Python para Desenvolvimento Web.

**Faculdade Santa Marcelina — FASM**  
Curso de Análise e Desenvolvimento de Sistemas  
Muriaé, MG — 2026

---

## Sobre o projeto

Aplicação web simples construída com Flask, cobrindo os fundamentos do framework: rotas, templates Jinja2 e formulários com validação. Simula uma loja fictícia com páginas de produtos e autenticação.

## Conteúdo por aula

| Aula | Tópico | O que foi implementado |
|------|--------|------------------------|
| 1 | Introdução ao Flask | Estrutura básica do `app.py`, inicialização da aplicação |
| 2 | Rotas e URLs | Rotas `/`, `/produto`, `/sobrenos`, `/login` com `@app.route` |
| 3 | Templates com Jinja2 | `base.html` com herança, loops `{% for %}`, condicionais `{% if %}` |
| 4 | Formulários e Validação | `LoginForm` com Flask-WTF, validadores `DataRequired`, `Email`, `Length` |

## Estrutura do projeto

```
1_INICIANTE/
├── app.py                  # Aplicação principal e rotas
├── requirements.txt        # Dependências do projeto
├── templates/
│   ├── base.html           # Template base com navbar e footer
│   ├── index.html          # Página inicial
│   ├── produto.html        # Listagem de produtos (Jinja2 loop)
│   ├── sobrenos.html       # Página sobre nós
│   └── login.html          # Formulário de login com Flask-WTF
└── venv/                   # Ambiente virtual (não versionado)
```

## Rotas disponíveis

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/produto` | GET | Lista de produtos |
| `/sobrenos` | GET | Sobre a turma |
| `/login` | GET, POST | Formulário de login com validação |

## Tecnologias utilizadas

- **Python 3.x**
- **Flask 3.1.3** — micro-framework web
- **Jinja2 3.1.6** — motor de templates
- **Flask-WTF 1.3.0** — integração Flask com WTForms
- **WTForms 3.2.1** — validação de formulários
- **email-validator 2.3.0** — validação de e-mail

## Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/aldecirfonseca/<nome-do-repositorio>.git
cd <nome-do-repositorio>
```

**2. Crie e ative o ambiente virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Execute a aplicação**
```bash
python app.py
```

**5. Acesse no navegador**
```
http://localhost:5000
```

> Com `debug=True` ativo, o servidor reinicia automaticamente ao salvar o arquivo.

## Conceitos demonstrados

- **Application Factory mínima** — `app = Flask(__name__)`
- **Decorador de rota** — `@app.route()` com suporte a múltiplos métodos HTTP
- **Herança de templates** — `{% extends %}` e `{% block %}` para evitar repetição de código
- **Passagem de variáveis** — `render_template()` com contexto de dados
- **Loop Jinja2** — `{% for produto in produtos %}` para listas dinâmicas
- **Formulário seguro** — `{{ form.hidden_tag() }}` para proteção CSRF automática
- **Validação server-side** — `form.validate_on_submit()` com feedback de erros no template

---

*Curso ministrado por Aldecir Fonseca — FASM Muriaé, MG*
