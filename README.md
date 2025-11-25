# Cine_Python
gerenciador de filmes e series
cine_python – Sistema Web para Gestão Simples de Conteúdo em Flask

O cine_python é um aplicativo web desenvolvido em Python + Flask, criado com foco em estudo de desenvolvimento backend, organização de rotas, autenticação de usuários e estruturação de páginas HTML integradas ao servidor.

Esse projeto fornece uma base sólida para aplicações que exigem login, controle de sessão, páginas internas protegidas e expansão futura, mantendo uma arquitetura limpa, escalável e fácil de manter.


---

📌 Funcionalidades Principais

🔐 Autenticação completa

Verificação de usuário e senha

Controle de sessão por Flask Session

Proteção automática de rotas internas


📁 Arquitetura organizada

Separação entre backend (Flask) e frontend (templates)

Estrutura padronizada de pastas para escalabilidade


📄 Páginas internas protegidas

Página 1

Página 2

Página 3
(Apenas acessíveis após login)


🚪 Logout funcional

Remove sessão e força login novamente


🎨 Layout melhorado (HTML + CSS personalizado)
(Sem imagens, conforme pedido)

🧱 Código comentado e preparado para expansão



---

🏗️ Arquitetura do Projeto

cine_python/
│
├── app.py                # Arquivo principal que executa a aplicação Flask
├── requirements.txt      # Dependências do projeto
│
├── static/               # Arquivos estáticos (CSS, JS, ícones)
│   └── style.css
│
└── templates/            # Templates HTML renderizados pelo Flask
    ├── login.html
    ├── pagina1.html
    ├── pagina2.html
    ├── pagina3.html
    ├── base.html
    └── erro.html


---

🔧 Tecnologias Utilizadas

Tecnologia	Uso

Python 3.x	Linguagem principal
Flask	Servidor web, rotas, sessões
Werkzeug	Gerenciamento seguro de sessões
HTML5 / CSS3	Interface das páginas
Jinja2	Template engine do Flask



---

📚 Documentação das Rotas

🔐 /login – Tela de login (GET/POST)

Exibe o formulário

Verifica usuário e senha

Inicia sessão


/pagina1, /pagina2, /pagina3 – Rotas protegidas

Exigem sessão ativa

Redirecionam para /login se o usuário não estiver autenticado


/logout

Encerra a sessão

Redireciona para /login


/

Redirecionamento automático para a tela de login



---

▶️ Como Executar o Projeto (Tutorial Completo)

1. Instale as dependências

pip install -r requirements.txt

Se não tiver o arquivo, use:

pip install flask


---

2. Execute o servidor

python app.py


---

3. Abra no navegador

http://127.0.0.1:5000


---

👤 Credenciais de Acesso

Usuário: admin
Senha: 123
