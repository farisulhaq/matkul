from typing import MutableMapping
import pyautogui, time
ps = pyautogui.position()
pesan = "sayangku, maap"
for i in range(100):
    pyautogui.click(ps.x,ps.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.5)
    pyautogui.typewrite(['enter'])
