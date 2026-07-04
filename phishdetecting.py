
import argparse
import time
from colorama import Fore, Style, init
from urllib.parse import urlparse
init(autoreset=True)
keywords=[
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "password",
    "bank",
    "wallet",
    "signin",
    "confirm"
]


a = argparse.ArgumentParser(description="""
===========================================
   PHISHING DETECTOR v1.0
===========================================


"Trust nothing. Verify everything."
===========================================
""",formatter_class=argparse.RawTextHelpFormatter)
a.add_argument("-u","--url",required=True,help="website link")
a.add_argument("-v","--verbose",action = "store_true",help="show the process")
args = a.parse_args()
p = urlparse(args.url)

url = args.url
score = 0
if url.startswith("https://"):
    score = score + 10
else:
    score = score - 10

if len(url) > 70:
    score = score - 10
if "@" in url:
    score = score - 10
if "-" in url:
    score = score - 10
for keyword in keywords:
    if keyword in url.lower():
        score = score - 10
if args.verbose:

   print(Fore.BLUE +"-----------------------")
   time.sleep(1)
   print(Fore.CYAN +"URL:", url)
   time.sleep(1)
   print("[*] Analyzing URL...")
   print(Fore.LIGHTGREEN_EX + f"Protocol : {p.scheme}")
   print(Fore.LIGHTGREEN_EX + f"Hostname : {p.hostname}")
   print(Fore.LIGHTGREEN_EX + f"Path     : {p.path}")
   print(Fore.LIGHTBLUE_EX +"Score:", score)

else:
    time.sleep(3)
if score >= 10:
    print(Fore.GREEN + "[+] Status: Looks Safe")
elif score >= 0:
    print(Fore.YELLOW + "[!] Status: Use Caution")
elif score >= -30:
    print(Fore.RED + "[-] Status: Suspicious")
else:
    print(Fore.RED + Style.BRIGHT + "[!!] Status: Dangerous")





