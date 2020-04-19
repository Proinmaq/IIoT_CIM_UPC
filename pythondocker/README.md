# Python en Docker

## Preparación
1. Descargar [Docker](https://docs.docker.com/docker-for-windows/install/) o Docker Toolbox

1. Crear dos archivos dentro de una carpeta

	* [Dockerfile](Dockerfile)
	
		Documento que describe los pasos a seguir para generar nuestra imagen Docker
		```cpp
		FROM python:3

		WORKDIR /usr/src/app

		COPY requirements.txt ./

		RUN pip install --no-cache-dir -r requirements.txt
		```
   	* [requirements.txt](requirements.txt)
	
		Documento que describe las Librerías Python Package ([pip](https://pypi.org/project/pip/)) que necesitaremos para después poder importarlas en nuestro proyecto `Python`, algunas podrían ser:

		```
		numpy
		pandas
		matplotlib
		seaborn
		paho-mqtt
		```

1. Generar la imagen `Docker`

	Este comando generará una imagen de Docker personalizada con `Python` y las librerías que hayamos puesto en el documento `requirements.txt`.
	```
	docker build -t yourimagename .
	```
	_Nota: Ejecutar el comando desde la ruta de la carpeta donde haya los dos ficheros anteriores_

## Ejecución

Para ejectuar un fichero `Python` con la nueva imagen generada en `Docker`, arrancaremos un contenedor de la siguiente manera.
```
docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp yourimagename python yourscript.py 
```
 * `--rm` elimina el contedor generado automáticamente al finalizar la ejecución
 * `-v` enlazar directorios
 * `$PWD` directorio actual
 * `-w` directorio dentro del contenedor
 
_Nota: Ejecutar el comando desde la ruta de la carpeta donde haya los dos ficheros anteriores_

## Ejemplos

 * [hello-world.py](Codigos/hello-world.py) - comprueba el correcto funcionamiento y la versión de `Python`
 * [versions.py](Codigos/versions.py) - visualizar las versiones de todas las librerias instaladas en la imagen `Docker`
 * [pythonmqtt.py](Codigos/pythonmqtt.py) - implementación simple de cliente mqtt
