import json
from flask import Blueprint, current_app, request, jsonify
from .model import Book
from .serealizer import BookSchema


bp_books = Blueprint('book', __name__)


@bp_books.route('/mostar', methods=['GET'])
def mostrar():
    bs = BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result), 200



@bp_books.route('/deletar/<id>', methods=['GET'])
def delet(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')



@bp_books.route('/alterar/<id>', methods=['POST'])
def alterar(id):
    bs = BookSchema()
    query = Book.query.filter(Book.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())



@bp_books.route('/inserir', methods=['POST'])
def insert():
    bs = BookSchema()
    book = bs.load(request.json)
    escritor = book['escritor']
    livro = book['livro']
    books = Book(escritor=escritor, livro=livro)
    current_app.db.session.add(books)
    current_app.db.session.commit()
    bs.dump(books)
    return bs.jsonify(book), 201