# Sistema De Gestion De Biblioteca 📚
Este proyecto es parte de *reto tecnico* propuesto, consiste en la elaboracion de un *microservicio* el cual estara encargado de la gestion de los libros de una biblioteca a travez de los distintos *endpoints* inmersos en el microservicio, que a su vez permitiran realizar operaciones *CRUD* tipicas de una *API REST*.

Con la estructura propuesta se plantea separa la parte de los datos, endpoints y logica del sevicio con la finalidad de tener una aplicacion escalable y que pueda ser incorporada con otros microservicios como los referentes a seguridad y autenticacion, usuarios, pedidos o cualquier otro microservicio que pueda contribuir a una aplicacion de microservicios compleja.

## Construido con 🛠️
Para la elaboracion de este proyecto se usaron las siguientes tecnologias:
* [FastAPI](https://fastapi.tiangolo.com/) - Framework web.
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM.
* [PYPI](https://pypi.org/) - Repositorio de dependencias.
* [PostgreSQL](https://www.postgresql.org/) - Base de datos Relacional.
* [Docker](https://www.docker.com/) - Empaquetador de software.
* [Docker Hub](https://hub.docker.com/) - Biblioteca de imagenes docker.
* [Git](https://git-scm.com/doc) - Sistema de control de versiones.
<br>

## Instalacion 🔧
Pasos pertinentes para la correcta instalacion del proyecto y dependencias en un equipo local.

### Requisitos 📋
Para la correcta intalacion del proyecto es necesario contar con lo siguiente instalado en tu quipo local.
* **python >= 3.6** (se recomienda versiones superiores o mas recientes)
* **pip** (gestor de dependencias de python, biene instalado por defecto a partir de python >= 3.10)
* **Docker**
* **Docker Desktop** (opcional)
* **Git**

Si no tiene las herramientas puedes instalarlas aqui 👇
* [Pagina oficial python](https://www.python.org/)
* [Instalar pip en linux](https://geekland.eu/como-instalar-y-usar-el-gestor-de-paquetes-pip/#:~:text=Pip%20es%20un%20gestor%20de,sencilla%20en%20nuestro%20sistema%20Linux.)
* [Pagina oficial de Docker](https://www.docker.com/)
* [Descargar Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [Descargar Git](https://git-scm.com/downloads)

### Comenzando 🚀
Clona este repositorio en tu equipo local con ayuda de git.
Efectua el siguiente comando en tu terminar en el directorio donde desees que se almacene el proyecto
**Por SSH o si lo prefires por HTTPS**
``` bash
git clone git@github.com:JJavierHA/APIForo.git
```
``` bash
git clone https://github.com/JJavierHA/APIForo.git
```

>[!NOTE]
> Usa python o python3 en tu terminal dependiendo de tu sistema operativo

### Creacion de entorno virtual
Dentro del proyecto raiz abre una terminal y crea un entorno virtual y activalo con los siguientes comandos:
``` bash
python -m venv venv
```
``` bash
venv\Scripst\activate # Windows
```
``` bash
source venv/bin/activate # Linux
```
<br>

## Despliegue con Docker 🐳 
Para el despliegue de este proyecto se requiere de docker o docker Desktop segun sea el caso, con la finalidad de poner en marcha los contenedores y ver el correcto funcionamiento del proyecto.

El Proyecto cuenta con los siguietes documentos:
* **Dockerfile** Instrucciones de creacion para la imagen del proyecto.
* **docker-compose.yml** Instrucciones para el levnatamiento de la aplicacion en contenedores.

> [!IMPORTANT]
> * Si usas Docker Desktop asegurate de iniciar la maquina virtual.
> * Configura el archivo **.env.template** conforme a las instrucciones en su interior.

### Pasos para levantar el proyecto
Permitira construir la imagen y levantar los contenedores declarados en el archivo **docker-compose.yml** 
``` bash
docker compose up --build
```
> [!NOTE] 
> deberas ver los logs de los contenedores en tu terminal, lo cual es senial de que todo a salido bien.

Ejecuta el siguiente comando para ver los contenedores activos. Deberias ver los contenedores de la aplicacion en funcionamiento
``` bash
docker ps
```
Deverias ver algo similar, lo que indica que tus contenedores estan activos
| ... | STATUS  | PORT | NAMES      |
|-----|---------|------|----------|
|...| Up 46 seconds     | 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   | book_service-book_service-1  |
|...| Up 52 seconds (healthy) | 0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   | book_service-reto_tecnico-1   |

> [!WARNING]
> Si algo falla revisa la configuracion del archivo .env.template.
> Asegurate de no tener los puertos que usa la aplicacion ocupados.
<br>

## Despliegue del proyecto en equipo local 💻
Pasos para desplegar el proyecto desde un equipo local, para permitir mejoras o personalizacion de acuerdo a tus necesidades.

### Instalacion de dependencias del proyecto
Instala en tu entorno entorno virtual las dependencias para que el proyecto funcione correctamente.
``` bash
pip install -r requirements.txt
```

Ejecuta en tu terminal el siguiente comando para poner en marcha la aplicacion.
``` bash
uvicorn app.main:app  
```
o si deseas ver los cambios reflejados en el codigo
``` bash
uvicorn app.main:app --reload # evita reiniciar el proyecto
```

> [!WARNING]
> Asegurate de contar con una base de datos valida para este proyecto. Puedes configurar la nueva ruta de tu base de datos en el archivo .env.template de este proyecto
<br>

## Funcionamiento
El proyecto consiste en la gestion de libros de una biblioteca a travez de un **CRUD** basico.
* Direccion para la gestion de generos http://localhost:8000/api/catalogs/genre
* Direccion para la gestion de libros http://localhost:8000/api/books

> [!NOTE]
> Los metodos get de listado implementan paginacion para mejorar la visibilidad de los recursos
> Ejemplo: http://localhost:8000/api/catalogs/genre?page=1&size=5

> [!IMPORTANT]
> Asegurate de crear generos correctamente, para ser usados en la creacion de los libros 
<br>

## Documentacion
Para ver la documentacion de la API ingresa a la siguiente direccion: 
* Documentacion interactiva - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* Documentacion alternativa - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
<br>

## Elaborado por ️
**Javier Herrera** - *Trabajo Inicial* - [JJavierHA](https://github.com/JJavierHA)

Puedes descargar o ver la imagen del proyecto sin base de datos en mi repositorio de Docker Hub - [jjavierha](https://hub.docker.com/r/jjavierha/reto-backend)
