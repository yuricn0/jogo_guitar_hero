import pyautogui as gui

if gui.pixelMatchesColor(524,720,(0,189,0)):
    gui.press('a')
elif gui.pixelMatchesColor(622,720,(220,1,10)):
    gui.press('s')
elif gui.pixelMatchesColor(717,721,(240,240,0)):
    gui.press('j')
