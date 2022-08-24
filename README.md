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

Ahora tenemos que darle permiso a Termux para acceder al almacenamiento, así cuando levantemos el servidor FTP podremos acceder a nuestros directorios.

Vamos a ajustes y entramos en aplicaciones, buscamos Termux, entramos en permisos, y permitimos el acceso a almacenamiento.

## Configuraciones y despliegue del servidor FTP

Lo siguiente que haremos será entrar a la aplicación Termux
