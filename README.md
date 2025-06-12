
# Aplicación del algoritmo PageRank

El algoritmo PageRank se utiliza para medir la importancia relativa de cada nodo en un grafo dirigido. Para implementarlo, necesitamos construir un grafo donde los nodos representan entidades (sucursales, conductores, clientes) y las aristas representan las relaciones entre ellas (en este caso, las encomiendas que pasan de una sucursal a un conductor y luego de un conductor a un cliente).

## Datos utilizados para construir el grafo (PageRank)
Los datos provienen de la tabla encomienda en la base de datos `transporte_entre_rios`. Los campos relevantes son:

| id_encomienda | id_sucursal_origen | id_conductor | id_remitente | id_consignatario |
|---------------|--------------------|--------------|--------------|------------------|
| 1             | 1                  | 3            | 7            | 8                |
| 2             | 2                  | 4            | 8            | 7                |
| 3             | 1                  | 5            | 9            | 10               |

**Descripción de los campos:**
- `id_sucursal_origen`: Sucursal de donde sale la encomienda.
- `id_conductor`: Conductor que transporta la encomienda.
- `id_remitente` y `id_consignatario`: Son los clientes que envían y reciben la encomienda.

## Construcción del Grafo
- **Nodos**: Los nodos del grafo son sucursales, conductores y clientes.
- **Aristas**: Las aristas representan las relaciones entre estos nodos:
  - **Sucursal → Conductor**: Una sucursal envía una encomienda a un conductor.
  - **Conductor → Cliente (Remitente y Consignatario)**: El conductor entrega la encomienda al remitente y consignatario.

## Cómo se aplica PageRank
1. **Inicialización del grafo**: Usamos las relaciones de la tabla encomienda para crear un grafo dirigido.
2. **Cálculo de PageRank**: El algoritmo PageRank asigna un valor de importancia a cada nodo, basado en la cantidad y calidad de los nodos que apuntan hacia él.

## Ejemplo
La fila `(1, 3, 7, 8)` indica que:
- **Sucursal 1** envía una encomienda a **Conductor 3**.
- **Conductor 3** entrega esa encomienda a **Cliente 7** (Remitente) y **Cliente 8** (Consignatario).

Esto crea las siguientes aristas:
- Sucursal 1 → Conductor 3
- Conductor 3 → Cliente 7
- Conductor 3 → Cliente 8

El valor de PageRank se calcula utilizando el parámetro `alpha=0.85` como factor de amortiguamiento.

## Resultados de PageRank

| Nodo | PageRank |
|------|----------|
| Nodo 1 | 0.05876045920297074 |
| Nodo 3 | 0.09621982112985815 |
| Nodo 7 | 0.14581799617935495 |
| Nodo 8 | 0.11855534458946687 |
| Nodo 2 | 0.05876045920297074 |
| Nodo 4 | 0.08760450413253272 |
| Nodo 9 | 0.1294604052254221 |
| Nodo 10 | 0.12099668507503306 |

### Interpretación:
- Los nodos con valores más altos de PageRank son considerados más importantes en el sistema.
- El **Nodo 7** tiene el PageRank más alto, lo que indica que este nodo tiene muchas conexiones hacia otros nodos importantes.

## Aplicación de MapReduce (Cálculo de tarifas por sucursal)

**MapReduce** es un modelo de programación utilizado para procesar y analizar grandes volúmenes de datos de forma distribuida. En este caso, utilizamos MapReduce para calcular el total de tarifas por sucursal.

### Datos utilizados para MapReduce
Utilizamos los datos de la tabla encomienda, específicamente los campos `tarifa` y `id_sucursal_origen`, para calcular el total de tarifas por cada sucursal.

### Proceso de MapReduce
1. **Map**: Extraemos las tarifas y las agrupamos por `id_sucursal_origen` (sucursal de origen de la encomienda).

```python
def map_reduce(data):
    mapped_data = []
    for row in data:
        id_sucursal_origen = row[7]  # id_sucursal_origen
        tarifa = float(row[12])  # tarifa
        mapped_data.append((id_sucursal_origen, tarifa))
    return mapped_data
```

2. **Reduce**: Sumamos las tarifas por cada sucursal.

```python
from collections import defaultdict

def reduce(mapped_data):
    reduced_data = defaultdict(float)
    for sucursal, tarifa in mapped_data:
        reduced_data[sucursal] += tarifa
    return reduced_data
```

### Resultados de MapReduce
El resultado es el total de tarifas por sucursal:

| Sucursal | Total de tarifa |
|----------|-----------------|
| Sucursal 2 | 165.0 |
| Sucursal 3 | 185.0 |
| Sucursal 1 | 175.0 |

### Interpretación:
- **Sucursal 1** tiene un total de 175.0 en tarifas de encomiendas.
- **Sucursal 2** tiene un total de 165.0 en tarifas.
- **Sucursal 3** tiene un total de 185.0 en tarifas.
