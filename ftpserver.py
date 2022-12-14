import os, socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Puerto del servidor
FTP_PORT = 8021

# Variables para usuario
FTP_USER = 'user'
FTP_PASSWORD = 'password'

# Directorio a mostrar, de forma predeterminada muestra todo el almacenamiento del dispositivo
FTP_DIRECTORY = '/storage/emulated/0'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()

# Mensajes para conexion
print(f'DIRECCION: ftp://{IP}:{FTP_PORT}')
print(f'DIRECTORIO RAIZ: {FTP_DIRECTORY}')
print(f'Pulsa CTRL+C para salir \n')

authorizer = DummyAuthorizer()

# Permiso de lectura y escritura a usuario anonimo
authorizer.add_anonymous(FTP_DIRECTORY, perm='elr')
authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "pyftpdlib based ftpd ready."
#handler.masquerade_address = '151.25.42.11'
#handler.passive_ports = range(50000, 55535)

address = ('', FTP_PORT)
server = FTPServer(address, handler)

server.max_cons = 256
server.max_cons_per_ip = 5

server.serve_forever()
