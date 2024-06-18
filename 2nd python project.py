import time
from plyer import notification
from tkinter import Tk, Label, Button, Entry

def set_resolution():
    resolution_text = entry.get()
    notification.notify(
        title="New Year's Resolution",
        message=resolution_text,
        timeout=10
    )

def start_bot():
    while True:
        set_resolution()
        time.sleep(3600)  # Send notification every hour (3600 seconds)

# GUI setup
root = Tk()
root.title("New Year's Resolution Bot")

label = Label(root, text="Enter your resolution:")
label.pack()

entry = Entry(root, width=50)
entry.pack()

button = Button(root, text="Set Resolution", command=start_bot)
button.pack()

root.mainloop()