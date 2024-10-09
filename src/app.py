from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicacion

@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM Productos")
    myresult = cursor.fetchall()

    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    
    cursor.close()

    return render_template('index.html', data=insertObject)

#Ruta para guardar usuarios en la base de datos
@app.route('/Products', methods=['POST'])
def addProduct():
    Nombre = request.form['Nombre']
    Descripcion = request.form['Descripcion']
    Precio = request.form['Precio']
    Stock = request.form['Stock']
    EmpresaId = request.form['EmpresaId']

    if Nombre and Descripcion and Precio and Stock and EmpresaId:
        cursor = db.database.cursor()
        sql = "INSERT INTO Productos (Nombre, Descripcion, Precio, Stock, EmpresaId) VALUES (%s, %s, %s, %s, %s)"
        data = (Nombre, Descripcion, Precio, Stock, EmpresaId)
        cursor.execute(sql, data)
        db.database.commit()
        cursor.close()
    return redirect(url_for('home'))

@app.route('/delete/<string:RFID>')
def delete(RFID):
    cursor = db.database.cursor()
    sql = "DELETE FROM Productos WHERE RFID=%s"
    data = (RFID,)
    cursor.execute(sql, data)
    db.database.commit()
    cursor.close()
    return redirect(url_for('home'))

@app.route('/edit/<string:RFID>', methods=['POST'])
def edit(RFID):
    Nombre = request.form['Nombre']
    Descripcion = request.form['Descripcion']
    Precio = request.form['Precio']
    Stock = request.form['Stock']
    EmpresaId = request.form['EmpresaId']

    if Nombre and Descripcion and Precio and Stock and EmpresaId:
        cursor = db.database.cursor()
        sql = "UPDATE Productos SET Nombre = %s, Descripcion = %s, Precio = %s, Stock = %s, EmpresaId = %s WHERE RFID = %s"
        data = (Nombre, Descripcion, Precio, Stock, EmpresaId, RFID)
        cursor.execute(sql, data)
        db.database.commit()
        cursor.close()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True, port=4000)



