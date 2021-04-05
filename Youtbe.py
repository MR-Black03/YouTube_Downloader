from pytube import YouTube


print ("""....
Welcome to my youtube video downloader.
....""")

try :

    resolution = int(input ("""please enter which type of resolution do you want

1- Highest resolution

2- Lowest resolution

Please enter a number: """)
)
    
    if resolution == 2 :
    
        try:

            link = input("Please enter the link : ")

            video = YouTube(link)

            stream = video.streams.get_lowest_resolution()

            print("Title: ",YouTube.title)

            booly = input("Is it right (Y/N): ")

            if booly == "y" or booly == "Y" :
                stream.download()

                print("Download completed!!")

            input("press any key to exit ... ")

            exit()

        except :

            print ("Your link is wrong")

            input("press any key to exit ... ")

            exit()


    elif resolution == 1 :
    
        try:

            link = input("Please enter the link : ")

            video = YouTube(link)

            stream = video.streams.get_highest_resolution()

            print("Title: ",YouTube.title)

            booly = input("Is it right (Y/N): ")

            if booly == "y" or booly == "Y" :

                stream.download()

                print("Download completed!!")

            input("press any key to exit ... ")

            exit()


        except :

            print ("Your link is wrong")

            input("press any key to exit ... ")

            exit()

    else:

        print("your number is wrong")

        input("press any key to exit ... ")

        exit()

except:

    print ("There is a problem")

    input("press any key to exit ... ")

    exit()