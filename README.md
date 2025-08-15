# Projeto Estoque

Sistema de **controle de estoque** desenvolvido em **Django** para gerenciamento de produtos, movimentações e relatórios.

---

## 📌 Funcionalidades

- **Cadastrar Produtos**
  - Registro de nome, quantidade e preço.
  - Entrada automática no histórico de movimentações.

- **Listar Produtos**
  - Visualização de todos os produtos cadastrados com quantidade e preço.

- **Movimentações**
  - Registro de entradas e saídas de produtos.
  - Histórico detalhado com data e tipo da movimentação.

- **Dar Baixa**
  - Reduz a quantidade de produtos em estoque.
  - Criação automática de movimentação de saída.

- **Relatórios**
  - Total de itens no estoque.
  - Valor total do estoque.
  - Gráfico de barras mostrando a quantidade de cada produto.
  - Tabela detalhada com preço unitário e valor total por produto.

---

## 🛠 Tecnologias

- **Backend:** Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Banco de Dados:** SQLite  
- **Gráficos:** Chart.js  

---

## 📂 Estrutura do Projeto

```
Projeto_Estoque/
┣ .git/
┣ .github/
┃ ┗ workflows/
┃ ┗ django.yml
┣ estoque/
┃ ┣ migrations/
┃ ┣ static/
┃ ┃ ┣ css/
┃ ┃ ┃ ┣ cadastrar_produto.css
┃ ┃ ┃ ┣ navbar.css
┃ ┃ ┃ ┗ relatorios.css
┃ ┃ ┗ js/
┃ ┃ ┗ script.js
┃ ┣ templates/
┃ ┃ ┣ cadastrar_produto.html
┃ ┃ ┣ listar_produtos.html
┃ ┃ ┣ movimentacoes.html
┃ ┃ ┣ navbar.html
┃ ┃ ┗ relatorios.html
┃ ┣ admin.py
┃ ┣ apps.py
┃ ┣ models.py
┃ ┣ views.py
┃ ┣ tests.py
┃ ┗ init.py
┣ estoque_project/
┃ ┣ settings.py
┃ ┣ urls.py
┃ ┣ wsgi.py
┃ ┣ asgi.py
┃ ┗ init.py
┣ db.sqlite3
┣ manage.py
┣ requirements.txt
┗ package-lock.json
```

---

## ⚙️ Modelos

### Produto
- `nome`: CharField
- `quantidade`: PositiveIntegerField
- `preco`: DecimalField

### Movimentacao
- `produto`: ForeignKey para Produto
- `tipo`: Entrada ou Saída
- `quantidade`: Integer
- `data`: DateTimeField automático

---

## 🏃 Como Executar

1. Clone o repositório:
   
```
git clone https://github.com/EricIkeda1/Projeto_Estoque.git
cd Projeto_Estoque
```

2. Crie e ative o ambiente virtual 
```
python -m venv venv
```

3. Ativar o ambiente virtual (Se for no Windows utilizar cmd)

Linux / Mac
```
source venv/bin/activate
```

Windows
```
venv\Scripts\activate
```

2. Instale as dependências
   
```
pip install -r requirements.txt
```

3. Execute as migrações
```
python manage.py migrate
```

4. Inicie o servidor
```
python manage.py runserver
```

5. Acesse no navegador
```
http://127.0.0.1:8000/
```

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).