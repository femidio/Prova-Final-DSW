from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample data
disciplinas = [
    {"disciplina": "DSWA5", "semestre": "5º semestre"},
    {"disciplina": "TCOA5", "semestre": "5º semestre"},
    {"disciplina": "IHCA5", "semestre": "5º semestre"},
    {"disciplina": "SODA5", "semestre": "5º semestre"},
    {"disciplina": "PJIA5", "semestre": "5º semestre"},
    {"disciplina": "s", "semestre": "4º semestre"},
    {"disciplina": "teste", "semestre": "6º semestre"}
]

# Routes
@app.route('/')
def home():
    local_datetime = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template('index.html', aluno='Francisco Emidio', prontuario='PT3021912', datetime=local_datetime)

@app.route('/cadastro_disciplinas', methods=['GET', 'POST'])
def cadastro_disciplinas():
    global disciplinas
    if request.method == 'POST':
        disciplina = request.form.get('disciplina')
        semestre = request.form.get('semestre')
        disciplinas.append({"disciplina": disciplina, "semestre": semestre})
        return redirect(url_for('cadastro_disciplinas'))
    return render_template('cadastro_disciplinas.html', disciplinas=disciplinas)

@app.route('/cadastro_professores')
@app.route('/cadastro_alunos')
def not_available():
    return render_template('not_available.html')

if __name__ == '__main__':
    app.run(debug=True)
