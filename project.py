import tkinter as tk
from tkinter import *
from tkinterweb import HtmlFrame #import the HtmlFrame widget
import time
from threading import *
import random


lastFrame1LoadingTime = 0;
lastFrame2LoadingTime = 0;
pageUrl = '';

class PLProject(tk.Tk):
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
        self.firstFrame = HtmlFrame(self.frame1, messages_enabled = False)  # create HTML browser
        self.firstFrame.load_html("<h1>Please enter a URL to see something!</h1>")
        #    firstFrame.load_website(e1.get())

        self.firstFrame.pack(side="top", expand=True)  # attach the HtmlFrame widget to the parent window
        self.firstFrame.pack()

        # Constructing the second frame, frame2
        self.frame2 = LabelFrame(self, text="Second Frame", padx=15, pady=15)

        # Displaying the frame2 in row 2 and column 0
        self.frame2.grid(row=2, column=0)
        self.secondFrame = HtmlFrame(self.frame2, messages_enabled = False)  # create HTML browser
        self.secondFrame.load_website("courses.cs.ut.ee")
        self.secondFrame.pack(side="bottom", expand=True)  # attach the HtmlFrame widget to the parent window
        self.secondFrame.pack()

    def timed_refresh_frame1(self):
        self.firstFrame.after(60000, lambda: self.reset_first_frame());

    def timed_refresh_frame2(self):
        self.secondFrame.after(60000, lambda: self.reset_second_frame());

    def reset_first_frame(self):
        print("Resetting frame 1")
        global lastFrame1LoadingTime
        lastFrame1LoadingTime = 0
        self.firstFrame.load_html("<h1>Please enter a URL to see something!</h1>")
        self.frame1.grid()

    def reset_second_frame(self):
        print("Resetting frame 2")
        global lastFrame2LoadingTime
        lastFrame2LoadingTime = 0
        self.secondFrame.load_html("<h1>Please enter a URL to see something!</h1>")
        self.frame2.grid()

    def url_entered(self, pgUrl):
        global pageUrl #For some reason passing pageUrl as parameter inside Thread causes thread to wait
        pageUrl = pgUrl
        if (lastFrame1LoadingTime == 0 and lastFrame2LoadingTime == 0):
            print("Both frames are empty. Choosing a new frame at random.")
            frameToLoad = random.randint(0, 1)
            print(frameToLoad)
            if (frameToLoad == 0):
                t1 = Thread(target=self.reload_frame_1)
                t1.start()
                t2 = Thread(target=self.timed_refresh_frame1)
                t2.start()
            else:
                t3 = Thread(target=self.reload_frame_2)
                t3.start()
                t4 = Thread(target=self.timed_refresh_frame2)
                t4.start()
        elif (lastFrame1LoadingTime < lastFrame2LoadingTime):
            print("Loading in frame 1.")
            t5 = Thread(target=self.reload_frame_1)
            t5.start()
            t6 = Thread(target=self.timed_refresh_frame1)
            t6.start()
        else:
            print("Loading in frame 2.")
            t7 = Thread(target=self.reload_frame_2)
            t7.start()
            t8 = Thread(target=self.timed_refresh_frame2)
            t8.start()



    def reload_frame_1(self):
        global lastFrame1LoadingTime
        lastFrame1LoadingTime = time.time()
        if (pageUrl):
            self.firstFrame.load_website(pageUrl)
            self.frame1.grid()
        else:
            self.firstFrame.load_html("<h1>Please enter a URL to see something!</h1>")
            self.frame1.grid()

    def reload_frame_2(self):
        global lastFrame2LoadingTime
        lastFrame2LoadingTime = time.time()
        if (pageUrl):
            self.secondFrame.load_website(pageUrl)
            self.frame2.grid()
        else:
            self.secondFrame.load_html("<h1>Please enter a URL to see something!</h1>")
            self.frame2.grid()

if __name__ == "__main__":
    PLProject().mainloop()