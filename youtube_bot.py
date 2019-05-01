from pyautogui import press
from pyautogui import keyDown
from pyautogui import keyUp
from pyautogui import typewrite
from time import sleep
from requests import get

import webbrowser
import os

class Bot:
    def __init__(self, url, views):

        if url.startswith("https://www.youtube.com/watch?v="):
            if self.test_url(url):
                self.url = url
            else:
                print("* This URL dosen't exist *")
                quit()
        else:
            print("* Bad requested URL *")
            quit()


        self.views = views

    def test_url(self, url):
        response = get(url).status_code
        if response == 200:
            return True
        return False

    def open_window(self):
        webbrowser.open_new(self.url)
        press("enter")

    def start_bot(self):
        for _ in range(self.views):
            sleep(2.5)
            if os.name == "nt":
                press("f5")
            elif os.name == "posix":
                keyDown("command")
                press("r")
                keyUp("command")
    
    def banner(self):
        message = "* For make working correctly the script, you have to be disconnected of your YouTube's account *"
        print(message)

def main():

    url = input("* Enter the vieo's URL * : ")
    if len(url.strip()) == 0:
        print("* Bad requested URL *")
        quit()
    try:
        views = int(input("* Enter the number of views that you want * : "))
    except:
        print("* Bad requested views *")
        quit()

    bot = Bot(url, views)
    bot.banner()
    bot.open_window()
    bot.start_bot()
main()