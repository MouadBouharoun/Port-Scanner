import sys
import socket
from datetime import datetime
#hostname to ipv4
if len(sys.argv)==2:
    target=socket.gethostbyname(sys.argv[1])
else:
    print("invalid arguments")
    sys.exit()

#adding a port scanner        
print('*'*50)
print('scanning target : '+target)
print('time started : '+str(datetime.now()))
print('*'*50)


try:
    for port in range(1,1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print("Checking port {}".format(port))
        if result==0:
            print('the port {} is open '.format(port))
        s.close()


except KeyboardInterrupt:
    print('\n')
    print('Exiting program')
    sys.exit()
except socket.gaierror:
    print('Hostname could not be resolved')
    sys.exit()
except socket.error:
    print('socket could not be resolved')
    sys.exit()        