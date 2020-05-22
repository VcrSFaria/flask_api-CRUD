## CRUD com flask usando:

- flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy

## como rodar o projeto

'''sh
export FLASK_APP=app \
export FLASK_ENV=Development \
export FLASK_DEBUG=True

flask run
'''

## Como fazer as migracoes

'''sh
flask db init \
flask db migrate \
flask db upgrade 
'''