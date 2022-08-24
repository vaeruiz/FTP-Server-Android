# FTP-Server-Android

Para montar nuestro servidor FTP en Android necesitamos lo siguiente:
- Terminal Termux instalado en nuestro dispositivo
- Instalar python en el terminal y el modulo pyftpdlib

## Instalar Termux

Termux es un terminal adaptado para Android con el que podremos hacer acciones parecidas a las de un terminal Ubuntu, para instalarlo vamos a la web [f-droid](https://f-droid.org/en/packages/com.termux/) 

![imagen1](/images/img1.PNG)

Y descargamos su APK

![imagen2](/images/img2.png)

Cuando se descargue, la instalamos en nuestro dispositivo Android

![imagen3](/images/img3.png)

## Configuracion de Termux

Para acceder a nuestros directorio al levantar el servidor FTP, tenemos que darle permiso a Termux para que acceda a nuestro almacenamiendo, para ello vamos a ajustes y entramos en aplicaciones, buscamos Termux, entramos en permisos, y permitimos el acceso a almacenamiento.

Lo siguiente que haremos será entrar a la terminal, al abrirlo por primera vez se harán unas configuraciones, cuando termine, nos encontraremos nuestra terminal lista para trabajar.

Lo primero que haremos será asegurarnos de que estamos en el directorio home de Termux, este directorio /data/data/com.termux/files/home, podemos ver en que directorio estamos actualmente ejecutando el comando ``pwd``, si no nos encontramos en dicho directorio, basta con ejecutar ``cd``, es importante que nos encontremos en esa ruta.

Lo siguiente es actualizar los repositorios de la terminal haciendo un update-upgrade, ejecutamos los comandos ``apt update`` y ``apt upgrade``

Cuando termine de actualizarse la terminal, instalamos Python ejecutando el comando ``pkg install python``.

Después instalamos el módulo pyftpdlib con el comando ``python -m pip install pyftpdlib``. Es posible que de un error, si se da el caso, instalamos la herramienta openssl-tool (``apt install openssl-tool``) y ejecutamos de nuevo el comando para instalar el módulo.

Con esto hecho, creamos un script de python como el que se encuentra en el repositorio [ftpserver.py](https://github.com/vaeruiz/FTP-Server-Android/blob/main/ftpserver.py) que levantará el servidor FTP cada vez que lo ejecutemos, en el archivo de este repositorio se explican algunas instrucciones del script con mayor peso.
