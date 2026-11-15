import mysql.connector

conexion=None
cursor=None

try:
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_estudiantes'
    )
    cursor=conexion.cursor(buffered=True)

except Exception as error:
    print(f"... ¡Por el momento no es posible conectarse a la Base de Datos intentelo mas tarde! ... ")
    print(f"Detalle del error: {error}")