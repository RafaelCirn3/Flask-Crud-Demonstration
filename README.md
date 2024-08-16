# Flask CRUD Application with Bootstrap

Este é um projeto Flask que implementa um CRUD (Create, Read, Update, Delete) básico utilizando Bootstrap para estilização. O objetivo principal é fornecer um exemplo educativo de como construir uma aplicação web com Flask e como aplicar estilos com Bootstrap.

## Funcionalidades

### 1. **Listagem de Itens**
- **Página Principal**: Exibe uma lista de todos os itens no banco de dados.
- **Ações**: Inclui opções para editar e excluir itens.

### 2. **Criação de Itens**
- **Formulário de Criação**: Permite adicionar um novo item ao banco de dados.
- **Validação**: O nome do item é obrigatório.

### 3. **Atualização de Itens**
- **Formulário de Edição**: Permite atualizar as informações de um item existente.
- **Validação**: O nome do item é obrigatório.

### 4. **Exclusão de Itens**
- **Confirmação de Exclusão**: Permite excluir um item após confirmação.

## Estrutura do Projeto

O projeto é estruturado da seguinte forma:

## Como Instalar

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
### 2. Criar e Ativar um Ambiente Virtual
python -m venv env
source env/bin/activate   # No Windows: env\Scripts\activate
### 3. Instalar as Dependências
python -m venv env
source env/bin/activate   # No Windows: env\Scripts\activate
### 4. Executar a Aplicação
python app.py

A aplicação estará disponível em http://127.0.0.1:5000/.

Como Usar
### 1. Acessar a Página Principal
URL: http://127.0.0.1:5000/
Descrição: Exibe a lista de itens com opções para adicionar, editar e excluir.
### 2. Criar um Novo Item
URL: http://127.0.0.1:5000/create
Descrição: Formulário para criar um novo item.
### 3. Atualizar um Item Existente
URL: http://127.0.0.1:5000/update/<id>
Descrição: Formulário para atualizar um item existente.
### 4. Excluir um Item
URL: http://127.0.0.1:5000/delete/<id>
Descrição: Confirmação de exclusão de um item.
### ependências
Flask: >=2.0.0
Flask-SQLAlchemy: >=2.5.0
Bootstrap: Utilizado via CDN para estilização.
### Notas Finais
Este projeto é uma demonstração básica de CRUD com Flask e Bootstrap. Ele é ideal para fins educacionais e pode ser expandido com mais funcionalidades conforme necessário.

Para quaisquer dúvidas ou contribuições, sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório.