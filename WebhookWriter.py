import requests
from art import text2art
from colorama import init, Fore, Style
from datetime import datetime

init()

now = datetime.now()
current_date = now.strftime("%Y-%m-%d %H:%M:%S")

def send_webhook(webhook_url, content):
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        'content': content
    }
    
    try:
        response = requests.post(webhook_url, json=data, headers=headers)
        response.raise_for_status()
        print(f'{Fore.WHITE}{current_date} (1/1) {Fore.WHITE}>>>{Fore.YELLOW} Sent: "{content}"')
    except requests.exceptions.RequestException as e:
        print(f'{Fore.RED}Error: {e}')

def spam_webhook(webhook_url, content, pytanie):
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        'content': content
    }
    
    try:
        ilosc1 = int(pytanie)
    except ValueError:
        print(f'{Fore.RED}Error: Invalid number of repetitions.')
        return
    
    ilosc = ilosc1 + 1
    uzyta = 0
    
    for i in range(1, ilosc):
        try:
            uzyta = uzyta+1
            response = requests.post(webhook_url, json=data, headers=headers)
            response.raise_for_status()
            print(f'{Fore.WHITE}{current_date} ({uzyta}/{ilosc}) {Fore.WHITE}>>>{Fore.YELLOW} Sent: "{content}"')
        except requests.exceptions.RequestException as e:
            print(f'{Fore.RED}Error: {e}')
            break

def start():
    naglowek = text2art("WEBHOOK   WRITER")
    print(f"{Fore.CYAN}{naglowek}\nGITHUB: https://github.com/stainowy/WebhookWriter\nAUTHOR: https://github.com/stainowy\n\n{Fore.WHITE}Our current webhook writer has the following features:\n{Fore.CYAN}   [1] {Fore.WHITE}Webhook Send           {Fore.CYAN}[2] {Fore.WHITE}Webhook Spam")

    akcja = input(f"{Fore.WHITE}> ")

    if akcja == "1":
        webhook_url = input(f"{Fore.CYAN}Please enter the link to the webhook:\n{Fore.WHITE}> ")
        content = input(f"\n{Fore.CYAN}Please enter your webhook content:\n{Fore.WHITE}> ")
        send_webhook(webhook_url, content)
        e = input("")
    elif akcja == "2":
        webhook_url = input(f"{Fore.CYAN}Please enter the link to the webhook:\n{Fore.WHITE}> ")
        content = input(f"\n{Fore.CYAN}Please enter your webhook content:\n{Fore.WHITE}> ")
        pytanie = input(f"\n{Fore.CYAN}How many times should the message be repeated?\n{Fore.WHITE}> ")
        spam_webhook(webhook_url, content, pytanie)
        e = input('')
    else:
        print(f"{Fore.RED}Invalid option. Please choose either 1 or 2.")

if __name__ == "__main__":
    start()
