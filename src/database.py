import mysql.connector 

database = mysql.connector.connect(
    host='localhost',  # Cambia 'localhost' si usas otro servidor
    port=3306,  # Este es el puerto correcto para MySQL
    user='root',
    password='253545',  # Las contraseñas deben ir entre comillas
    database='logistica_rastrack'     
)
