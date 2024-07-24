import pyautogui
import time
import keyboard


key_w = 'w'
key_s = 's'
key_a = 'a'
key_d = 'd'

delay_short = 0.25
delay_aow = 5
delay_load = 5  #long dealy for loading

key_aow = 'f'  #ashes of war
key_inter = 'e'  #interaction
key_map = 'm'  #map open


def select_process(process_name):
    try:
        window = pyautogui.getWindowsWithTitle(process_name)[0]
        print("Successed to connect Elden Ring.")
        return window
    except IndexError:
        print("Is that right you're playing Elding Ring??")
        return None


def wait_for_enter():  #wait for your pressing enter
    input("press enter to continue.")


def press_duration(key, delay_var):  #press one key with duration
    start_time = time.time()
    end_time = start_time + delay_var

    while time.time() < end_time:
        keyboard.press(key)
        time.sleep(0.1)
        keyboard.release(key)


# ----------------

#main proc start
elden_farm = select_process("ELDEN RING")
wait_for_enter()

elden_farm.activate()
time.sleep(1)

while 1:
    press_duration(key_w, 1.75)
    press_duration(key_a, 0.5)
    press_duration(key_w, 0.75)
    press_duration(key_a, 0.25)
    press_duration(key_w, 1.5)
    press_duration(key_a, 0.025)
    press_duration(key_w, 1.5)

    press_duration(key_aow, 0.25)
    time.sleep(delay_aow)

    press_duration(key_map, 0.1)
    time.sleep(delay_short)
    press_duration(key_s, 0.05)
    time.sleep(delay_short)
    press_duration(key_inter, 0.25)
    time.sleep(delay_short)
    press_duration(key_inter, 0.25)
    time.sleep(delay_short)
    time.sleep(delay_load)