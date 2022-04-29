import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

session = requests.session()

print(Fore.RED + """ 


████████╗██████╗░██╗░██████╗░░██████╗░██╗░░░██╗
╚══██╔══╝██╔══██╗██║██╔════╝░██╔════╝░╚██╗░██╔╝
░░░██║░░░██████╔╝██║██║░░██╗░██║░░██╗░░╚████╔╝░
░░░██║░░░██╔══██╗██║██║░░╚██╗██║░░╚██╗░░╚██╔╝░░
░░░██║░░░██║░░██║██║╚██████╔╝╚██████╔╝░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚═════╝░░╚═════╝░░░░╚═╝░░░
      
      
░█████╗░███╗░░██╗██████╗░
██╔══██╗████╗░██║██╔══██╗
███████║██╔██╗██║██║░░██║
██╔══██║██║╚████║██║░░██║
██║░░██║██║░╚███║██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░

      
████████╗███████╗███╗░░██╗░██████╗███████╗██╗░██████╗
╚══██╔══╝██╔════╝████╗░██║██╔════╝██╔════╝╚█║██╔════╝
░░░██║░░░█████╗░░██╔██╗██║╚█████╗░█████╗░░░╚╝╚█████╗░
░░░██║░░░██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░░░░░╚═══██╗
░░░██║░░░███████╗██║░╚███║██████╔╝███████╗░░░██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝░░░╚═════╝░
      
▀█▀ ▀█▀   █▀█ █▀▀ █▀█ █▀█ █▀█ ▀█▀   █▄▄ █▀█ ▀█▀
░█░ ░█░   █▀▄ ██▄ █▀▀ █▄█ █▀▄ ░█░   █▄█ █▄█ ░█░
      """)
print("USE A VPN TO PREVENT THE IP BAN")
print("Join the discord for Updates: https://discord.gg/Qwy5KE4369 ")
print("A report is sent every 10 seconds")
print("")
print("")

x = input('Enter the request URL from Inspect Element: ')
print("")
print("")

print('Reporting...')
print('')
print('')

while True:
    req = session.post(x)
    
    print(req.text)
    print('Reported :)')

    time.sleep(10)


input()
