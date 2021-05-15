from pytube import YouTube
from colorama import Fore
from banner import banner
import shutil
import os
import time

def video_saver(title):
    files= os.listdir()
    for thing in files:
        if title in thing:
            shutil.copy(thing, destination)
            print(Fore.BLUE+f"Video saved in { destination } "+Fore.RESET)
        else: pass

try:
    destination=open("destination.inf", "r")
except:
    destination=open("destination.inf", "w")
    destination.write("./Desktop")
    destination.close()
    destination=open("destination.inf", "r")

banner.banner()

try:
    print(Fore.CYAN+"please enter which type of resolution do you want")
    time.sleep(0.1)
    print("1- Highest resolution")
    time.sleep(0.1)
    print("2- Lowest resolution")
    time.sleep(0.1)
    resolution= input(Fore.CYAN+"Please enter a number: "+Fore.RESET)
    
    if "1" in resolution :    #Download lowest resolution
        try:
            link = input(Fore.WHITE+"Please enter the link : "+Fore.RESET)
            video = YouTube(link)
            stream = video.streams.get_highest_resolution()
            video_name= YouTube.title()
            print (video_name)
            booly = input("Is it right (Y/N): ")
            if booly == "y" or booly == "Y" :
                stream.download()
                print(Fore.GREEN+f"[ File {video_name} Downloaded! ]")
                video_saver(video_name)
                input(Fore.CYAN+"Press any key to exit ... "+Fore.RESET)
                exit()
        except :
            print (Fore.RED+"Your link is wrong")
            input(Fore.CYAN+"Press any key to exit ... "+Fore.RESET)
            exit()

    elif "2" in resolution :
        try:
            link = input(Fore.WHITE+"Please enter the link : "+Fore.RESET)
            video = YouTube(link)
            stream = video.streams.get_lowest_resolution()
            video_name= YouTube.title()
            print (video_name)
            booly = input("Is it right (Y/N): ")
            if booly == "y" or booly == "Y" :
                stream.download()
                print(Fore.GREEN+f"[ File {video_name} Downloaded! ]")
                video_saver(video_name)
            input("press any key to exit ... ")
            exit()
        except :
            print ("Your link is wrong")
            input("press any key to exit ... ")
            exit()
    else:
        print(Fore.RED+"Please just enter 1 or 2")
        input(Fore.CYAN+"Press any key to exit ... "+Fore.RESET)
        exit()

except KeyboardInterrupt:
    print("GoodBye!")
    exit()
except Exception as ex:
    print (ex)