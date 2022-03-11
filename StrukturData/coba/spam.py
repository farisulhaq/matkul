# from typing import MutableMapping
# import pyautogui, time
# ps = pyautogui.position()
# pesan = "marah yaa!"
# for i in range(30):
#     pyautogui.click(ps.x,ps.y)
#     pyautogui.typewrite(pesan)
#     print(pesan)
#     time.sleep(0.5)
#     pyautogui.typewrite(['enter'])


def prev_mult_of_three(n):
    while n % 3:
        n //= 10
        print(n)
    return 0 or None
print(prev_mult_of_three(10))