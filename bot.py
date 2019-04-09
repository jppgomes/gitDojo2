import pyscreenshot as ImageGrab
import pyautogui
import numpy as np

class Cordinates():
	replayBtn = (700, 440)
	im = ImageGrab.grab()
	im2 = np.asanyarray(im)
def restartGame():
	pyautogui.click(Cordinates.replayBtn)

restartGame()
	
