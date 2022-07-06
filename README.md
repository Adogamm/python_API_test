# Requests python-spring
## Funcionamiento general
Este programa fue diseñado en python y permite generar registros a la base de datos H2 dentro de un proyecto de Spring que funciona como API Rest, esta API recibe un conjunto de datos por medio de JSON para poder hacer los registros dentro de la tabla.

### Archivos txt
Para el funcionamiento de este aplicativo se requiere generar un archivo con extensión txt que contenga los siguientes valores

------------


	"Nombre del empleado"
	"Apellido"
	"Pais de recidencia"
	"Idioma"
	"Aeropuerto en donde realiza sus labores"

------------


Todo debe de ser colocado en un renglón separado por el caracter de coma ( , ) y al introducir el último dato hacer un salto de linea para poder realizar otro registro.

### Requisiciones
Se hace el envío de las requisiciones por el metodo POST, en el archivo **Request.py** se genera un request vía POST a la URL Asignada desde el proyecto de spring ademas de introducir el parametro JSON que es el contenido que se va a registrar en la base de datos.

###App.py
Por último. El archivo app.py hace una instancia del la clase que manipula los archivos, ya que en esta clase se abre el archivo y se hacen las operaciones para enviar la petición a la base de datos, todo esto en un esquema de POO que permite tener un código optimizado y lo más limpio y simple posible
