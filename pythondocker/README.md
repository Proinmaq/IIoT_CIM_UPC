# Python en Docker
1. Descargar [Docker](https://docs.docker.com/docker-for-windows/install/) o Docker Toolbox

2. Crear dos archivos dentro de una carpeta:

   * [Dockerfile](Dockerfile): Dentro de este archivo añadiremos lo siguiente:

```cpp
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
```

2.	* [requirements.txt](requirements.txt):
Dentro de este archivo añadiremos los PythonPackage( [PIP](https://pypi.org/project/pip/)) que necesataremos para después importar las librerias en nuestro proyecto, por ejemplo algunas podrian ser:

```cpp
numpy
pandas
matplotlib
seaborn
paho-mqtt
```

3. En la consola de comandos de DockerToolbox:

	* Dentro de la ruta de la carpeta donde haya los dos ficheros anteriores:

```cpp
docker build -t yourimagename .
```
Este comando generarà una imagen de Docker personalizada con Python y las librerias que hayamos puesto en el documento _requirements.txt_. 
Una vez creada la imagen tendremos que arrancar un contenedor con ella y el script que queramos.

3. 	* Dentro de la ruta de la carpeta de nuestro codigo o aplicación:

```cpp
docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp yourimagename python yourscript.py 
```
	* rm = eliminar container al cerrarlo
	* w = Directorio dentro del contenedor
	* $PWD = Directorio actual
	* v = Para enlazar directorios


4. Dentro de la carpeta [Codigos](Codigos) hay 3 codigos:
	* [hello-world.py](Codigos/hello-world.py): Codigo simple para comprobar su correcto funcionamiento y la versión de Python.
	* [versions.py](Codigos/versions.py): Para ver las versiones de todas las librerias dentro de requirements.txt
	* [pythonmqtt.py](Codigos/pythonmqtt.py): Codigo ejemplo simple de cliente mqtt
