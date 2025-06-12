import mysql.connector
import networkx as nx
from decimal import Decimal

# Conexión a la base de datos
def connect_to_database():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',  # Reemplaza con tu contraseña
        database='transporte_entre_rios'
    )
    return connection

# Función para construir el grafo
def build_graph():
    # Conectar a la base de datos
    connection = connect_to_database()
    cursor = connection.cursor()

    # Obtener los datos de la tabla encomienda
    cursor.execute("""
        SELECT e.id_sucursal_origen, e.id_conductor, e.id_remitente, e.id_consignatario
        FROM encomienda e
    """)
    data = cursor.fetchall()  # Traer todos los datos

    # Crear un grafo dirigido
    G = nx.DiGraph()

    # Añadir aristas al grafo, donde los nodos son las sucursales, conductores y clientes
    for row in data:
        id_sucursal_origen = row[0]
        id_conductor = row[1]
        id_remitente = row[2]
        id_consignatario = row[3]

        # Añadir aristas (sucursal -> conductor, conductor -> cliente, etc.)
        G.add_edge(id_sucursal_origen, id_conductor)
        G.add_edge(id_conductor, id_remitente)
        G.add_edge(id_conductor, id_consignatario)

    # Cerrar la conexión
    cursor.close()
    connection.close()

    return G

# Construir el grafo
G = build_graph()

# Calcular el PageRank en el grafo
pagerank = nx.pagerank(G, alpha=0.85)

# Mostrar el PageRank de cada nodo
print("Ranking de Páginas (Nodos):")
for node, rank in pagerank.items():
    print(f"Nodo {node}: {rank}")
