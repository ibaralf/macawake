import pyautogui
import random
import time
import re

def show_title():
    title = """
 __  __                 _                _        
|  \/  | __ _  ___     / \__      ____ _| | _____ 
| |\/| |/ _` |/ __|   / _ \ \ /\ / / _` | |/ / _ \\
| |  | | (_| | (__   / ___ \ V  V / (_| |   <  __/
|_|  |_|\__,_|\___| /_/   \_\_/\_/ \__,_|_|\_\___|
                                                   
    """
    print(title)

def get_sec():
    retsec = 60
    RE_INT = re.compile(r'^[-+]?[0-9]+$')
    is_int = False
    while not is_int: 
        n = input("Enter seconds between move: ")
        if bool(re.match(r'^[1-9]+[0-9]*$', n)): 
            is_int = True
            retsec = int(n)
        else:
            print("ERROR: Please enter an integer value.")
    
    return retsec

def get_msg(numsec):
    time_msg = str(numsec) + " seconds"
    if numsec > 60:
        nmins = numsec // 60
        nsecs = numsec % 60
        time_msg = str(nmins) + " mins " + str(nsecs) + " secs"
    return time_msg

show_title()
nsec = get_sec()
tmsg = get_msg(nsec)

while True:
    x = random.randint(0,1000)
    y = random.randint(0,1000)
    pyautogui.moveTo(x,y)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print('Moved at ' + str(current_time) + ' ('  + str(x) + ', ' + str(y) + ')' + " every " + tmsg)
    time.sleep(nsec)