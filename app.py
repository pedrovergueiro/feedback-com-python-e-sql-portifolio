from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

USUARIO = {
    "username": "admin",
    "password": "123456"
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id == USUARIO['username']:
        return User(user_id)
    return None

def init_db():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedbacks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        nota INTEGER NOT NULL,
        comentario TEXT,
        data_hora TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return redirect(url_for('feedback'))

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        try:
            nota = int(request.form.get('nota'))
            if nota < 0 or nota > 10:
                flash('Nota deve ser entre 0 e 10', 'error')
                return redirect(url_for('feedback'))
        except:
            flash('Nota inválida', 'error')
            return redirect(url_for('feedback'))

        comentario = request.form.get('comentario', '').strip()
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()
        c.execute('INSERT INTO feedbacks (nome, nota, comentario, data_hora) VALUES (?, ?, ?, ?)',
                  (nome, nota, comentario, data_hora))
        conn.commit()
        conn.close()

        flash('Obrigado pelo seu feedback!', 'success')
        return redirect(url_for('feedback'))

    return render_template('feedback.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USUARIO['username'] and password == USUARIO['password']:
            user = User(username)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha incorretos', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Desconectado com sucesso!', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('SELECT nome, nota, comentario, data_hora FROM feedbacks ORDER BY data_hora DESC')
    feedbacks = c.fetchall()
    conn.close()

    total = len(feedbacks)
    promotores = len([f for f in feedbacks if f[1] >= 9])
    neutros = len([f for f in feedbacks if 7 <= f[1] <= 8])
    detratores = len([f for f in feedbacks if f[1] <= 6])
    media = round(sum(f[1] for f in feedbacks) / total, 2) if total > 0 else 0
    nps = (promotores / total - detratores / total) * 100 if total > 0 else 0

    return render_template('dashboard.html', feedbacks=feedbacks, promotores=promotores,
                           neutros=neutros, detratores=detratores, media=media, nps=round(nps, 2))

if __name__ == '__main__':
    app.run(debug=True)

