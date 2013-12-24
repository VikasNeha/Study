import gui
from socket import *
# --- here goes your event handlers ---


def load(evt):
    #mywin.minimized = True
    host = "127.168.2.75"
    port = 4446                         # Sets the variable port to 4444
    s = socket(AF_INET, SOCK_STREAM)    # Creates a socket
    s.connect((host, port))             # Connect to server address

    # while True:
    #
    #     msg = s.recv(1024)                  # Receives data upto 1024 bytes and stores in variables msg
    #     print ("Message from server : " + msg.strip().decode('ascii'))
    #
    #     #s.send("Message received")
    #     # s = socket(AF_INET, SOCK_STREAM)
    #     # s.connect((host, port))
    #     mywin['label_211_281'].value = msg.strip().decode('ascii')
    #     mywin.minimized = False
    #
    #     s.send("ok")
    #
    #     # Closes the socket
    #     if msg.strip().decode('ascii') == 'quit':
    #         s.close()
    #         break

# --- gui2py designer generated code starts ---

#======== MAIN WINDOW ========#
gui.Window(name=u'ChatClient',
           title=u'ChatClient',
           maximize_box=False, resizable=False, height='400px', left='173',
           top='58', width='550px', bgcolor=u'#E0E0E0', fgcolor=u'#000000',
           )
gui.Label(id=281, name='label_211_281', height='17', left='50', top='40',
          width='254', transparent=True,
          font={'size': 9, 'family': 'sans serif', 'face': u'Arial'},
          parent=u'ChatClient',
          text=u'abcd', )

# --- gui2py designer generated code ends ---

# get a reference to the Top Level Window:
mywin = gui.get("ChatClient")

# assign your event handlers:
mywin.onload = load

if __name__ == "__main__":
    # myLogger.setupLogging()
    mywin.show()
    gui.main_loop()