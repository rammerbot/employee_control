##### Español:
### Sistema de control de empleados
<div align="center">
<img src="https://github.com/rammerbot/files/blob/main/Captura%20de%20pantalla%202024-05-26%20195124.png?raw=true" align="center" style="width: 100%" />
</div>  
  

### <div align="center">Sistema para el control de empleados de la empresa</div>  
  #### Descripcion.
  
> Es un sistema de control de empleados, tanto para el control de informacion como el control de acceso y asistencia, informacion de identificacion dentro de la empresa, control de entrega de dotaciones, amonestaciones y contribuciones de empleados de manera individual, cargo y sucursal.

#### Características
- Registro de empleado.
- Generacion de codigo de empleado.
- Carga de aportes del empleado a la empresa.
- Carga de amonestaciones.
- Ficha tecnica del empleado.
- Registro de entrada y salida del empleado.
- Registro de hora de almuerzo.
- Panel administrativo.
- Cuenta de administrador.

#### Instalación

##### Crear entorno virtual:
```
python -m venv employee_control
```

##### Entrar en el entorno
```
cd employee_control
```
##### Activar el entorno dependiendo del sistema operativo
>  windows:
```
cd employee_control/Script
```
```
activate
```
> en Lunix:
```
source employee_control/bin/activate
```

##### Clonar el repositorio:

```
git clone https://github.com/rammerbot/employee_control.git
```

> Navegar al directorio del proyecto:

```
cd employee_control
```

##### Instalar las dependencias requeridas:

```
pip install -r requirements.txt
```

#### Uso
##### Crear base de dato y configurar la conexion
> luego ejecutar las migraciones
```
python manage.py makemigrations
```
```
python manage.py migrate
```

> Ejecutar la aplicación:

```
python manage.py runserver
```

##### Acceder al sistema a través de la URL proporcionada.

> Crear una cuenta de Administrador

```
python manage.py createsuperuser
```

##### Iniciar sesión con tu cuenta administrativa.
##### Usar la interfaz para cargar, evaluar y generar reportes y balances.

#### Contribuciones
##### Haz un fork del repositorio.

>Crea tu rama de funcionalidad:
  > Copiar código
```
git checkout -b feature/tu-funcionalidad
```
> Realiza tus cambios:

> Copiar código
```
git commit -m 'Agrega alguna funcionalidad'
```

> Sube tus cambios:

> Copiar código
```
git push origin feature/tu-funcionalidad
```
> Abre un pull request.
### Licencia
<p>Este proyecto está licenciado bajo la Licencia MIT. RammerBot</p>


### English:

## Control management system
<div align="center">
<img src="https://github.com/rammerbot/files/blob/main/Captura%20de%20pantalla%202024-05-26%20195124.png?raw=true" align="center" style="width: 100%" />
</div>  
<div align="center">Control management system</div>

 ### Description
 
 > A system designed for managing employees' information, access control. It includes employee identification withim the company, management equipment distribution, reprimands and individual contributions. information about position and branch.

#### Features

- Employee registration.
- Generation of employee codes.
- Uploading employee contribution to the company.
- Uploading reprimands.
- Employee technical sheet.
- Employee recording check-in and check-out.
- Recording lunch out.
- Administrative panel.
- Administrator account.
  
#### Installation
#### Create a virtual environment:

```
python -m venv employee_control
```

#### Enter the environment
```
cd employee_control
```
#### Activate the environment depending on the operating system:

> Windows:

```
cd employee_control/Scripts
```
```
activate
```
> Linux:
```
source employee_control/bin/activate
```

Clone the repository:
```
git clone https://github.com/rammerbot/employee_control.git
```

> Navigate to the project directory:

```
cd employee_control
```

#### Install the required dependencies:
```
pip install -r requirements.txt
```

#### Usage
#### Create a database and configure the connection

> Then run the migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```

#### Run the application:

```
python manage.py runserver
```

#### Access the system through the provided URL.
 > Create an admin account:

```
python manage.py createsuperuser
```

#### Log in with your administrative account.
#### Use the interface to upload, evaluate, and generate reports and balances.
#### Contributions
> Fork the repository.
> Create your feature branch:

```
git checkout -b feature/your-feature
```

#### Commit your changes:

```
git commit -m 'Add some feature'
```

#### Push to the branch:
```
git push origin feature/your-feature
```

#### Open a pull request.

#### License
<p>This project is licensed under the MIT License. RammerBot</p>
