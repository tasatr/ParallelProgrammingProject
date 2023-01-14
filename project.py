import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinterweb import HtmlFrame #import the HtmlFrame widget


class Example(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Parallel Programming Project")

        self.inputFrame = LabelFrame(self, padx=15, pady=15)
        self.inputFrame.grid(row=0, column=0)
        self.tb1 = Label(self.inputFrame, text="Input a URL").grid(row=0, column=0)
        self.e1 = Entry(self.inputFrame)
        self.e1.grid(row=0, column=1)

        self.b1 = Button(self.inputFrame, text="Show URL", command=lambda: self.url_entered(self.e1.get())).grid(row=0, column=2)


        # Displaying the frame1 in row 1 and column 0
        self.frame1 = LabelFrame(self, text="First Frame", fg="white", padx=15, pady=15)
        self.frame1.grid(row=1, column=0)
        self.firstFrame = HtmlFrame(self.frame1)  # create HTML browser
        self.firstFrame.load_html("<h1>Please enter a URL to see something!</h1>")
        #    firstFrame.load_website(e1.get())

        self.firstFrame.pack(side="top", expand=True)  # attach the HtmlFrame widget to the parent window
        self.firstFrame.pack()

        # Constructing the second frame, frame2
        self.frame2 = LabelFrame(self, text="Second Frame", padx=15, pady=15)

        # Displaying the frame2 in row 2 and column 0
        self.frame2.grid(row=2, column=0)
        self.secondFrame = HtmlFrame(self.frame2)  # create HTML browser
        # myhtmlframe.load_html("<h1>Hello, World!</h1>") #Load some HTML code
        self.secondFrame.load_website("courses.cs.ut.ee")
        self.secondFrame.pack(side="bottom", expand=True)  # attach the HtmlFrame widget to the parent window
        self.secondFrame.pack()


        # self.geometry("600x400")
        # self.current_ticket_number = 1
        # self.data = [[97, "Mike"], [98, "Kaite"], [99, "Tom"]]
        # self.display_frame = tk.Frame(self)
        # self.display_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")
        #
        # self.lbl1 = tk.Label(self, text="Next ticket number: {}".format(self.current_ticket_number))
        # self.lbl1.grid(row=0, column=0)
        # self.lbl2 = tk.Label(self, text="Customer Name: ".format(self.current_ticket_number))
        # self.lbl2.grid(row=0, column=1)
        # self.entry1 = tk.Entry(self)
        # self.entry1.grid(row=0, column=2)
        #
        # tk.Button(self, text="Refresh List", command=self.refresh).grid(row=1, column=0, pady=5)
        # tk.Button(self, text="Submit new ticket", command=self.new_ticket).grid(row=1, column=1, pady=5)

        #self.timed_refresh()

    def new_ticket(self):
        x = self.entry1.get().strip()
        if x != "":
            self.data.append([self.current_ticket_number, x])
            #self.refresh() # you could do self.refresh() here if you want to update as soon as you create a ticket
            #I left it out though so you can see how after() works below.
            if self.current_ticket_number >= 99:
                self.current_ticket_number = 1
            else:
                self.current_ticket_number += 1

    def refresh(self):
        self.display_frame.destroy()
        self.display_frame = tk.Frame(self)
        self.display_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")
        for ndex, item in enumerate(self.data):
            tk.Label(self.display_frame, text=r"Order #{} is ready for {}.".format(item[0], item[1])).grid(row=ndex, column=1)
            tk.Button(self.display_frame, text=r"Remove Ticket".format(item[0], item[1]), command=lambda x=ndex: self.remove_ticket(x)).grid(row=ndex, column=0)

    def remove_ticket(self, ndex):
        self.data.pop(ndex)
        self.refresh()

    def timed_refresh(self):
        #this after statement is set for every 6 seconds
        self.after(6000, self.url_entered(''))
        #self.refresh()

    def url_entered(self, pageUrl):
        self.reload_frame_2(pageUrl)


    def reload_frame_1(self, pageUrl):
        if (pageUrl):
            self.firstFrame.load_website(pageUrl)
            self.frame1.grid()
        else:
            self.firstFrame.load_html("<h1>Please enter a URL to see something!</h1>")
            self.frame1.grid()

    def reload_frame_2(self, pageUrl):
        if (pageUrl):
            self.secondFrame.load_website(pageUrl)
            self.frame2.grid()
        else:
            self.secondFrame.load_html("<h1>Please enter a URL to see something!</h1>")
            self.frame2.grid()

if __name__ == "__main__":
    Example().mainloop()