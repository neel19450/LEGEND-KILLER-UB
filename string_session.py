from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import random
from colorama import Fore, Style, Back


aura = """
╔╗──╔═══╦═══╦═══╦═╗─╔╦═══╦═══╦═══╦╗──╔╗
║║──║╔══╣╔═╗║╔══╣║╚╗║╠╗╔╗║╔═╗║╔═╗║╚╗╔╝║  
║║──║╚══╣║─╚╣╚══╣╔╗╚╝║║║║║║─║║╚═╝╠╗╚╝╔╝  
║║─╔╣╔══╣║╔═╣╔══╣║╚╗║║║║║║╚═╝║╔╗╔╝╚╗╔╝   
║╚═╝║╚══╣╚╩═║╚══╣║─║║╠╝╚╝║╔═╗║║║╚╗─║║   
╚═══╩═══╩═══╩═══╩╝─╚═╩═══╩╝─╚╩╝╚═╝─╚╝   
"""
logo = """
.____                                    .___  ____  __.__.__  .__                  ____ ___                  ___.           __   
|    |    ____   ____   ____   ____    __| _/ |    |/ _|__|  | |  |   ___________  |    |   \______ __________\_ |__   _____/  |_ 
|    |  _/ __ \ / ___\_/ __ \ /    \  / __ |  |      < |  |  | |  | _/ __ \_  __ \ |    |   /  ___// __ \_  __ \ __ \ /  _ \   __\
|    |__\  ___// /_/  >  ___/|   |  \/ /_/ |  |    |  \|  |  |_|  |_\  ___/|  | \/ |    |  /\___ \\  ___/|  | \/ \_\ (  <_> )  |  
|_______ \___  >___  / \___  >___|  /\____ |  |____|__ \__|____/____/\___  >__|    |______//____  >\___  >__|  |___  /\____/|__|  
        \/   \/_____/      \/     \/      \/          \/                 \/                     \/     \/          \/             
"""
baap_bolte = """
#Legendary Legend Killer Userbot          
Made With Love By Team Legend Killer userbot
"""
                                                                                                            
print("")
print(Style.BRIGHT + Fore.MAGENTA + aura)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.BLUE + logo)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.CYAN + Back.BLUE + baap_bolte)
print(Style.RESET_ALL)
print("""Welcome To Legend Killer String Generator By @killer_king_xd""")
print("""Kindly Enter Your Details To Continue ! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("String Sent To Your Saved Message, Store It To A Safe Place!! ")
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit @LEGEND_KILLER_Userbot For Any Help !",
            )

            print(
                "Thanks for Choosing W2HBOT Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +919811099999 ! Kindly Retry"
        )
        print("")
        continue
    break
