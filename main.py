import requests
import random
from colorama import *
from datetime import datetime
import os

def rntime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

os.system('cls')
print(f"""{Fore.MAGENTA}
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝                                                                                         
by miki | moddatei
""")

channel_id = input(f"{Fore.MAGENTA}[+] Enter channel ID: {Fore.RESET}")
amount = int(input(f"{Fore.MAGENTA}[+] Number of message you want send : {Fore.RESET}"))
message = input(f"{Fore.MAGENTA}[+] Message you want to send : {Fore.RESET}")

os.system('cls')

def nonce_generator(length=19):
    return ''.join(str(random.randint(1, 9)) for _ in range(length))

json_template = {
    "mobile_network_type": "unknown",
    "content": message,
    "nonce": "",
    "tts": False,
    "flags": 0
}

before_time = datetime.now()

with open("tokens.txt") as f:
	tokens = f.read().splitlines()

token_index = 0
num_tokens = len(tokens)

for _ in range(amount):
    
    header = {
        "Authorization": tokens[token_index]
    }
    
    token_index = (token_index + 1) % num_tokens
    
    json_data = {
        "mobile_network_type": "unknown",
        "content": message,
        "nonce": nonce_generator(),
        "tts": False,
        "flags": 0
    }
    req = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=header, json=json_data)
    if req.status_code == 200:
        print(f"{Fore.WHITE}[{Fore.GREEN}{rntime()}{Fore.WHITE}] {Fore.GREEN}Message sent: {tokens[token_index][:49]}****.****")
    else:
        print(f"{Fore.WHITE}[{Fore.RED}{rntime()}{Fore.WHITE}] {Fore.RED}Error with token: {tokens[token_index][:49]}****.**** : {req.status_code} : {req.text}")

after = datetime.now()

print(f"{Fore.GREEN}All message sent. Spamming already finished.")