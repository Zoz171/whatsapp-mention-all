import pygetwindow as gw
import time
import pyautogui as pg

def countdown(seconds, opt_str=''):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = '{:02d}:{:02d}'.format(mins, secs)
        print(opt_str + timer_display, end='\r') 
        time.sleep(1) 
        seconds -= 1

n = None

while True:
    whatsapp_opened = False
    for window in gw.getWindowsWithTitle("WhatsApp"):
        if window.title == "WhatsApp":
            whatsapp_opened = True

    if whatsapp_opened:
        n = int(input("Enter Number of members in your Group: "))
        print()
        countdown(5, 'Please focus cursor on whatsapp\'s text input ')

        for i in range(n):
            pg.write('@')
            time.sleep(0.1)  # Give WhatsApp time to show the mention list
            pg.keyDown('down')
            pg.keyUp('down')
            time.sleep(0.05)
            pg.press('tab')
    else:
        print("Please open Whatsapp.....", end='\r')
            
# for i in range(10):
#     time.sleep(1)
#     pg.press('down')