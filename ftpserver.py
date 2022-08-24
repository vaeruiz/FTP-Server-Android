import os, socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Puerto de servidor
FTP_PORT = 8021

# Directorio a mostrar
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

# Permiso de solo lectura a usuario anonimo
#authorizer.add_anonymous(FTP_DIRECTORY, perm='elr')

# Permiso de lectura y escritura a usuario anonimo
authorizer.add_anonymous(FTP_DIRECTORY, perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = 'Termux FTP Server :D'
handler.passive_ports = range(50000, 55535)

address = ('', FTP_PORT)
server = FTPServer(address, handler)

server.max_cons = 256
server.max_cons_per_ip = 5

server.serve_forever()
