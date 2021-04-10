import pyautogui as pg

#to move the mouse to the desired coordinates
pg.moveTo(211,23,4)

#just a print statement 
print("look at your mouse, it is moving by it self ^^ ")

#to click the right button of the mouse
pg.click(button='right')

#to move the mouse again
pg.moveTo(262,155,4)

#to click (select something from the list)
pg.click()




#import pyautogui, sys

#this part from line 23 to line 32 it will help you to track the position of the mouse, so you can know the values of x, y
# print('Press Ctrl-C to quit.')
# try:
    # while True:
        # x, y = pyautogui.position()
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # print(positionStr, end='')
        # print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
    # print('\n')
