import platform
from colorama import Fore,Style
import os
import time

def banner():
    os_name= platform.uname()[0]
    if "Linux" in os_name:
        os.system("clear")
        os.system("neofetch")
        time.sleep(0.5)
        print(Fore.LIGHTMAGENTA_EX+"""Welcome to my YouTube Video Downloader
This software will download your video in High/Low reolution now let's start"""+Fore.RESET)
        time.sleep(0.5)
    elif "Win" in os_name:
        os.system("cls")
        print(Fore.MAGENTA+"""
               /$$     /$$               /$$$$$$$$        /$$                                 
              |  $$   /$$/              |__  $$__/       | $$                                 
               \  $$ /$$//$$$$$$  /$$   /$$| $$ /$$   /$$| $$$$$$$   /$$$$$$                  
                \  $$$$//$$__  $$| $$  | $$| $$| $$  | $$| $$__  $$ /$$__  $$                 
                 \  $$/| $$  \ $$| $$  | $$| $$| $$  | $$| $$  \ $$| $$$$$$$$                 
                  | $$ | $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$| $$_____/                 
                  | $$ |  $$$$$$/|  $$$$$$/| $$|  $$$$$$/| $$$$$$$/|  $$$$$$$                 
                  |__/  \______/  \______/ |__/ \______/ |_______/  \_______/                                                                                                                                                                                                          
 /$$$$$$$                                    /$$                           /$$                    
| $$__  $$                                  | $$                          | $$                    
| $$  \ $$  /$$$$$$  /$$  /$$  /$$ /$$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$  | $$ /$$__  $$| $$ | $$ | $$| $$__  $$| $$ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  | $$| $$  \ $$| $$ | $$ | $$| $$  \ $$| $$| $$  \ $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \__/
| $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$| $$  | $$ /$$__  $$| $$  | $$| $$_____/| $$      
| $$$$$$$/|  $$$$$$/|  $$$$$/$$$$/| $$  | $$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
|_______/  \______/  \_____/\___/ |__/  |__/|__/ \______/  \_______/ \_______/ \_______/|__/      
        """)
        time.sleep(0.5)
        print(Fore.LIGHTMAGENTA_EX+"""Welcome to my YouTube Video Downloader
This software will download your video in High/Low reolution now let's start"""+Fore.RESET)
banner()