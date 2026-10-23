import os
from flask import Flask
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', ''),
        database=os.environ.get('DB_NAME', 'holamundo_db')
    )

@app.route('/')
def hello_world():
    status = ""
    try:
        conn = get_db_connection()
        conn.ping(reconnect=True)
        status = "¡Conectado exitosamente a la base de datos MySQL!"
        conn.close()
    except Exception as e:
        status = f"Error al conectar a la base de datos: {str(e)}"

    return f"<h1>Hola Mundo</h1><p>{status}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
