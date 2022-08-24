# FTP-Server-Android

Para montar nuestro servidor FTP en Android necesitamos lo siguiente:
- **Terminal Termux instalado en nuestro dispositivo**
- **Instalar python en el terminal y el modulo pyftpdlib**

## Instalar Termux

Termux es un terminal adaptado para Android con el que podremos hacer acciones parecidas a las de un terminal Ubuntu, para instalarlo vamos a la web [f-droid](https://f-droid.org/en/packages/com.termux/) 

![imagen1](/images/img1.png)

Y descargamos su APK

![imagen2](/images/img2.png)

Cuando se descargue, lo instalamos en nuestro dispositivo Android

![imagen3](/images/img3.png)

## Configuracion de Termux

Para acceder a nuestros directorio al levantar el servidor FTP, tenemos que darle permiso a Termux para que acceda a nuestro almacenamiendo, para ello vamos a ajustes y entramos en aplicaciones, buscamos Termux, entramos en permisos, y permitimos el acceso al almacenamiento.

![imagen4](/images/img4.png)

Lo siguiente que haremos será entrar a la terminal, al abrirlo por primera vez se harán unas configuraciones, cuando termine, nos encontraremos nuestra terminal lista para trabajar.

![imagen8](/images/img8.png)

Lo primero que haremos será asegurarnos de que estamos en el directorio home de Termux, este directorio /data/data/com.termux/files/home, podemos ver en que directorio estamos actualmente ejecutando el comando ``pwd``, si no nos encontramos en dicho directorio, basta con ejecutar ``cd``, es importante que nos encontremos en esa ruta.

Lo siguiente es actualizar los repositorios de la terminal haciendo un update-upgrade, ejecutamos los comandos ``apt update`` y ``apt upgrade``

Cuando termine de actualizarse la terminal, instalamos Python ejecutando el comando ``pkg install python``.

Después instalamos el módulo pyftpdlib con el comando ``python -m pip install pyftpdlib``. Es posible que de un error, si se da el caso, instalamos la herramienta openssl-tool (``apt install openssl-tool``) y ejecutamos de nuevo el comando para instalar el módulo.

## Script y configuracion del servidor

Al terminar de configurar Termux, creamos un script de python como el que se encuentra en el repositorio llamado [ftpserver.py](https://github.com/vaeruiz/FTP-Server-Android/blob/main/ftpserver.py) que levantará el servidor cada vez que lo ejecutemos, en el script de este repositorio se explican de forma breve algunas instrucciones que tienen mayor peso.

## Creacion de usuarios y permisos

Es posible crear varios usuarios y asignarles diferentes permisos, estes tipo de configuracion se tiene que hacer debajo de la clase ``authorizer = DummyAuthorizer()``, podemos crear dos tipos de usuarios:

- **Usuario anonimo.** Con el que podremos conectarnos al servidor sin necesidad de iniciar sesion, lo declaramos con la instruccion ``authorizer.add_anonymous``.
- **Usuario personal.** Tendremos que iniciar sesion para acceder al servidor, se declara con ``authorizer.add_user``.

De la misma forma, podemos asignar dos tipos de permisos:

- **Permisos de lectura.** ``perm='elr``
- **Permisos de lectura y escritura.** Estos incluyen un control total del almacenamiento, ``perm='elradfmw'``

Además, hay que indicar a que directorio tienen acceso los usuarios, tomando ejemplo del [script](https://github.com/vaeruiz/FTP-Server-Android/blob/main/ftpserver.py), podemos crear un usuario anonimo de solo lectura con la instruccion:

``authorizer = DummyAuthorizer()``

``authorizer.add_anonymous(FTP_DIRECTORY, perm='elr')``

De una manera parecida, podemos crear un usuario propio que tenga permisos de lectura y escritura:

``authorizer = DummyAuthorizer()``

``authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')``

En este caso, para el nombre de usuario, contraseña, y directorio de acceso se han hecho uso de las variables FTP_USER, FTP_PASSWORD y FTP_DIRECTORY, pero se pueden sustituir y configurar tantos usuarios como sean necesarios.

## Levantar el servidor y conectarse

Después de todo esto solo queda levantar el servidor, para hacerlo ejecutamos el comando ``python ftpserver.py``, si queremos levantarlo en segundo plano añadimos un " &" al final del comando, si no hay errores, se verá un mensaje como el siguiente:

![imagen9](/images/img9.png)

Para conectarnos a el, podemos utilizar un cliente ftp como por ejemplo [Filezilla](https://filezilla-project.org), indicamos la direccion IP que ha tomado el servidor, e iniciamos sesion si es necesario, hecho esto, veremos la lista de directorios que hemos configurado.

![imagen10](/images/img10.png)

## Documentación oficial

Para ver toda la información disponible acerca de pyftpdlib puedes visitar su sitio [web](https://pyftpdlib.readthedocs.io) oficial
