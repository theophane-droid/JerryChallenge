import time

from labyrinthe import Labyrinthe, UP, DOWN, LEFT, RIGHT
from exceptions import WinException, InvalidMoveException

# read flag02 to flag04
with open('flag02.txt', 'r') as f:
    FLAG2 = f.read()
with open('flag03.txt', 'r') as f:
    FLAG3 = f.read()
with open('flag04.txt', 'r') as f:
    FLAG4 = f.read()
with open('banner.txt', 'r') as f:
    BANNER = f.readlines()
 
def print_banner():
    i = 0
    for line in BANNER:
        if i < 7:
            print(line)
        else:
            for c in line:
                print(c, end='', flush=True)
                time.sleep(0.05)
        if i in [0, 1, 5, 6]:
            time.sleep(1)
        i += 1
if __name__ == "__main__":
    print_banner()
    lab = Labyrinthe(11, nb_break=20)
    win = False
    start_time = time.time()
    while True:
        print(lab)
        dir = input('$ ')
        if dir in [UP, DOWN, LEFT, RIGHT]:
            try:
                lab.moove(dir, lab.jerry)
            except WinException:
                win = True
                break
            except InvalidMoveException:
                print('> Squik ! I can\'t go there !')
                time.sleep(1)
        elif dir == 'please give me a flag':
            print('> Sure :', FLAG2)
            time.sleep(1)
        else:
            print('> Squik ! is not valid direction !')
            time.sleep(1)
    if win:
        if time.time() - start_time > 5:
            print('> Thank you for helping me reach my cheese')
            time.sleep(1)
            print('> But you waited too long, it stinks now!')
            time.sleep(1)
            print('> Huuummm, I will still give you a flag')
            time.sleep(1)
            print('> Here it is :', FLAG3)
            time.sleep(1)
            print('> You should try to be faster ! Try, to write a little program to help me !')
            time.sleep(1)
            print('> You have only 5 secs to do it !')
            exit()
        else:
            print('> Well done !!')
            print('> See you in the mouse challenge ;)')
            time.sleep(1)
            print('> Btw, you deserved this flag : ', FLAG4)