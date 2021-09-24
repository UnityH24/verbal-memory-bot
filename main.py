from PIL import ImageGrab, Image
import win32api, win32con
import time
import os
import keyboard
import string
import sys
import random

"""Constants"""
try:
	delay = int(sys.argv[1])
except:
	delay = 1
region = (786, 344, 1106, 424)
curr_dir = os.path.dirname(__file__)
pic_path = os.path.join(curr_dir, "pic.png")
word_path = os.path.join(curr_dir, "words")
seen = (881, 473)
new = (1016, 476)

def click(pos):
	win32api.SetCursorPos(pos)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(0.005)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	
def del_pic():
	if os.path.exists(pic_path):
		os.remove(pic_path)

def clear_words():
	for subdir, dirs, files in os.walk(word_path):
		for file in files:
			os.remove(os.path.join(subdir, file))
		
def get_screenshot():
	return ImageGrab.grab(bbox=region)

def is_in_words(word):
	img = Image.open(word)
	for subdir, dirs, files in os.walk(word_path):
		for file in files:
			im = Image.open(os.path.join(subdir, file))
			if list(img.getdata()) == list(im.getdata()):
				return True
			
	return False
	
def main():
	clear_words()
	while not keyboard.is_pressed('q'):
		if keyboard.is_pressed('p'):
			while not keyboard.is_pressed('q'):
				word = get_screenshot()
				word.save(os.path.join(pic_path))
				if is_in_words(pic_path):
					click(seen)
					
				else:
					del_pic()
					name = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(5)]) + ".png"
					word.save(os.path.join(word_path, name))
					click(new)
					
				time.sleep(delay)
				
			else:
				break
	clear_words()
	
	
main()