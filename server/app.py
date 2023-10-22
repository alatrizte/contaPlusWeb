from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="pY4s%/dtRd",
    database="contaplus"
)
cursor = db.cursor()

# Crear tabla de usuarios
def create_user_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_mail VARCHAR(255) NOT NULL UNIQUE,
        user_name VARCHAR(255) NOT NULL,
        user_pass VARCHAR(255) NOT NULL,
        mail_confirm BOOLEAN NOT NULL DEFAULT false
    )
    """
    cursor.execute(create_table_query)
    db.commit()

create_user_table()

# Ruta para agregar un usuario
@app.route('/add_user', methods=['POST'])
def add_user():

    data = request.get_json()
    user_mail = data['user_mail']
    user_name = data['user_name']
    user_pass = data['user_pass']

    hashed_password = generate_password_hash(user_pass)

    insert_user_query = "INSERT INTO users (user_mail, user_name, user_pass) VALUES (%s, %s, %s)"
    values = (user_mail, user_name, hashed_password)
    cursor.execute(insert_user_query, values)
    db.commit()

    return jsonify({'message': 'Usuario creado con éxito'})

if __name__ == '__main__':
    app.run(debug=True)