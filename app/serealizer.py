from flask_marshmallow import Marshmallow
from .model import Book


ma = Marshmallow()



def configure(app):
    ma.init_app(app)



class BookSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Book

    id = ma.auto_field()
    escritor = ma.auto_field()
    livro = ma.auto_field()