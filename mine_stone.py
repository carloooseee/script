import pyautogui as press
from time import sleep

pickaxe = 9
seconds = 243
elapseTime = pickaxe * seconds
def mine_stone(seconds):
    press.keyDown('i')
    sleep(seconds)
    press.keyUp('i')

print("Program Started")
sleep(5)
for i in range  (1, pickaxe + 1):
    print(f'Update: Tool #{i} Currently in use')
    press.press(str(i))
    mine_stone(seconds)
    print(f'Update: Tool #{i} used')

print(f'Total Elapsed Time: {elapseTime} seconds')