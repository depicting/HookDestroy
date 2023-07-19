import requests
import json
import time
import os
import sys
from colorama import *
from pystyle import *
import threading

os.system('clear' if os.name == 'posix' else 'cls')

intro = """                
 ██░ ██  ▒█████   ▒█████   ██ ▄█▀   ▓█████▄ ▓█████   ██████ ▄▄▄█████▓ ██▀███   ▒█████▓██   ██▓
▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▒██▀ ██▌▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒██  ██▒
▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ░██   █▌▒███   ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒▒██ ██░
░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ░▓█▄   ▌▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░░ ▐██▓░
░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄   ░▒████▓ ░▒████▒▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░░ ██▒▓░
 ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒    ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ██▒▒▒ 
 ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░    ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░▓██ ░▒░ 
 ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░     ░ ░  ░    ░   ░  ░  ░    ░        ░░   ░ ░ ░ ░ ▒ ▒ ▒ ░░  
 ░  ░  ░    ░ ░      ░ ░  ░  ░         ░       ░  ░      ░              ░         ░ ░ ░ ░     
                                     ░                                                ░ ░   


                                     > Press Enter
"""

Anime.Fade(Center.Center(intro), Colors.blue_to_black, Colorate.Vertical, interval=0.035, enter=True)


init()

intro = f"""{Fore.BLUE}

   ▄█    █▄    ████████▄  
  ███    ███   ███   ▀███ 
  ███    ███   ███    ███ 
 ▄███▄▄▄▄███▄▄ ███    ███  ʙʏ ʀᴇɴᴋᴏ & ʟᴇᴅɢᴇʀ
▀▀███▀▀▀▀███▀  ███    ███ 
  ███    ███   ███    ███ 
  ███    ███   ███   ▄███ 
  ███    █▀    ████████▀                              
                                                                                                                                                                                                  
{Fore.MAGENTA}> 1 - Webhook spammer
{Fore.MAGENTA}> 2 - Webhook deleter
{Fore.MAGENTA}> 3 - Exit

"""

print(intro)


def send_message(webhook_url, message):
    """
    Sends messages continuously to the specified webhook URL.
    """
    while True:
        data = {
            "content": message,
            "username": ".gg/debt",
            "avatar_url": "https://cdn.discordapp.com/attachments/1131161283509616643/1131163396105056278/fatfuck.jpg"
        }

        json_data = json.dumps(data)

        response = requests.post(webhook_url, data=json_data, headers={"Content-Type": "application/json"})

        if response.status_code == 204:
            print(f"[+] Sent!")
        
        
        time.sleep(1)


while True:
    choice = input(f"{Fore.BLUE}Enter your choice: {Fore.MAGENTA}")
    if choice == "1":

        print(f"{Fore.GREEN}You have selected the webhook spammer. (press E to exit)")
        while True:
            webhook_url = input(f"{Fore.BLUE}Please enter the Discord webhook URL: {Fore.MAGENTA}")
            if webhook_url == "e":
                break
            if webhook_url == "E":
                break

            try:
                response = requests.get(webhook_url)
                if not response.ok:
                    raise ValueError("Invalid webhook URL!")
            except Exception as e:
                print(f"Invalid webhook URL! Error message: {str(e)}")
                continue

            while True:
                message = input(f"{Fore.BLUE}Please enter the message to be sent: {Fore.MAGENTA}")
                if message == "e":
                    break
                if message == "E":
                    break

               
                threads = []
                for i in range(10):  
                    thread = threading.Thread(target=send_message, args=(webhook_url, "@everyone " + message))
                    threads.append(thread)
                    thread.start()

    elif choice == "2":

        print(f"{Fore.GREEN}You have selected the webhook deleter. (press E to exit)")
        while True:
            webhook_url = input(f"{Fore.BLUE}Please enter the Discord webhook URL you want to delete: {Fore.MAGENTA}")
            if webhook_url == "e":
                break
            if webhook_url == "E":
                break

            try:
                response = requests.head(webhook_url)
                assert response.status_code == 200
            except:
                print(f"{Fore.RED}Invalid webhook URL! Please try again.")
                continue

            response = requests.delete(webhook_url)

            if response.status_code == 204:
                print(f"{Fore.GREEN}The webhook has been successfully deleted.")
            else:
                print(f"{Fore.RED}Error deleting webhook: {response.status_code}")
    elif choice == "3":
        print("Exiting program...")
        sys.exit()
    else:
        print(f"{Fore.RED}Invalid choice! Please try again.")