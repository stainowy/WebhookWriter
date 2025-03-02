import requests
from art import text2art
from colorama import init, Fore, Style
from datetime import datetime

init()

now = datetime.now()
current_date = now.strftime("%Y-%m-%d %H:%M:%S")

def spam_webhook(webhook_url, content, count):
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        'content': content
    }
    
    try:
        count1 = int(count)
    except ValueError:
        print(f'{Fore.RED}Error: Invalid number of repetitions.')
        return
    
    count2 = count1 + 1
    uzyta = 0
    
    for i in range(1, count2):
        try:
            uzyta = uzyta+1
            response = requests.post(webhook_url, json=data, headers=headers)
            response.raise_for_status()
            print(f'{Fore.WHITE}{current_date} ({uzyta}/{count2}) {Fore.WHITE}>>>{Fore.YELLOW} Sent: "{content}"')
        except requests.exceptions.RequestException as e:
            print(f'{Fore.RED}Error: {e}')
            break

def start():
    naglowek = text2art("WEBHOOK  WRITER")
    print(f"{Fore.CYAN}{naglowek}\nGITHUB: {Fore.WHITE}https://github.com/stainowy/WebhookWriter\n{Fore.CYAN}AUTHOR: {Fore.WHITE}https://github.com/stainowy\n\n{Fore.WHITE}To run the program, select the functions:\n{Fore.CYAN}   [1] {Fore.WHITE}Start")

    akcja = input(f"{Fore.WHITE}> ")

    if akcja == "1":
        webhook_url = input(f"{Fore.CYAN}Please enter the link to the webhook:\n{Fore.WHITE}> ")
        content = input(f"\n{Fore.CYAN}Please enter your webhook content:\n{Fore.WHITE}> ")
        count = input(f"\n{Fore.CYAN}How many times should the message be repeated?\n{Fore.WHITE}> ")
        spam_webhook(webhook_url, content, count)
        end = input('')
        if end == "fuck":
            print("You're a fuck, don't swear!!!")
    else:
        print(f"{Fore.RED}Invalid option.")

if __name__ == "__main__":
    start()
