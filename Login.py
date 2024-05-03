import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
#import maskpass

from mysql.connector import connect, Error

from Artist import ArtistView
from customer import CustomerView

class ArtGallery:
    pass
class LoginPage(tk.Frame,ArtGallery):
    
    cred = []
    access = False

    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.parent = parent
        img = Image.open(r'images\\painter.png')
        self.resize_imagex = img.resize((500,500))
        self.imgx = ImageTk.PhotoImage(self.resize_imagex)

        img = Image.open(r'images\\logo.png')
        self.resize_imagex = img.resize((300,189))
        self.logo = ImageTk.PhotoImage(self.resize_imagex)

        self.Login(parent)
        
        
    def mySql(self, username, password):        
        try:
            with connect(
                host="localhost",
                user = 'root', 
                password = "Shan.9999",
                database = "art_gallery"
            ) as connection:
            
                with connection.cursor() as cursor: 
                    cursor.execute("Select * from user")
                    result = cursor.fetchall()
                    
                    for elem in result:
                        if (elem[0] == username and elem[1] == password):
                                self.Category = elem[2]
                                connection.close()
                                return True                
                    return False        
        except Error as error:
            print(error)


    def Login(self, parent):

        self.ArtGalLabel = tk.Label(parent, bg = 'white' ,font = "Arial 25 bold" ,image=self.logo)
        self.ArtGalLabel.place(x=220,y=20,anchor="nw")

        self.userLabel = tk.Label(parent, bg = 'white' ,font = "Arial 13" ,text="Username")
        self.userLabel.place(x=200,y=280,anchor="nw")

        self.passLabel = tk.Label(parent, bg = 'white' ,font = "Arial 13" ,text="Password")
        self.passLabel.place(x=200,y=320,anchor="nw")

        # Background purple labels
        tmp = tk.Label(parent, width=29, bg='purple')
        tmp.place(x=300,y=280, anchor='nw')

        tmp2 = tk.Label(parent, width=29, bg='purple')
        tmp2.place(x=300,y=320, anchor='nw')       

        self.userEntry = tk.Entry(parent, bd=0, font = 'Arial 12')
        self.userEntry.place(x=300,y=280,anchor="nw", width=210)

        self.passEntry = tk.Entry(parent, bd=0, show = "*", font= 'Arial 12')
        self.passEntry.place(x=300,y=320,anchor="nw", width =210)     

        self.submitBtn = tk.Button(parent, text = "Submit", font = "Arial 12 bold",
                             bg="purple", fg="white", width=30,
                             command = lambda:self.submit(parent, event=None))
        self.submitBtn.place(x=202,y=410,anchor="nw")

        tmp3 = tk.Label(parent, width=1, height=40, bg='purple')
        tmp3.place(x=750,y=45, anchor='nw')

        tmp4 = tk.Label(parent, width=1, height=40, bg='white')
        tmp4.place(x=752,y=45, anchor='nw')


        label = tk.Label(parent, image=self.imgx, width=496, height=490)
        label.place(x=800, y=100, anchor='nw')

  
        def entersub(event):
            event.widget.config(cursor="hand2")
            # submitBtn.config(bg = "#4754FA")
            event.widget.after(100, event.widget.config(fg = "#E3E3F3"))

        def leavesub(event):
            event.widget.config(cursor="arrow")
            event.widget.config(bg = "purple")
            event.widget.after(100, event.widget.config(fg = "white"))


        self.submitBtn.bind("<Enter>", entersub)
        self.submitBtn.bind("<Leave>", leavesub)

        # self.bind("<Return>", self.submit(parent, event=None))

        # self.signUpBtn(parent)


    def submit(self, parent, event):
        password = self.passEntry.get()
        username = self.userEntry.get()


        self.passEntry.delete(0, 'end')
        self.userEntry.delete(0, 'end')

        LoginPage.cred = [username, password]
        auth = LoginPage.mySql(self,LoginPage.cred[0], LoginPage.cred[1])
        
        if(auth == True):
            self.access = True
            show_frame(self,self.Category, username)
            
        else:
            warning = tk.Label(parent, text = "Invalid Credentials ! Try Again", font="Arial 10 bold", bg="white", fg="red")
            warning.place(x=260, y=365, anchor='nw')
            parent.after(1500, warning.destroy)
                
        

    def signUpBtn(self,parent):
        win = parent
        signLabel = tk.Label(parent, bg = "white", fg = "purple", text="Sign Up", font="Arial 10 bold")
        signLabel.place(x=200, y=240, anchor='nw')

        def enterSign(event):
            event.widget.config(cursor = "hand2")
            event.widget.config(font = "Arial 10 bold underline")
        def LeaveSign(event):
            event.widget.config(cursor = "arrow")
            event.widget.config(font = "Arial 10 bold")
        def ClickSign(event):
            self.signUp(parent)

        signLabel.bind("<Enter>", enterSign)
        signLabel.bind("<Leave>", LeaveSign)
        signLabel.bind("<Button-1>", ClickSign)
        
    def signUp(self):
        parent = self.win
        parent.title("Sign Up")
        frame1 = tk.Frame(self.win, height=300, width=300, bg='white')
        frame1.place(x=0, y=0, anchor='nw')
        
        userLabel = tk.Label(frame1, bg = 'white' ,font = "Arial 11" ,text="Username")
        userLabel.place(x=35,y=80,anchor="nw")

        passLabel = tk.Label(frame1, bg = 'white' ,font = "Arial 11" ,text="Password")
        passLabel.place(x=35,y=120,anchor="nw")


class ArtGallery:
    def __init__(self):
        self.root = tk.Tk()
        
        width = 1100
        height = 600
        self.root.title("Login Page")

        global screen_height, screen_width
        screen_width = self.root.winfo_screenwidth()  # Width of the screen
        screen_height = self.root.winfo_screenheight() # Height of the screen

        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2) - 30

        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.state("zoomed")
        self.root.config(bg="white")
        
        show_frame(self, 1)


def show_frame(self, category, username=None):
    if category == 1:
        LoginPage(self.root)
    if category == 'Artist':
        ArtistView(self.parent, username)
    if category == 'Customer':
        CustomerView(self.parent, username)
    

art = ArtGallery()
art.root.mainloop()
