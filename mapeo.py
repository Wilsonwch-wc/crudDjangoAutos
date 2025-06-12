import mysql.connector
from collections import defaultdict
from decimal import Decimal

# Conexión a la base de datos
def connect_to_database():
    connection = mysql.connector.connect(
        host='127.0.0.1',  
        user='root',       
        password='',  
        database='transporte_entre_rios'  
    )
    return connection

# Función de Mapeo: Emitir id_sucursal_origen y tarifa
def map_reduce(data):
    mapped_data = []
    for row in data:
        id_sucursal_origen = row[7]  # id_sucursal_origen está en la posición 7 de la fila
        tarifa = float(row[12]) 
        mapped_data.append((id_sucursal_origen, tarifa))
    return mapped_data

# Función de Reducción: Sumar tarifas por sucursal
def reduce(mapped_data):
    reduced_data = defaultdict(float)
    for sucursal, tarifa in mapped_data:
        reduced_data[sucursal] += tarifa  
        # Aquí ya estamos sumando flotantes
    return reduced_data


def main():

    connection = connect_to_database()
    cursor = connection.cursor()

    # Obtener los datos de la tabla encomienda
    cursor.execute("SELECT * FROM encomienda;")
    data = cursor.fetchall()  # Traer todos los datos

    # Mapeo: Emitir id_sucursal_origen y tarifa
    mapped_data = map_reduce(data)

    # Reducción: Sumar tarifas por sucursal
    reduced_data = reduce(mapped_data)

    # Mostrar resultados
    print("Total de tarifas por sucursal:")
    for sucursal, total_tarifa in reduced_data.items():
        print(f"Sucursal {sucursal}: Total de tarifa = {total_tarifa}")


    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
