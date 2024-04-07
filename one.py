from tkinter import *
import tkinter as tk
class Application(tk.Tk):
    def __init__(self, *args):
        super().__init__(*args)
        
        self.main_page()
        
        
    def main_page(self):
        self.clear_screen() 
        
        self.l1 = tk.Label(self, text="Main Page")
        self.b1 = tk.Button(self, text="Go to Page One", command=self.page_one)
        
        self.l1.pack()
        self.b1.pack()

        
    def page_one(self):
        self.clear_screen()
        pressed = 'Thanks for pressing the button on the previous screen!'

        self.did_he_press = tk.StringVar(self, value=':(\nWhy didnt you press the button on the previous screen?\n:(')

        self.l2 = tk.Label(self,text="Page One")
        self.b2 = tk.Button(self, text="Press this Button!",command=lambda: self.did_he_press.set(pressed))
        self.b3 = tk.Button(self, text="Go to Page Two", command= lambda: self.page_two(self.did_he_press.get())) 
        
        self.l2.pack()
        self.b2.pack()
        self.b3.pack()
        
    def page_two(self, exampleInput):
        self.clear_screen()
        self.l3 = tk.Label(self, text="Page Two")
        self.l4 = tk.Label(self, text=exampleInput)
        self.b4 = tk.Button(self,text="Back to previous page",command=self.page_one)
        self.b5 = tk.Button(self,text="Return to Home",command=self.main_page)
        
        self.l3.pack()
        self.l4.pack()
        self.b4.pack()
        self.b5.pack()
        
    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

app = Application()
app.mainloop()