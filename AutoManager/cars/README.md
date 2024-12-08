# Proyecto de Gestión de Autos con Django 🚗

Este proyecto implementa un sistema para gestionar **autos**, **clientes**, **marcas** y **ventas** usando **Django** y **Django Rest Framework (DRF)**. Permite realizar operaciones CRUD y ofrece una API RESTful para manejar los recursos de manera eficiente.

---

## 🛠 Características

- **Aplicación de Django** con modelos para:
  - `Marca`
  - `Auto`
  - `Cliente`
  - `Venta`
  
- **Validaciones personalizadas**:
  - El `año` del auto no puede ser anterior a 1886 (primer auto).
  - Un auto no puede ser vendido más de una vez.

- **Interfaz de administración** personalizada con:
  - Filtros para visualizar autos por marca, año, etc.
  - Búsqueda por nombre de cliente y modelo de auto.

- **APIs RESTful** creadas con **Django Rest Framework**:
  - Endpoints para gestionar autos, marcas, clientes y ventas.
  - API personalizada para listar los autos disponibles.

---

## ⚙ Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local.

### 1. Clonar el repositorio

Clona el repositorio en tu máquina:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```
 
### 2. Crear y activar un entorno virtual
```bash
python -m venv venv
linux: source venv/bin/activate  
Windows: venv\Scripts\activate

```
 ### 3. Instalar las dependencias
```bash
pip install -r requirements.txt


```
  ### 4. Realizar migraciones
```bash
python manage.py migrate
```

  ### 5. Ejecutar el servidor
```bash
python manage.py runserver

```

