# JRC

## Descripción
Proyecto de integración para JRC Cia Limitada. Este proyecto tiene como objetivo proporcionar una solución integrada para la gestión de la compañía utilizando tecnologías web modernas.

## Estructura del Proyecto
- **Carpetas:**
  - `.vscode`: Configuraciones del entorno de desarrollo.
  - `core`: Núcleo de la aplicación.
  - `mysite`: Configuración principal del sitio web.
  - `staticfiles`: Archivos estáticos como CSS, JavaScript e imágenes.

- **Archivos Importantes:**
  - `db.sqlite3`: Base de datos SQLite.
  - `manage.py`: Script de gestión de Django.

## Instalación
1. Clona el repositorio: `git clone https://github.com/isveloz/JRC.git`
2. Navega al directorio del proyecto: `cd JRC`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Ejecuta las migraciones: `python manage.py migrate`
5. Inicia el servidor: `python manage.py runserver`

## Uso
Accede a `http://127.0.0.1:8000/` en tu navegador para ver la aplicación en funcionamiento.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para contribuir a este proyecto.

## Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
