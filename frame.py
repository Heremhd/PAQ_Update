from slrp_module import *
from tkinter import *

global bg


class Window(Tk):

    def __init__(self):
        super().__init__()
        self.minsize(768, 768)
        self.title("AFPC Database tool")
        self.load_widgets()
        self.resizable(width=False, height=False)

    def load_widgets(self):
        bg = PhotoImage(file=r'C:\Users\Aiden\PycharmProjects\PAQ_Update\images\AFPC.png')
        bgLabel = Label(image=bg, width=768, height=768)
        bgLabel.image = bg
        bgLabel.place(y=0, x=0, width=768, height=768)
        button_next = Button(self, text="Filter SLRP", bg="black", font=("Ariel", 20, "bold"), fg="white",
                             command=getCopySLRPReport)
        button_next.place(relx=0.25, rely=.95, anchor="s")
        exit_button = Button(self, text='Quit!', bg="black", fg="white", font=("Ariel", 20, "bold"),
                             command=lambda: self.destroy())
        exit_button.place(relx=.75, rely=.95, anchor="s")
