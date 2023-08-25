from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import datetime
import psycopg2
import bcrypt
import json
import jwt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
salt = bcrypt.gensalt()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    complete = db.Column(db.Boolean)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)

with app.app_context():
    db.create_all()

def generate_token(user):
    token = jwt.encode({'user.id': user.id}, 'key', algorithm='HS256')
    return token

def generate_password_hash(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

@app.route('/register')
def register():
    # Mostra a tela de registro
    return render_template('register.html')

@app.route('/loginpage')
def login():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def login_post():
    try:
        email = request.form['email']
        password = request.form['password']
        
        # Verifica se o usuário existe no banco de dados
        user = User.query.filter_by(email=email).first()

        if user:
            print(User.query.filter_by(email=email).one().password)
            result = bcrypt.checkpw(password.encode('utf-8'), User.query.filter_by(email=email).one().password.encode('utf-8'))
            print(User.query.filter_by(email=email).one().password.encode('utf-8'))
            if result:
                try:
                    token = generate_token(user)
                    response = make_response(jsonify({'url': url_for('todo')}))
                    response.set_cookie('userID', str(user.id), secure=True)
                    response.set_cookie('token', token, secure=True)
                    return redirect(url_for(f'todo'))
                except Exception as e:
                    return jsonify({'error': str(e)}), 500
            else:
                return "Senha incorreta", 401
        else:
            return "Usuário não encontrado", 401
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/add_user', methods=["POST"])
def add_user():
    # Adiciona os dados do usuário ao banco de dados
    email = request.form['email']
    password = request.form['password']

    # Criptografa a senha do usuário
    password_hash = generate_password_hash(password)

    new_user = User(email=email, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return render_template('login.html')

@app.route('/todo')
def todo():
    # Mostra todos os itens
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('todo.html', todo_list=todo_list)

@app.route('/add', methods=["POST"])
def add():
    # Adiciona um novo item
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('todo'))

@app.route('/update/<int:todo_id>', methods=["POST"])
def update(todo_id):
    # Altera o status de um item
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('todo'))

@app.route('/delete/<int:todo_id>', methods=["POST"])
def delete(todo_id):
    # Deleta um item
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo'))

if __name__ == "__main__":

    app.run(debug=True)