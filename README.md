# 🚀 Sistema de Feedback com NPS

<p align="center">
  <img src="https://media.giphy.com/media/ETjjp8skvlTGM/giphy.gif" alt="Star Wars" width="480"/>
</p>

---

## 🔧 Tecnologias Utilizadas

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="40" height="40"/>
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" alt="Flask" width="40" height="40"/>
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" alt="SQLite" width="40" height="40"/>
</p>

---

## 📌 Sobre o Projeto

Este é um sistema simples para coleta de feedback com cálculo automático do **NPS** (Net Promoter Score), feito com Python e Flask, armazenando dados em SQLite.

---

## 🚀 Como rodar o projeto

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\\Scripts\\activate   # Windows
pip install -r requirements.txt
python app.py
```

---

## 📊 Funcionalidades

- Formulário para envio de feedback (nota 0-10, comentário e nome opcional)
- Dashboard protegido por login para visualizar:
  - NPS em tempo real
  - Lista de feedbacks com data, hora, nota e comentário

---

## 📂 Estrutura do projeto

```
feedback-nps/
├── app.py
├── feedback.db
├── requirements.txt
├── templates/
│   ├── feedback.html
│   ├── login.html
│   └── dashboard.html
├── static/
│   └── style.css
└── README.md
```

---

## 👨‍💻 Autor

Pedro Lucas Vergueiro

---

✨ *Que a Força esteja com você!* ✨
