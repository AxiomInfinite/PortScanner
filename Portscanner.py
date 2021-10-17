import sys
import socket
from datetime import datetime
#Future Improvements
#Better Handle ranges, have predefined ranges for selection


#Define our target 
if len(sys.argv) == 2: 
    #Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("Syntax: Python3 Scanner <IP>")

print("-" * 50)
print("Scanning target " + target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        #returns an error indicator
        result = s.connect_ex((target.port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
#Ways to get out of the problem
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")

except socket.error:
    print("Couldnt connect to server")
    sys.exit