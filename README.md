# 📘 Guia de Promoções

Aplicação web para listar promoções de bares e restaurantes por região.  
Desenvolvida com Django no backend e Vue.js no frontend, com consumo via API e painel administrativo.

---

## 📌 Visão Geral / Contexto

Este projeto foi criado para facilitar a divulgação de promoções locais em estabelecimentos gastronômicos.  
Permite que usuários visualizem ofertas por região, enquanto o cadastro é feito por administradores via painel Django ou requisições autenticadas.  
É voltado para empreendedores, gestores de bares e restaurantes, e profissionais de marketing local.

---

## 📊 Status do Projeto

- 🧪 MVP funcional  
- 🚧 Em evolução, com novas funcionalidades planejadas  

---

## 🚀 Tecnologias Utilizadas

- Python  
- Django  
- Django REST Framework  
- Vue.js  
- TypeScript  
- HTML  
- CSS  
- PostgreSQL  

---

## 🛠️ Funcionalidades

- [x] Listagem de promoções por região  
- [x] Cadastro de estabelecimentos via Django Admin ou API  
- [x] Painel administrativo para gestão de dados  
- [x] Integração frontend-backend via API REST  
- [ ] Interface pública para cadastro (planejada)  
- [ ] Autenticação de usuários finais (planejada)  
- [ ] Melhorias de responsividade no frontend (planejada)  

---

## 📘 Como Rodar o Projeto
Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### 🔧 Pré-requisitos
- Python 3.8+  
- pip (gerenciador de pacotes Python)  
- Node.js (LTS recomendado)  
- npm (gerenciador de pacotes Node.js)  

---

### ⚙️ Configuração do Backend (Django)
```bash
# Navegue até a pasta backend
cd backend

# Crie e ative um ambiente virtual (recomendado)
python -m venv venv

# No Windows:
.\venv\Scripts\activate

# No macOS/Linux:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

O backend estará acessível em: **http://127.0.0.1:8000/api/**  
Nesta URL você verá a página do Django REST Framework com os endpoints disponíveis.  
Popule o banco de dados com dados iniciais via **Django Admin (/admin/)** ou ferramentas como **Postman**.

---

### 🧪 População do Banco com Postman
Após iniciar o servidor, você pode cadastrar dados fictícios para testes usando requisições **POST**.

#### 📌 Endpoints disponíveis
- Categorias: `http://127.0.0.1:8000/api/categories/`
- Estabelecimentos: `http://127.0.0.1:8000/api/establishments/`  
- Promoções: `http://127.0.0.1:8000/api/promotions/`  

---

#### 📌 Exemplo: Cadastro de Estabelecimentos
```json
{
  "name": "Bar"
}
```

```json
{
  "name": "Restaurante"
}
```

```json
{
  "name": "Pizzaria"
}
```

```json
{
  "name": "Cafeteria"
}
```

---

#### 📌 Exemplo: Cadastro de Estabelecimentos
```json
{
  "name": "Estabelecimento Genérico A",
  "phone_number": "(00) 00000-0000",
  "address": "Rua Exemplo, 100",
  "categories": [1]
}
```

```json
{
  "name": "Estabelecimento Genérico B",
  "phone_number": "(11) 11111-1111",
  "address": "Avenida Modelo, 200",
  "categories": [2]
}
```

---

#### 📌 Exemplo: Cadastro de Promoções
Promoções vinculadas ao **Estabelecimento Genérico A** (ID = 1):
```json
{
  "title": "Promoção Teste 1",
  "description": "Descrição fictícia da promoção 1.",
  "establishment": 1
}
```

```json
{
  "title": "Promoção Teste 2",
  "description": "Descrição fictícia da promoção 2.",
  "establishment": 1
}
```

Promoções vinculadas ao **Estabelecimento Genérico B** (ID = 2):
```json
{
  "title": "Promoção Teste 3",
  "description": "Descrição fictícia da promoção 3.",
  "establishment": 2
}
```

```json
{
  "title": "Promoção Teste 4",
  "description": "Descrição fictícia da promoção 4.",
  "establishment": 2
}
```

> ⚠️ Observação:

- O campo `establishment` deve referenciar o **ID** retornado pelo cadastro dos estabelecimentos.
- O campo `categories` deve referenciar os **IDs** das categorias previamente cadastradas.

---

### 🎨 Configuração do Frontend (Vue.js)
```bash
# Abra um novo terminal e navegue até a pasta frontend
cd frontend

# Instale as dependências
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

O frontend estará acessível em: **http://localhost:5173/**

---

### 💻 Uso
Após iniciar ambos os servidores (backend e frontend), acesse **http://localhost:5173/** em seu navegador para interagir com o aplicativo.  
Os links de navegação para **Estabelecimentos** e **Promoções** estarão disponíveis na página inicial.

---

## 📂 Estrutura do Projeto
```
guia-promocoes/
│
├── backend/
│   ├── core/              # Models, serializers e views
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/               # Código Vue.js
│   └── package.json
│
└── README.md
```

---

## ⏭️ Próximas Etapas

- [ ] Criar interface pública para cadastro de estabelecimentos e promoções

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 👤 Autor / Contato

**Pablo Sousa da Costa**  
[LinkedIn](https://www.linkedin.com/in/pablosilva013/)  
📧 pablosousa013@gmail.com
