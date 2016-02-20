from socket import *
import sys, time
from datetime import datetime

host = str(' ')
max_port = int(5000)
min_port = int(1)

try:
    host= input("voer een IP adres in")

except isinstance(host, int):
    print ("u heeft geen geldig IP adres ingevoegd")


except KeyboardInterrupt:
        print("Gebruiker heeft het programma afgebroken)")
        sys.exit(1)


