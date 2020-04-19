//Python Image

//*Crear Dockerfile + requiremenets dins una carpeta
	//Dins Docker file:
		/*FROM python:3

		WORKDIR /usr/src/app

		COPY requirements.txt ./
		RUN pip install --no-cache-dir -r requirements.txt

		COPY . .

		CMD [ "python", "./hello-world.py" ]
		*/
	//Dins Requirements.txt
		/*
		numpy
		pandas
		matplotlib
		*/

 CMD:docker build -t python-app .
 CMD:docker run -it --rm --name my-running-app python-app //rm = eliminar container al cerrarlo

 //Ejecutar python
$ docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp python-app python versions.py
