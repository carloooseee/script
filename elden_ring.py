from pynput.keyboard import Controller, Key
from time import sleep

keyboard = Controller()

repeat = 10000

print("Initiated")
for i in range(5, 0, -1):
    print(f"{i}")
    sleep(1)
def aow():
    print('*using ash of war')
    keyboard.press('i')
    sleep(3)
    keyboard.release('i')
    sleep(3)
def openmap():
    print('*opening map')
    keyboard.press('g')
    sleep(0.5)
    keyboard.release('g')
    keyboard.press('f')
    sleep(0.5)
    keyboard.release('f')
def teleport():
    print('*teleporting')
    keyboard.press(Key.enter)
    sleep(0.5)
    keyboard.release(Key.enter)
    sleep(0.5)
    keyboard.press(Key.enter)
    sleep(0.5)
    keyboard.release(Key.enter)
def mohg():
    print('Loading Actions.....')
    print('*moving to location')
    keyboard.press('w')
    sleep(4)
    keyboard.release('w')
    keyboard.press('a')
    sleep(1)
    keyboard.release('a')
    keyboard.press('w')
    sleep(1)
    keyboard.release('w')
    sleep(1 )
    aow()
    openmap()
    teleport()
    sleep(7)

for i in range(repeat):
    print(f'====Loop #{i+1} started====')
    mohg()
    print(f'====Loop #{i+1} ended====\n')
    sleep(2)