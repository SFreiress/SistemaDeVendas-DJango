# Sistema de Vendas - DJango

## Como instalar
## Comandos
- python –m venv venv
- .\venv\Scripts\activate
- python -m pip install --upgade
- pip install django
- pip install mysqlclient
- python manage.py migrate
- python manage.py runserver 
- python manage.py runserver
- python manage.py makemigrations

## Padrões de Commit
### feat: adição de função
_`feat: função de validação de cartão`_

- python manage.py makemigrations
_`feat: tela de home`_

### fix: correção de algum erro
_`fix: processo de validação de CVV`_

### docs: ({documento}) adição em documentos
_`docs: (readme) padrões de commit`_

### style: mudanças que não impactam funcionamento
_`style: nomenclatura`_

### refactor: não corrige bug nem adiciona função
_`refactor: função de cadastro de clientes`_

### test: "{teste}"
_`test: "Deve retornar ClientModel quando 200"`_

### test: {item} para "{teste}"
_`test: mock para "Deve retornar ClientModel quando 200"`_

### chore: mudança em build ou bibliotecas
_`chore: novas bibliotecas`_

_`chore: ajuste docker`_

## Padrão de nomenclatura
### HTML:
class: `dashed-case`

id: `camelCase`

### JavaScript
var, let: `camelCase`

### Django
modelos: `CamelCasePascal`

views, funções: `snake_case`
