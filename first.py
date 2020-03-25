import pyautogui

pyautogui.hotkey('win')

pyautogui.typewrite('notepad')
pyautogui.hotkey('enter')
pyautogui.typewrite("Hi Im Prema's bot", interval=0.5)
pyautogui.hotkey('ctrl', 's')
pyautogui.typewrite('filename.txt')
pyautogui.hotkey('enter')
pyautogui.hotkey('alt', 'f4')