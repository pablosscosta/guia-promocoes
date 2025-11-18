# Guia de Promoções

Este é o Produto Mínimo Viável (MVP) do aplicativo "Guia de Promoções". O objetivo desta versão é apresentar uma plataforma funcional para listar estabelecimentos e suas promoções associadas. **O cadastro de dados (categorias, estabelecimentos e promoções) é feito via painel administrativo do Django ou através de requisições diretas à API.**

## Funcionalidades do MVP

Atualmente, o aplicativo oferece as seguintes funcionalidades:

* **Home:** Página inicial de boas-vindas com links de navegação para as demais seções.
* **Listagem de Estabelecimentos:** Visualização de todos os estabelecimentos cadastrados, incluindo nome, telefone e endereço.
* **Listagem de Promoções:** Visualização de todas as promoções, com título, descrição e o estabelecimento associado.

## Tecnologias

* **Backend:** Django, Django REST Framework
* **Frontend:** Vue.js 3 (com Composition API), Vite, Tailwind CSS, Axios, Vue Router
* **Banco de Dados:** SQLite (padrão Django, para desenvolvimento)

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

* Python 3.8+
* pip (gerenciador de pacotes Python)
* Node.js (LTS recomendado)
* npm (gerenciador de pacotes Node.js)

### Configuração do Backend (Django)

1.  Navegue até a pasta `backend`:
    ```bash
    cd backend
    ```
2.  Crie e ative um ambiente virtual (recomendado):
    ```bash
    python -m venv venv
    # No Windows:
    # .\venv\Scripts\activate
    # No macOS/Linux:
    # source venv/bin/activate
    ```
3.  Instale as dependências Python a partir do `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
4.  Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
5.  Crie um superusuário para acessar o painel Admin (se ainda não tiver):
    ```bash
    python manage.py createsuperuser
    ```
6.  Popule o banco de dados com dados iniciais (categorias, estabelecimentos, promoções) usando o painel Django Admin (`/admin/`) ou ferramentas como Postman.
7.  Inicie o servidor Django:
    ```bash
    python manage.py runserver
    ```
    O backend estará acessível em `http://127.0.0.1:8000/`.

### Configuração do Frontend (Vue.js)

1.  Abra um **novo terminal** e navegue até a pasta `frontend`:
    ```bash
    cd frontend
    ```
2.  Instale as dependências Node.js:
    ```bash
    npm install
    ```
3.  Inicie o servidor de desenvolvimento Vue.js:
    ```bash
    npm run dev
    ```
    O frontend estará acessível em `http://localhost:5173/`.

## Uso

Após iniciar ambos os servidores (backend e frontend), acesse `http://localhost:5173/` em seu navegador para interagir com o aplicativo. Os links de navegação para **Estabelecimentos** e **Promoções** estarão disponíveis na página inicial.


## Próximos Passos

Este projeto está em evolução contínua. Novas funcionalidades e melhorias serão implementadas nas próximas versões.


## Autor

[Pablo S. S. Costa](https://github.com/pablosscosta/) / [LinkedIn](https://www.linkedin.com/in/pablosilva013/)
