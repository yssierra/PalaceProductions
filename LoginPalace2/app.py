from flask import Flask
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQLdb, MySQL
from flask import Flask, render_template


app = Flask(__name__, template_folder=('templates'), static_folder='static')

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='PalaceProductions'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql=MySQL(app)




@app.route('/')
def home():
    return render_template('home.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')
#FUNCION DE LOGIN

@app.route('/acceso-login', methods=["GET" , "POST"])



def login():
    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword' in request.form:
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']
            
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE correo = %s AND contrasena = %s', (_correo, _password,))
        account = cur.fetchone()  
        
        if account:
            session['logueado'] = True
            session['id'] = account['id_usuario']
            
            return render_template("admin.html")
        else:
            return render_template('home.html', mensaje = "USUARIO INCORRECTO")
#REGISTRO DE USUARIOS
@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/crear-registro', methods=["GET" , "POST"])
def crear_registro():
    nombre = request.form['txtNombre']
    apellido = request.form['txtApellido']
    tipoDocumento = request.form['txtTipoDoc']
    numeroDocumento = request.form['txtNumeroDocumento']
    correo = request.form['txtCorreo']
    celular = request.form['txtNumeroTelefono']
    fechaNacimiento = request.form['txtFechaNacimiento']
    password = request.form['txtPassword']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Usuarios (nombres, apellidos, tipo_documento, numero_documento, correo, celular, fecha_de_nacimiento , contrasena, id_rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,'2')",
                (nombre, apellido, tipoDocumento, numeroDocumento, correo, fechaNacimiento ,celular, password))
    mysql.connection.commit()
    
    return render_template("index.html" , mensaje2 = "usuario registrado exitosamente")
    
#------------------------------



if __name__ == '__main__':
    app.secret_key = "santiago_urrea"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded = True)