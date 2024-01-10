from slrp_module import *
from tkinter import *

class Window(Tk):

    def __init__(self):
        super().__init__()
        self.minsize(568, 568)
        self.title("AFPC Database tool")
        self.resizable(width=True, height=True)

    def load_start_frame(self):
        bg = PhotoImage(file=fr'{root}\images\AFPC.png')
        bgLabel = Label(image=bg, width=568, height=568)
        bgLabel.image = bg
        bgLabel.place(y=0, x=0, width=568, height=568)
        button_next = Button(self, text="options", bg="black", font=("Ariel", 20, "bold"), fg="white",
                             command=lambda: self.load_options_frame())
        button_next.place(relx=0.25, rely=.96, anchor="s")
        exit_button = Button(self, text='Quit!', bg="black", fg="white", font=("Ariel", 20, "bold"),
                             command=lambda: self.destroy())
        exit_button.place(relx=.75, rely=.95, anchor="s")

    def load_options_frame(self):
        for i in self.place_slaves():
            i.destroy()
        bg = PhotoImage(file=fr'{root}\images\AFPC.png')
        bgLabel = Label(image=bg, width=568, height=568)
        bgLabel.image = bg
        bgLabel.place(y=0, x=0, width=568, height=568)
        button_SLRP = Button(self, text="SLRP Filter", bg="black", font=("Ariel", 20, "bold"), fg="white",
                             command=lambda: filterSLRP())
        button_SLRP.place(relx=0.25, rely=.96, anchor="s")
