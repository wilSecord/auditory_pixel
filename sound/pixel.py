import pyautogui as pag

sc = pag.screenshot()
px = sc.getpixel(xy=(960, 540))
print(px[0])