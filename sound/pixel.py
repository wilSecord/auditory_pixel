import pyautogui as pag

sc = pag.screenshot()
px = sc.getpixel(xy=(960, 540))
sound = (px[0] + px[1] + px[2])/3

print(sound)