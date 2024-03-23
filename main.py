# Itz_Wildy and RokyYTR Development
# All rights reserved. Do not copy or redistribute without permission.
# If you have any questions or need further information, please contact us.
# Thanks for your cooperation!

import time
import os
from dhooks import Webhook
import urllib3

print("""
┏┓┏┓┏┓╋╋┏┓╋┏┓╋╋╋╋╋╋╋┏┓╋╋╋┏┓╋╋╋╋╋╋┏┓
┃┃┃┃┃┃╋╋┃┃╋┃┃╋╋╋╋╋╋╋┃┃╋╋┏┛┗┓╋╋╋╋╋┃┃
┃┃┃┃┃┣━━┫┗━┫┗━┳━━┳━━┫┃┏┓┗┓┏╋━━┳━━┫┃┏━━┓
┃┗┛┗┛┃┃━┫┏┓┃┏┓┃┏┓┃┏┓┃┗┛┛╋┃┃┃┏┓┃┏┓┃┃┃━━┫
┗┓┏┓┏┫┃━┫┗┛┃┃┃┃┗┛┃┗┛┃┏┓┓╋┃┗┫┗┛┃┗┛┃┗╋━━┃
╋┗┛┗┛┗━━┻━━┻┛┗┻━━┻━━┻┛┗┛╋┗━┻━━┻━━┻━┻━━┛
    """)

print ("Program is starting...")
time.sleep(0.8)
print ("Please choose Category")
print ("1 - Webhooks")
print ("2 - Not Finished yet.")
print ("3 - Not Finished yet.")

x = input("YOUR CHOICE: ")
if x == "1":
    os.system("cls")
    print("""
┏┓┏┓┏┓╋╋┏┓╋┏┓╋╋╋╋╋╋╋┏┓╋╋╋┏┓╋╋╋╋╋╋┏┓
┃┃┃┃┃┃╋╋┃┃╋┃┃╋╋╋╋╋╋╋┃┃╋╋┏┛┗┓╋╋╋╋╋┃┃
┃┃┃┃┃┣━━┫┗━┫┗━┳━━┳━━┫┃┏┓┗┓┏╋━━┳━━┫┃┏━━┓
┃┗┛┗┛┃┃━┫┏┓┃┏┓┃┏┓┃┏┓┃┗┛┛╋┃┃┃┏┓┃┏┓┃┃┃━━┫
┗┓┏┓┏┫┃━┫┗┛┃┃┃┃┗┛┃┗┛┃┏┓┓╋┃┗┫┗┛┃┗┛┃┗╋━━┃
╋┗┛┗┛┗━━┻━━┻┛┗┻━━┻━━┻┛┗┛╋┗━┻━━┻━━┻━┻━━┛

                                                                                                                
  1. DISCORD WEBHOOK SPAMMER.          2. DISCORD WEBHOOK MULTI-SPAMMER.
  3. COOMING SOON - NOT FINISHED.         4. COOMING SOON.
    """)

    y = input("YOUR CHOICE: ")
    if y == "1":
      message = input("Webhook Tools | TYPE WHAT DO YOU WANT TO SPAM: ")
      if not message.strip():
        message = "@everyone SPAMMED BY INFINIT TOOL NIGGAS"
      print("")
      z=int(input("Type delay:"))
      webhook_url = input("TYPE WEBHOOK URL: ")
      print("")
      print(f"Webhook sending to, {webhook_url}!")
      print(f"With Delay: {z}") 
      time.sleep(1)
      os.system("cls")
      webhook = Webhook(webhook_url)
    if y == "2":
      print ("This Feature suppoorts 10 webhooks.")
      message = input("TYPE WHAT DO YOU WANT TO SPAM: ")
      if not message.strip():
        message = "@everyone SPAMMED BY INFINIT TOOL NIGGAS"
      print("")
      webhook_url = input("TYPE WEBHOOK URL 1: ")
      print("")
      webhook_url1 = input("TYPE WEBHOOK URL 2: ")
      print("")
      webhook_url2 = input("TYPE WEBHOOK URL 3: ")
      print("")
      webhook_url3 = input("TYPE WEBHOOK URL 4: ")
      print("")
      webhook_url4 = input("TYPE WEBHOOK URL 5: ")
      print("")
      webhook_url5 = input("TYPE WEBHOOK URL 6: ")
      print("")
      webhook_url6 = input("TYPE WEBHOOK URL 7: ")
      print("")
      webhook_url7 = input("TYPE WEBHOOK URL 8: ")
      print("")
      webhook_url8 = input("TYPE WEBHOOK URL 9: ")
      print("")
      webhook_url9 = input("TYPE WEBHOOK URL 10: ")
      print("")
      os.system("cls")
      webhook = Webhook(webhook_url)
      webhook1 = Webhook(webhook_url1)
      webhook2 = Webhook(webhook_url2)
      webhook3 = Webhook(webhook_url3)
      webhook4 = Webhook(webhook_url4)
      webhook5 = Webhook(webhook_url5)
      webhook6 = Webhook(webhook_url6)
      webhook7 = Webhook(webhook_url7)
      webhook8 = Webhook(webhook_url8)
      webhook9 = Webhook(webhook_url9)

while True:
    if y == "1":
        time.sleep(z)
        webhook.send(message)
        print("")
        print(f"SUCCESS | SENT {message}")
        print(f"IF SENDING IS TOO SLOW, TRY TO REOPEN PROGRAM.")
    if y == "2":
        webhook.send(message)
        webhook1.send(message)
        webhook2.send(message)
        webhook3.send(message)
        webhook4.send(message)
        webhook5.send(message)
        webhook6.send(message)
        webhook7.send(message)
        webhook8.send(message)
        webhook9.send(message)
        print("")
        print(f"SUCCESS | SENT {message}")
        print(f"IF SENDING IS TOO SLOW, TRY TO REOPEN PROGRAM.")