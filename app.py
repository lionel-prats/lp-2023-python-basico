import connection # conexion a la DB 
#from connection import connection # forma B de importar el archivo

#with connection.cursor() as cursor: # forma B de utilizar la conexion a la DB
with connection.connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT * FROM usd"

    cursor.execute(sql)
    # result = cursor.fetchone()
    result = cursor.fetchall()
    print(result)