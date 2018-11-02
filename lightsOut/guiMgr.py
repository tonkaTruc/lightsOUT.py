from tkinter import *
import streamMgr

def sendSenderCreate():
    deviceValue=deviceValueButton.get()
    noOfSenders=noOfSendersButton.get()

    streamMgr.create_new_sender(deviceValue, noOfSenders)

    """
    StreamMgr.create_new_sender needs to request the specific Json 
    data within itself so passing as first arg is not required
    
    """
def buildUI():
    root = Tk()

    deviceValueButton = Entry(root, text="Enter Device ID")
    deviceValueButton.place(x=50, y=25)
    deviceValueButton.pack()
    deviceValueButton.bind("<Return>")

    noOfSendersButton = Entry(root, text="Enter number of senders")
    noOfSendersButton.pack()

    createSourceButton = Button(root, text="Create Source", command=sendSenderCreate)
    createSourceButton.pack(fill=X)

    root.mainloop()

if __name__ == "__main__":
    buildUI()