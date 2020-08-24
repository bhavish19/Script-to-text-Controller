import pyautogui, time
x,y=pyautogui.position()
pyautogui.click(x,y)
f = open("script.txt","r")
contents = f.readlines()
for x in contents:
    time.sleep(1)
    pyautogui.typewrite(x)
