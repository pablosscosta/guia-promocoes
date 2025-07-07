# 📘 Guia de Promoções

---

## 🧭 Visão Geral

Bem-vindo ao **Guia de Promoções**! Este é um sistema web intuitivo desenvolvido para centralizar e organizar promoções de restaurantes e bares. O objetivo é ajudar você a descobrir facilmente as melhores ofertas para sair, seja para um almoço casual ou uma noite divertida.

Este projeto está sendo desenvolvido como um **Produto Mínimo Viável (MVP)**, com foco nas funcionalidades essenciais de cadastro e visualização de promoções e estabelecimentos.

---

## 🧰 Tecnologias Utilizadas

- **Backend:** [Django](https://www.djangoproject.com/)
- **Frontend:** [Vue.js](https://vuejs.org/)
- **Ferramenta de Build (Frontend):** [Vite](https://vitejs.dev/)
- **Banco de Dados:** SQLite (para desenvolvimento, com planos de usar PostgreSQL em produção)
- **Controle de Versão:** Git & GitHub

---

## 💻 Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e rodar o **Guia de Promoções** em sua máquina local.

### ✅ Pré-requisitos

Certifique-se de ter instalado:

- **Python 3.9 ou superior**
- **Node.js 16 ou superior**
- **npm ou Yarn**
- **Git**

### ⚙️ Backend (Django)

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/guia-de-promocoes.git
   cd guia-de-promocoes/backend
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. **Instale as dependências do Django:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional, para acesso ao admin do Django):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor Django:**
   ```bash
   python manage.py runserver
   ```
   O backend estará disponível em `http://127.0.0.1:8000/`.

### 🖥️ Frontend (Vue.js + Vite)

1. **Acesse o diretório do frontend:**
   ```bash
   cd ../frontend
   ```

2. **Instale as dependências do Node.js:**
   ```bash
   npm install  # ou yarn install
   ```

3. **Inicie o servidor de desenvolvimento:**
   ```bash
   npm run dev  # ou yarn dev
   ```
   O frontend estará disponível em `http://localhost:5173/` (a porta pode variar).

---

## 📁 Estrutura do Projeto

```
guia-de-promocoes/
├── backend/                  # Projeto Django (API)
│   ├── guia_de_promocoes/    # Configurações globais do Django
│   ├── core/                 # Aplicativos Django (ex: promoções, estabelecimentos)
│   ├── manage.py             # Utilitário de linha de comando do Django
│   └── requirements.txt      # Dependências Python
├── frontend/                 # Projeto Vue.js (SPA)
│   ├── public/               # Arquivos estáticos públicos
│   ├── src/                  # Código-fonte Vue.js (componentes, rotas, stores)
│   ├── package.json          # Dependências Node.js
│   └── vite.config.js        # Configuração do Vite
├── .gitignore                # Arquivos a serem ignorados pelo Git
├── LICENSE                   # Licença do projeto
└── README.md                 # Este arquivo
```

---

## 🛣️ Roadmap (Pós-MVP)

- Autenticação de usuários
- Filtros avançados e pesquisa
- Funcionalidade de "favoritar" promoções
- Integração com mapas
- Sistema de avaliação/comentários
- Deploy em ambiente de produção

---

## 🤝 Como Contribuir

Contribuições são bem-vindas! Siga estas etapas:

1. Faça um fork do projeto.
2. Crie uma branch (`git checkout -b feature/sua-feature`).
3. Faça suas alterações e commit (`git commit -m 'feat: adiciona nova funcionalidade'`).
4. Envie para o seu fork (`git push origin feature/sua-feature`).
5. Abra um Pull Request.

---

## 📜 Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.