from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import speech
commands = ["Mouse Down", "Mouse all the way to the right", "Mouse all the way to the left", "Right Click", "Mouse to the left a little", "Double Click", "Mouse to the right a lot", "Mouse to the left a lot", "Mouse to the right a little", "Mouse Up", "Mouse down a little", "Mouse to the right", "Mouse Up a little", "Mouse to the left", "Click"]
print commands
def Get(phrase, listener):
    if phrase == "Mouse Down":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0], pos[1] - -100)
    elif phrase == "Right Click":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.click(pos[0], pos[1], 3)
    elif phrase == "Click":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.click(pos[0], pos[1])
    elif phrase == "Double Click":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.click(pos[0], pos[1])
        m.click(pos[0], pos[1])
    elif phrase == "Mouse Up":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0], pos[1] - 100)
    elif phrase == "Mouse Up a little":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0], pos[1] - 20)
    elif phrase == "Mouse down a little":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0], pos[1] - -20)
    elif phrase == "Mouse to the left":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0] - 50, pos[1])
    elif phrase == "Mouse to the right":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0] + 50, pos[1])
    elif phrase == "Mouse to the right a little":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0] + 10, pos[1])
    elif phrase == "Mouse to the right a lot":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0] + 200, pos[1])
    elif phrase == "Mouse all the way to the right":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0] + 1000, pos[1])
    elif phrase == "Mouse all the way to the left":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0] - 1000, pos[1])
    elif phrase == "Mouse to the left a little":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0] - 10, pos[1])
    elif phrase == "Mouse to the left a lot":
        m = PyMouse()
        m.position()
        pos = m.position()
        m.move(pos[0] - 200, pos[1])

Ll = speech.listenfor(["Mouse Down", "Mouse all the way to the right", "Mouse all the way to the left", "Right Click", "Mouse to the left a little", "Double Click", "Mouse to the right a lot", "Mouse to the left a lot", "Mouse to the right a little", "Mouse Up", "Mouse down a little", "Mouse to the right", "Mouse Up a little", "Mouse to the left", "Click"], Get)
while Ll.islistening():
    time.sleep(.5)




