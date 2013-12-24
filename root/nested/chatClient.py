# Client
# TCP Client Code
from socket import *

from multiprocessing import Process, Value
#import threading
import tkMessageBox
from Tkinter import Tk

s = None

def gui(msg, n):
    root = Tk()
    root.withdraw()
    tkMessageBox.showinfo("Message from server", msg)
    #root.destroy()
    #s.send("Done")
    n.value = 1
    return

if __name__ == '__main__':
    num = Value('i', 0)
    threads = []

    #host = "127.168.2.75"
    host = "192.168.186.128"
    port = 4446                         # Sets the variable port to 4444
    s = socket(AF_INET, SOCK_STREAM)    # Creates a socket
    s.connect((host, port))             # Connect to server address

    while True:

        msg = s.recv(1024)                  # Receives data upto 1024 bytes and stores in variables msg
        msg = msg.strip().decode('ascii')
        print ("Message from server : " + msg)
        num.value = 0

        if msg == 'close':
            for p in threads:
                p.terminate()
            s.send("Popups closed successfully at client")
        elif msg == '' or msg == 'quit':
            break
        else:
            p = Process(target=gui, args=(msg, num))
            p.start()
            p.join(10)
            threads.append(p)
            #print num.value
            if num.value == 1:
                s.send("Client closed the popup")
            else:
                s.send("Client did not close the popup. Send 'close' to close it")

    s.close()                            # Closes the socket