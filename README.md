# django_server

Mi primera aplicación con **Django**: un proyecto mínimo con una app `books` que devuelve una página HTML con una lista de libros.

## Tecnologías

- Python 3
- Django 5.2
- SQLite (base de datos por defecto de Django)

## Estructura

```
django_server/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── django_server/      # Configuración del proyecto (settings, urls, wsgi, asgi)
└── books/              # App de libros
    ├── views.py        # Vista find_all: genera una lista <ul> de libros
    └── urls.py         # Rutas de la app
```

## Rutas

| Ruta       | Descripción                                    |
|------------|------------------------------------------------|
| `/admin/`  | Panel de administración de Django              |
| `/books/`  | Lista de libros en HTML (vista de `books`)     |

## Instalación y ejecución

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Luego abre <http://127.0.0.1:8000/books/> en el navegador.

## Nota

En `books/urls.py` la ruta apunta a `views.findAll`, pero la función definida en `books/views.py` se llama `find_all`. Hay que usar el mismo nombre en ambos archivos para que el servidor arranque.
