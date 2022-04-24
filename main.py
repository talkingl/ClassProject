import tkinter as tk
from tkinter import ttk
from tkinter import *
import time


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        # label of frame Layout 2
        label = ttk.Label(self, text="Home Page", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.place(x=200, y=10)

        button1 = ttk.Button(self, text="Property Tax Calculator",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.place(x=5, y=100)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Income Calculator",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.place(x=5, y=150)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Property Tax Calculator", font=LARGEFONT)
        label1 = ttk.Label(self, text="Please enter your state to see your property tax rate")


        label.place(x=200, y=10)
        label1.place(x=200, y= 100)

        states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

        # setting variable for Integers
        self.variable = StringVar()
        self.variable.set(states[0])

        # creating widget
        self.dropdown = OptionMenu(
            self,
            self.variable,
            *states,
            command=self.display_selected
        )
        print(self.variable.get())
        self.dropdown_label = ttk.Label(self, text=f'{self.variable.get()}', font=LARGEFONT)
        self.dropdown_label.place(x=200, y=300)



        self.dropdown.pack(expand=True)
        self.dropdown.place(x=200, y=200)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Home Page",
                             command=lambda: controller.show_frame(StartPage))


        # putting the button in its place
        # by using grid
        button1.place(x=5, y=100)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Income Calculator",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.place(x=5, y=150)

    def display_selected(self, value):
        file_open = open("prng-service.txt", "w")
        file_open.write(f'{self.variable.get()}')
        file_open.close()
        file_open = open("prng-service.txt", "r")
        reader1 = file_open.readline()
        file_open.close()
        if reader1:
            tax_finder = open("tax-service.txt", "w")
            tax_finder.write(f"{reader1}")
            tax_finder.close()
            time.sleep(1)
        while True:
            file_open = open("tax-service.txt", "r")
            reader = file_open.readline()
            file_open.close()
            time.sleep(1)
            file_open = open("state-service.txt", "r")
            reader2 = file_open.readline()
            file_open.close()
            print(reader, reader2)
            if not reader:
                continue

            if reader:
                reader = str(float(reader) * 100) + "%"
                new_data = reader2 + " " + reader
                self.dropdown_label.destroy()
                self.dropdown_label = ttk.Label(self, text=new_data, font=LARGEFONT)
                self.dropdown_label.place(x=200, y=300)
                break


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.entry1 = tk.StringVar()
        self.entry2 = tk.StringVar()
        self.calculation = tk.StringVar()
        self.calculation.set(0)

        label = ttk.Label(self, text="Income Calculator", font=LARGEFONT)
        label1 = ttk.Label(self, text="Please enter you Revenue and Expenses to see your Income")
        label2 = ttk.Label(self, text="Income")
        label3 = ttk.Label(self, text="Expense")
        self.label4 = ttk.Label(self, text=f'{self.calculation.get()}')


        label.place(x=200, y=10)
        label1.place(x=200, y= 100)
        label2.place(x=200, y=175)
        label3.place(x=200, y=275)
        self.label4.place(x=200, y=450)


        entry = Entry(self, textvariable = self.entry1, width=40)
        entry.focus_set()
        entry.pack()
        entry.place(x=200, y=200)

        entry2 = Entry(self, textvariable = self.entry2, width=40)
        entry2.focus_set()
        entry2.pack()
        entry2.place(x=200, y=300)

        button3 = ttk.Button(self,text="Calculate Income and Taxes", command=self.calculate_income )
        button3.place(x=200, y=400)
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Property Tax Calculator",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.place(x=5, y=150)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Home Page",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.place(x=5, y=100)

    def calculate_income(self):
        self.label4['text'] = str(int(self.entry1.get()) - int(self.entry2.get()))



# Driver Code
app = tkinterApp()
app.geometry('700x700')
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=3)
app.mainloop()