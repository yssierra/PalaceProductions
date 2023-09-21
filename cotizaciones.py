from flask import Flask
from flask import redirect,url_for,render_template,request, flash #Run pip install flask-blueprint
from flask import Blueprint
blueprint = Blueprint('blueprint',__name__)

from flask_mysqldb import MySQL
app = Flask(__name__)

#Coneccion BDD
app.config['MYSQL_HOST'] = 'localhost'      #Definimos el Host
app.config['MYSQL_USER'] = 'root'           #Definimos el el usuario
app.config['MYSQL_PASSWORD'] = ''           #Definimos la contraseña 
app.config['MYSQL_DB'] = 'palaceproductions'    #Definimos cual es la base de datos

mysql = MySQL(app)

# Configuracion

app.secret_key ="mysecretkey"


@app.route('/')
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM cotizaciones')
    data = cursor.fetchall()
    print(data)
    
    return render_template('index.html', cotizaciones = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        Fecha_Cotizacion = request.form['Fecha_Cotizacion']
        TipoEntidad = request.form['TipoEntidad']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        numero_documento = request.form['numero_documento']
        fecha_de_nacimiento = request.form['fecha_de_nacimiento']
        Ocupacion = request.form['Ocupacion']
        celular = request.form['celular']
        correo = request.form['correo']
        Servicios = request.form['Servicios']
        Presupuesto = request.form['Presupuesto']
        Detalles_Proyecto = request.form['Detalles_Proyecto']
        
    #Aqui definimos que se va a dirigir a add cotizacion si del metodo post se obtienen los siguientes datos
        print(Fecha_Cotizacion)
        print(TipoEntidad)
        print(nombres)
        print(apellidos)
        print(numero_documento)
        print(fecha_de_nacimiento)
        print(Ocupacion)
        print(celular)
        print(correo)
        print(Servicios)
        print(Presupuesto)
        print(Detalles_Proyecto)
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO cotizaciones (Fecha_Cotizacion, TipoEntidad, nombres,apellidos,numero_documento,fecha_de_nacimiento,Ocupacion,celular,correo,Servicios,Presupuesto,Detalles_Proyecto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (Fecha_Cotizacion, TipoEntidad, nombres,apellidos,numero_documento,fecha_de_nacimiento,Ocupacion,celular,correo,Servicios,Presupuesto,Detalles_Proyecto))
        mysql.connection.commit()
        flash('Contacto agregado satisfactoriamente')
        
        return redirect(url_for('Index'))
    
    
@app.route('/edit/<id_Cotizaciones>')
def edit_contact(id_Cotizaciones ):
    cursor = mysql.connection.cursor()
    cursor.execute ('SELECT * FROM cotizaciones WHERE id_Cotizaciones = %s',[id_Cotizaciones])
    data = cursor.fetchall()
    
    return render_template('edit_contact.html', cotizacion = data[0])
    
    
@app.route('/update/<id_Cotizaciones>',methods=['POST'])
def update_cotizacion(id_Cotizaciones):
    if request.method == 'POST':
        Fecha_Cotizacion = request.form['Fecha_Cotizacion']
        TipoEntidad = request.form['TipoEntidad']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        numero_documento = request.form['numero_documento']
        fecha_de_nacimiento = request.form['fecha_de_nacimiento']
        Ocupacion = request.form['Ocupacion']
        celular = request.form['celular']
        correo = request.form['correo']
        Servicios = request.form['Servicios']
        Presupuesto = request.form['Presupuesto']
        Detalles_Proyecto = request.form['Detalles_Proyecto']
        cursor = mysql.connection.cursor()
        cursor.execute('''
        UPDATE cotizaciones SET Fecha_Cotizacion = %s,
        TipoEntidad = %s,
        nombres = %s,
        apellidos = %s,
        numero_documento = %s,
        fecha_de_nacimiento = %s,
        Ocupacion = %s,
        celular = %s,
        correo = %s,  # Agrega una coma después de celular
        Servicios = %s,
        Presupuesto = %s,
        Detalles_Proyecto = %s
        WHERE id_Cotizaciones = %s
        ''', (Fecha_Cotizacion, TipoEntidad, nombres, apellidos, numero_documento, fecha_de_nacimiento, Ocupacion, celular, correo, Servicios, Presupuesto, Detalles_Proyecto, id_Cotizaciones))

        mysql.connection.commit()
        
        flash('Contacto actualzado satisfactoriamente')
        return redirect(url_for('Index'))
    
  
@app.route('/delete/<string:id_Cotizaciones>')
def delete_contact(id_Cotizaciones):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM cotizaciones WHERE id_Cotizaciones = {0}'.format(id_Cotizaciones))
    mysql.connection.commit()
    flash('Contacto removido satisfactoriamente')
    return redirect(url_for('Index'))
    

    
    
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=3000,debug=True)