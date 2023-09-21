from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src' , 'templates')

app = Flask(__name__, template_folder = template_dir)


#RUTAS DE LA APLICACION
@app.route('/')
def home():     # sourcery skip: list-comprehension, move-assign-in-block
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    myresult = cursor.fetchall()
    #CONVERTIR LOS DATOS A DICCIONARIO
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()

    return render_template('index.html', data = insertObject)
#RUTA PARA GUARDAR USUARIOS EN LA BASE DE DATOS
@app.route('/user', methods = ['POST'])
def addUser():    # sourcery skip: avoid-builtin-shadow
   
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    tipo_documento = request.form['tipo_documento']
    numero_documento = request.form['numero_documento']
    fecha_nacimiento = request.form['fecha_nacimiento']
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    celular = request.form['celular']
    if  nombres and apellidos and correo:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuarios (id_usuario,nombres, apellidos,tipo_documento,numero_documento,fecha_de_nacimiento,correo,contrasena,celular) VALUES ('', %s, %s, %s, %s,%s ,%s ,%s ,%s )"
        data = (nombres, apellidos, tipo_documento,numero_documento,fecha_nacimiento,correo,contrasena,celular)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM usuarios WHERE id_usuario = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))
@app.route('/edit/<string:id>', methods = ['POST'])
def edit(id):
    id = request.form['id_usuario']
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    tipo_documento = request.form['tipo_documento']
    numero_documento = request.form['numero_documento']
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    
    
    if  id and nombres and apellidos and correo:
        cursor = db.database.cursor()
        sql = "UPDATE usuarios SET nombres=%s, apellidos=%s, tipo_documento=%s,numero_documento=%s,correo=%s,contrasena=%s WHERE id_usuario = %s"
        data = (nombres, apellidos,tipo_documento,numero_documento, correo,contrasena,id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

    

   

if __name__ == '__main__':
     app.run(debug = True, port=4000)