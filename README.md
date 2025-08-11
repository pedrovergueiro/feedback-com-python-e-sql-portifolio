# 🚀 Sistema de Feedback com Cálculo de NPS

<!-- Use um GIF local: coloque o arquivo `starwars.gif` na pasta `static/` do repositório -->
<p align="center">
  <img alt="Star Wars" src="./static/starwars.gif" width="480"/>
</p>

## 📌 Descrição
Este projeto é um sistema de coleta de feedback com cálculo automático de **NPS (Net Promoter Score)**.  
O administrador pode visualizar:
- 📅 Data e hora de cada feedback
- ⭐ Nota atribuída pelo usuário
- 💬 Comentário
- 📊 Percentual do NPS em tempo real

## 🔧 Por que o GIF pode não carregar?
Alguns motivos comuns:
- O link externo (ex.: Giphy) foi bloqueado ou não é o link direto do GIF.
- O README está local e o navegador não tem acesso à internet.
- Alguns hosts não permitem hotlinking (uso direto do arquivo).
- O caminho no README está incorreto (use caminhos relativos quando o GIF estiver no repositório).

## ✅ Correção recomendada (melhor prática)
1. Crie a pasta `static/` na raiz do seu repositório (se ainda não existir).
2. Faça upload do GIF `starwars.gif` para `static/`.
3. No `README.md`, use caminho relativo para garantir que o GIF seja exibido no GitHub:
```markdown
![Star Wars](./static/starwars.gif)
```

### Como subir o GIF no GitHub (via Web UI)
1. Abra seu repositório no GitHub.
2. Clique em **Add file → Upload files**.
3. Arraste o `starwars.gif` para a área de upload dentro de `/static/` (crie a pasta `static` se necessário).
4. Commit das mudanças (escreva uma mensagem e clique em "Commit changes").

### Como subir o GIF via Git (CLI)
```bash
# dentro da pasta do projeto
mkdir -p static
cp /caminho/para/starwars.gif static/
git add static/starwars.gif
git commit -m "Adiciona starwars.gif para README"
git push origin main
```

Depois de subir, o GitHub mostrará o GIF no README usando o caminho relativo.

## 📁 Estrutura recomendada
```
feedback-nps/
├── app.py
├── feedback.db
├── requirements.txt
├── templates/
├── static/
│   └── starwars.gif   <-- coloque o GIF aqui
└── README.md
```

---

## 🖼️ Quer que eu crie um GIF simples pra você?
Posso gerar um GIF curto estilo "Star Wars crawl" (texto rolando) e te disponibilizar para download aqui, para você só fazer upload no `static/`.  
Quer que eu gere esse GIF agora e te mande o link para baixar? (responda "sim" ou "não")

---

**Se preferir, eu também posso:**
- te ajudar a pegar um GIF público do Giphy/Imgur com o link direto correto;
- ou atualizar o README com uma alternativa (GIF externo confiável ou imagem estática).

