import pygame
import pyautogui

# Initialization Pygame
pygame.init()

# Gain joystick data
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

if not joysticks:
    exit()
for i, j in enumerate(joysticks):
    print(f"{i+1}. {j.get_name()}")

# Device selection
selection = int(input("Please Input The Number of The Joystick: ")) - 1
joystick = joysticks[selection]
joystick.init()

# Main loop
print(f"Connected: {joystick.get_name()}")
pyautogui.FAILSAFE = False  # Disable fail-safe to prevent mouse movement from stopping the script.
while True:
    pygame.event.pump()
    channel1 = joystick.get_axis(0) * 100
    channel2 = joystick.get_axis(1) * 100
    if 50 < channel1 <= 100:
        pyautogui.keyDown('shift')
        pyautogui.keyDown('d')
    elif 2 < channel1 <= 50:
        pyautogui.keyDown('d')
    elif -50 < channel1 < -2:
        pyautogui.keyDown('a')
    elif -100 <= channel1 <= -50:
        pyautogui.keyDown('shift')
        pyautogui.keyDown('a')
    pyautogui.keyUp('Shift')
    pyautogui.keyUp('d')
    pyautogui.keyUp('a')
    
    if 50 < channel2 <= 100:
        pyautogui.keyDown('shift')
        pyautogui.keyDown('w')
    elif 2 < channel2 <= 50:
        pyautogui.keyDown('w')
    elif -50 < channel2 < -2:
        pyautogui.keyDown('s')
    elif -100 <= channel2 <= -50:
        pyautogui.keyDown('shift')
        pyautogui.keyDown('s')
    pyautogui.keyUp('Shift')
    pyautogui.keyUp('w')
    pyautogui.keyUp('s')