from slrp_module import *
from tkinter import *
from PIL import Image, ImageTk


class Window(Tk):

    def __init__(self):
        super().__init__()
        self.minsize(768, 768)
        self.title("AFPC Database updater")
        self.load_widgets()

    def load_widgets(self):
        button_next = Button(self, text="Filter SLRP", bg="black", font=("Ariel", 20, "bold"), fg="white",
                             command=getCopySLRPReport)
        button_next.place(relx=0.25, rely=.95, anchor="s")
        exit_button = Button(self, text='Quit!', bg="black", fg="white", font=("Ariel", 20, "bold"),
                             command=lambda: self.destroy())
        exit_button.place(relx=.75, rely=.95, anchor="s")






