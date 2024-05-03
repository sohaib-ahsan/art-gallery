import tkinter as tk
from tkinter import *
from shutil import copy
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkinter.messagebox import askyesno
from mysql.connector import connect, Error


class ArtistView(tk.Frame):

    HomeUtils = [0,8,0]

    optionList = ['Home','My Profile', 'Search', 'Add Artwork', 'Log Out']
    artwork_DetailsUtil = ['Title', 'Year Made', 'Price', 'Genre', 'Likes']
    
    artImages = []
    rawImages = []
    my_img = []
    my_imgH = []
    
    Frames = {'Home':'', 'My Profile':'', 'Search':'', 'Add Artwork':'', 'Log Out' :''}
    picLabel = ''

    def __init__(self, parent, username):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.Username = username
        self.SQLloader()

        for i in self.optionList:
            image=Image.open('images\\'+i+'.png')
            img=image.resize((30, 30))
            self.my_img.append(ImageTk.PhotoImage(img))
   
            imageH=Image.open('images\\'+i+'H.png')
            imgH=imageH.resize((30, 30))
            self.my_imgH.append(ImageTk.PhotoImage(imgH))

            searchBar=Image.open('images\\searchbar.png')
            searchBar=searchBar.resize((650, 65))
            self.searchBar = ImageTk.PhotoImage(searchBar)

            img = Image.open(r'images\\logoH.png')
            self.resize_imagex = img.resize((180,115))
            self.logo = ImageTk.PhotoImage(self.resize_imagex)

        
        for i in range(len(self.ArtworkTitles)):
            image=Image.open('paintings\\'+str(i)+'.png')
            img=image.resize((212, 208))
            imgR=image.resize((400, 400))
            self.rawImages.append(ImageTk.PhotoImage(imgR))
            self.artImages.append(ImageTk.PhotoImage(img))

        self.MainScreen(parent)    
        pass


    def SQLconnection(self, query):
        try:
            with connect(
                host="localhost",
                user = 'root', 
                password = "Shan.9999",
                database = "art_gallery"
            ) as connection:
            
                with connection.cursor() as cursor: 
                    cursor.execute(query)
                    result = cursor.fetchall()
                    connection.commit()

                connection.close()
                return result

        except Error as error:
            print(error)
        pass


    def SQLloader(self):

        query1 = "Select * from artistInfo where user_name = \"" +self.Username+"\""
        artist_info = self.SQLconnection(query1)

        self.artist_info = {
            'Name':artist_info[0][0],
            'Email': artist_info[0][1],
            'Username': artist_info[0][2],
            'Phone':artist_info[0][3],
            'Category':'Artist', 
            'Genres':artist_info[0][4],
            'Artworks':artist_info[0][5], 
            'Sales':artist_info[0][6] 
            }

        query2 = "Select artwork.title from artwork ,artist where artwork.artist_id = artist.artist_id  and artist.user_name = \"" + self.Username +"\""
        titles = self.SQLconnection(query2)

        self.ArtworkTitles = [i[0] for i in titles]
        self._deficient = len(self.ArtworkTitles)
        
        pass


    def MainScreen(self, parent):
        parent.title('Artist Portal')
        self.leftFrame = tk.Frame(parent)
        self.leftFrame.config(bg='black', height=710, width=310)
        self.leftFrame.place(x=0, y=0, anchor='nw')
        
        for i in self.optionList:
            self.Frames[i] = tk.Frame(self.parent)
            self.Frames[i].config(bg='#181818', height=710, width=1100)
            self.Frames[i].place(x=300, y=0, anchor='nw')

        logoLabel = tk.Label(parent ,font = "Arial 25 bold" ,image=self.logo, width=175, height=110)
        logoLabel.place(x=40,y=15,anchor="nw")

        optionList = self.optionList
        self.imgLabels = {}
        OptionDict = {}

        def enteredOption(event):
            event.widget.config(cursor = 'hand2')
            idx = self.optionList.index(event.widget['text'])
            self.imgLabels[optionList[idx]].config(image =  self.my_imgH[idx])
            event.widget.config(fg='#8e47e0')

            
        def leaveOption(event):
            if(self.activePage != event.widget['text']):
                event.widget.config(fg='white')
                event.widget.config(cursor = 'arrow')
                idx = self.optionList.index(event.widget['text'])
                self.imgLabels[optionList[idx]].config(image =  self.my_img[idx])


        for i in range(len(optionList)):
            
            self.imgLabels[optionList[i]] = (Label(self.leftFrame, image = self.my_img[i], width = 20, height = 20))
            self.imgLabels[optionList[i]].place(x=15, y=(i*40)+160, anchor='nw')

            OptionDict[optionList[i]] = tk.Label(self.leftFrame)
            OptionDict[optionList[i]].config(text=optionList[i],
                                             bg='black', fg='white', font = 'Arial 11 bold')
            OptionDict[optionList[i]].place(x=50, y=(i*40)+160, anchor='nw')

            OptionDict[optionList[i]].bind("<Enter>", enteredOption)
            OptionDict[optionList[i]].bind("<Leave>", leaveOption)
        
        self.OptionDict = OptionDict

        OptionDict['Home'].bind("<Button>", self.HomeScreen)
        OptionDict['My Profile'].bind("<Button>", self.ProfileScreen)
        OptionDict['Search'].bind("<Button>", self.SearchScreen)
        OptionDict['Add Artwork'].bind("<Button>", self.NewArtworkScreen)
        OptionDict['Log Out'].bind("<Button>", self.LogOutScreen)

        #Active Page label to be purple always
        self.activePage = 'Home'
        OptionDict[self.activePage].config(fg='#8e47e0')
        self.imgLabels[self.activePage].config(image = self.my_imgH[optionList.index(self.activePage)])
        self.HomeScreen(event=None)
        # self.ProfileScreen(None)


    def raiseFrame(self, frame, text):
        frame.tkraise()
        self.greetings = Label(frame)
        self.greetings.config(text=text,font='Arial 25 bold', bg='#181818',fg='white')
        self.greetings.place(x=50, y=50, anchor='nw' )


    def shift_Focus(self, event):
        temp = self.activePage
        if event != None:
            self.activePage = event.widget['text']
        else:
            self.activePage = 'Home'
        if (self.activePage != temp):
            self.OptionDict[self.activePage].config(fg='#8e47e0')
            self.imgLabels[self.activePage].config(image = self.my_imgH[self.optionList.index(self.activePage)])
            self.OptionDict[temp].config(fg='white')
            self.imgLabels[temp].config(image = self.my_img[self.optionList.index(temp)])
    
    def EnteredButtons(self, event):
        event.widget['cursor'] = 'hand2'
        event.widget['bg'] = '#8357FF'

    def LeaveButtons(self, event):
        event.widget['cursor'] = 'arrow'
        event.widget['bg'] = '#6B37FA'

        
    def HomeScreen(self, event=None):
        self.shift_Focus(event)
        for i in self.Frames['Home'].winfo_children():
            i.destroy()
        self.raiseFrame(self.Frames['Home'], 'Home')  

        master = self.Frames['Home']

        self.yourWorkLabel = Label(master)
        self.yourWorkLabel.config(text=self.artist_info['Name'],font='Arial 15 bold', bg='#181818',fg='white')
        self.yourWorkLabel.place(x=55, y=115,anchor='nw')
        

        self.NextArtwork = Button(master,text=" > ",font='Arial 15 bold', relief='flat' ,bg='#6B37FA',fg='white', command=self.changeGridNext)
        self.NextArtwork.place(x=900, y=100,anchor='nw')

        self.PrevArtwork = Button(master,text=" < ",font='Arial 15 bold', relief='flat', bg='#6B37FA',fg='white',command=self.changeGridPrev)
        self.PrevArtwork.place(x=850, y=100,anchor='nw')
        
        self.NextArtwork.bind("<Enter>", self.EnteredButtons)
        self.PrevArtwork.bind("<Enter>", self.EnteredButtons)
        self.NextArtwork.bind("<Leave>", self.LeaveButtons)
        self.PrevArtwork.bind("<Leave>", self.LeaveButtons)

        def EnteredBoxes(event):
            event.widget['cursor'] = 'hand2'
            event.widget['bg'] = '#353535'
            for id in self.Boxes.keys():
                if self.Boxes[id] == event.widget:
                    self.ArtTitles[id].config(bg='#353535')

        def LeaveBoxes(event):
            event.widget['cursor'] = 'arrow'
            event.widget['bg'] = '#292929'
            for id in self.Boxes.keys():
                if self.Boxes[id] == event.widget:
                    self.ArtTitles[id].config(bg='#292929')

        self.Boxes = {}
        self.ArtTitles = {}
        self.Pictures = {}

        #self.HomeUtils = [start, end, _factor, prevStart]
        start = self.HomeUtils[0]
        end = self.HomeUtils[1]
        _factor = self.HomeUtils[2]

       
        for id in range(start, end):
            
            loopVar = id-(8*_factor)
            if (loopVar == self._deficient):
                break

            self.Boxes[id] = Frame(master, bg='#292929', width=230, height=250)
            if (loopVar<4):
                self.Boxes[id].place(x=(loopVar*245)+50, y=165, anchor='nw')
            else:
                self.Boxes[id].place(x=((loopVar-4)*245)+50, y=435, anchor='nw')

            self.Boxes[id].bind("<Enter>", EnteredBoxes)
            self.Boxes[id].bind("<Leave>", LeaveBoxes)
            
            self.Pictures[id] = tk.Label(self.Boxes[id])
            self.Pictures[id].config(image=self.artImages[id], width=208, height=204)
            self.Pictures[id].place(x=8,y=7,anchor='nw')

            self.Pictures[id].bind("<Button>",self.picDetailsZoomed)

            self.ArtTitles[id] = Label(self.Boxes[id], text=self.ArtworkTitles[id], bg='#292929',fg='white', font='Arial 11 bold')
            self.ArtTitles[id].place(x=110, y=232, anchor='center')
        pass


    def changeGridNext(self):
        prev = self.HomeUtils[0]
        self._deficient = len(self.ArtworkTitles) - (prev+8)

        if(self._deficient < 8):
            self.NextArtwork.config(state='disabled')

        if(self._deficient >= 1 ):
            self.HomeUtils = [prev+8, prev+16, (prev//8)+1 ]
            self.PrevArtwork.config(state='active')
            self.HomeScreen(None)

        pass
    
    def changeGridPrev(self):
        prev = self.HomeUtils[0]
        self._deficient = len(self.ArtTitles)
        if(prev == 0):
            self.PrevArtwork.config(state='disabled')

        if(prev >= 8):
            self.HomeUtils = [prev-8, prev, (prev//8)-1 ]
            self.NextArtwork.config(state='active')
            self.HomeScreen(None)
        pass

    
    def picDetailsZoomed(self, event=None, label=None):

        if label == None:
            for labelx in self.Pictures:
                if(event.widget ==self.Pictures[labelx]):
                    id = labelx
                    break
        else:
            id = self.ArtworkTitles.index(label)
        
        if label==None:
            master = self.Frames['Home']
            self.raiseFrame(self.Frames['Home'], 'Home')
            for i in self.Frames['Home'].winfo_children():
                i.destroy()
        else:
            master = self.Frames['Search']
            self.raiseFrame(self.Frames['Search'], 'Search')
            for i in self.Frames['Search'].winfo_children():
                i.destroy()
        
        picFrameLbl = Label(master, image = self.rawImages[int(id)])
        picFrameLbl.place(x=540, y=165, anchor='nw')

        self.goBack = Button(master,text=" Back",font='Arial 15 bold', relief='flat' ,
                             width=8, bg='#6B37FA',fg='white')
        self.goBack.place(x=70, y=70,anchor='nw')
        
        if label == None:
            self.goBack.config(command=self.HomeScreen)
        else:
            self.goBack.config(command=lambda:self.SearchScreen(None))
        

        self.goBack.bind("<Enter>", self.EnteredButtons)
        self.goBack.bind("<Leave>", self.LeaveButtons)


        title = Label(master, text=self.ArtworkTitles[int(id)])
        title.config(bg='#191919', fg='white', font='Arial 30 bold')
        title.place(x=60, y=200, anchor='nw')

    
        query3 = "Select title, year_made, price, categories.name, likes from artwork, categories where categories.category_id = artwork.category_id and artwork.title = \'"+ title['text']+"\'"
        artwork_info = self.SQLconnection(query3)

        self.artwork_Details = [i for i in artwork_info[0]]
      

        for i in range(1,len(self.artwork_DetailsUtil)):
            nameLabels = Label(master, text=self.artwork_DetailsUtil[i])
            nameLabels.config(bg='#191919', fg='white', font='Arial 15 bold')
            nameLabels.place(x=60, y=300+(i*40), anchor='nw')

            nameLabels = Label(master, text=self.artwork_Details[i])
            nameLabels.config(bg='#191919', fg='white', font='Arial 15 bold')
            nameLabels.place(x=200, y=300+(i*40), anchor='nw')
        

        query4 = 'Select artwork.art_id from sales,artwork where artwork.art_id = sales.art_id and artwork.title = \''+title['text']+"\'"
        checkforSale = self.SQLconnection(query4)
        
        if(len(checkforSale) == 0):

            deletePic = Button(master, text = 'Delete Artwork', font='Arial 15 bold', relief='flat' ,
                                width=15, bg='#E21313',fg='white', command = lambda:self.deleteArtwork(title['text']))
            deletePic.place(x=100, y=550,anchor='nw')

            def enterdel(event):
                event.widget['bg'] = '#B60808'
                event.widget['cursor'] = 'hand2'
            def leavedel(event):
                event.widget['bg'] = '#E21313'
                event.widget['cursor'] = 'arrow'

            deletePic.bind("<Enter>", enterdel)
            deletePic.bind("<Leave>", leavedel)
        
        else:
            soldLabel = Label(master, text = 'Sold!!', font='Arial 18 bold', relief='flat' ,
                                width=15, bg='#191919',fg='#00E9CB')
            soldLabel.place(x=100, y=550,anchor='nw')

        pass    


    def deleteArtwork(self, title):
        answer = askyesno(title='Confirmation',
                    message='Are you sure you want to delete?')
        if not answer:                    
            pass
        else:
            query5 = 'Delete from artwork where artwork.title=\''+title+'\''
            self.SQLconnection(query5)
            self.SQLloader()
            self.HomeScreen()


    def ProfileScreen(self, event):

        if(event!=None):
            self.shift_Focus(event)
        
        for i in self.Frames['My Profile'].winfo_children():
            i.destroy()
        
        self.raiseFrame(self.Frames['My Profile'], 'My Profile')
        master = self.Frames['My Profile']
        
        elems = ['Name','Username', 'Email', 'Phone', 'Category', 'Artworks' , 'Sales', 'Genres']

        for elem in range(len(elems)):
            self.nameLabel = Label(master, text=elems[elem])
            self.nameLabel.place(x=90, y=160+(40*elem), anchor='nw')

            self.artistLabel = Label(master, text=self.artist_info[elems[elem]])
            self.artistLabel.place(x=290, y=160+(40*elem), anchor='nw')

        for names in master.winfo_children():
            names.config(font="Arial 13 bold", fg='white', bg='#191919')

        self.greetings.config(font='Arial 25 bold', bg='#181818',fg='white')
        
        self.editProfileBtn = Button(master, text="Edit Profile", command=self.editProfileScreen)
        self.editProfileBtn.config(bg='#6B37FA', fg='white',font="Arial 13 bold", relief='flat', width=15, height=2)
        self.editProfileBtn.place(x=800, y=80, anchor='nw')
        self.editProfileBtn.bind('<Enter>', self.EnteredButtons)
        self.editProfileBtn.bind('<Leave>', self.LeaveButtons)
        pass


    def editProfileScreen(self):
        win = tk.Tk()
        win.geometry('%dx%d+%d+%d' % (700, 500, 350, 110))
        win.resizable(False,False)
        win.title('Edit Profile')
        win.config(bg='#212121')
        
        self.editLabel = Label(win, text='Edit Profile')
        self.editLabel.config(font="Arial 18 bold", fg='#D6CDFF', bg='#212121')
        self.editLabel.place(x=110, y=40, anchor='nw')

        self.getEntries = {}
        self.editElems = ['Name','Username', 'Password', 'Email', 'Phone']

        for elem in range(len(self.editElems)):
            self.nameLabel = Label(win, text=self.editElems[elem])
            self.nameLabel.config(font="Arial 13 bold", fg='white', bg='#212121')
            self.nameLabel.place(x=110, y=145+(40*elem), anchor='nw')

            tmp2 = tk.Label(win, width=41, bg='#8357FF')
            tmp2.place(x=260,y=146+(40*elem), anchor='nw')       

            self.getEntries[self.editElems[elem]] = tk.Entry(win, bd=0, font='Arial 12', fg='white',bg='#212121', insertbackground='white')
            self.getEntries[self.editElems[elem]].place(x=260,y=145+(40*elem),anchor="nw", width=300)
            if self.editElems[elem] != 'Password':
                self.getEntries[self.editElems[elem]].insert(END, self.artist_info[self.editElems[elem]])

            # self.getEntries[elems[elem]].set('wefwe')
       
        self.getDataBtn = Button(win, text="Update Data", command=lambda:self.updateData(win))
        self.getDataBtn.config(bg='#6B37FA', fg='white',font="Arial 13 bold", relief='flat', width=15, height=2)
        self.getDataBtn.place(x=260, y=400, anchor='nw')

        self.getDataBtn.bind('<Enter>', self.EnteredButtons)
        self.getDataBtn.bind('<Leave>', self.LeaveButtons)
        pass

        
            
    def updateData(self, win):
        self.updatedData = {}
        for elem in self.editElems:
            self.updatedData[elem] = self.getEntries[elem].get()
        
        if(self.dataValidity(win) == True):
            
            for elem in self.editElems:
                self.getEntries[elem].delete(0, 'end')
        
            query7 = 'Insert into user values(\''+self.updatedData['Username']+"\' ,  \'"+self.updatedData['Password']+"\' , \'Artist\')"
            self.SQLconnection(query7)

            query8 = 'Update artist set name= \''+self.updatedData['Name']+"\' ,user_name=\'"+self.updatedData['Username']+"\', email=\'"+ self.updatedData['Email']+"\', phone=\'"+self.updatedData['Phone']+"\' where user_name=\'"+self.Username+"\'" 
            self.SQLconnection(query8)

            query9 = "Delete from user where user_name=\'"+self.Username+"\'"
            self.SQLconnection(query9)

            self.sucTrans = Label(win, text='Successful Transaction!!')
            self.sucTrans.config(font='Arial 12 bold', bg='#212121', fg='#00A117')
            self.sucTrans.place(x=250, y=360,anchor='nw' )
            self.after(1200, win.destroy)

            self.Username = self.updatedData['Username']
            self.SQLloader()
            self.ProfileScreen(None)
        pass
    
    def dataValidity(self, win):

        if ('' in self.updatedData.values()):
            self.error = Label(win, text='Please Fill All Columns')
            self.error.config(font='Arial 12 bold', bg='#212121', fg='yellow')
            self.error.place(x=250, y=360,anchor='nw' )
            self.after(1000, self.error.destroy)

        elif len(self.updatedData['Password']) < 8:
            self.error = Label(win, text='Password should contain atleast 8 characters!')
            self.error.config(font='Arial 12 bold', bg='#212121', fg='yellow')
            self.error.place(x=250, y=360,anchor='nw' )
            self.after(1000, self.error.destroy)
            return False

        elif '@' not in self.updatedData['Email']:
            self.error = Label(win, text='Email should contain @ character!')
            self.error.config(font='Arial 12 bold', bg='#212121', fg='yellow')
            self.error.place(x=250, y=360,anchor='nw' )
            self.after(1000, self.error.destroy)
            return False

        elif (len(self.updatedData['Phone']) != 11 or not self.updatedData['Phone'].isnumeric()) :
            self.error = Label(win, text='Phone Number Not Valid!')
            self.error.config(font='Arial 12 bold', bg='#212121', fg='yellow')
            self.error.place(x=250, y=360,anchor='nw' )
            self.after(1000, self.error.destroy)
            return False
        
        query6 = 'Select user_name from user'
        InvalidUserNames = self.SQLconnection(query6)
        for i in InvalidUserNames:
            if(self.updatedData['Username'] == i[0]):
                self.error = Label(win, text='Username not available')
                self.error.config(font='Arial 12 bold', bg='#212121', fg='yellow')
                self.error.place(x=250, y=360,anchor='nw' )
                self.after(1000, self.error.destroy)
                return False
        
        else:
            return True


    def SearchScreen(self, event):
        if(event!=None):
            self.shift_Focus(event)
        else:
            self.activePage = 'Search'
            self.OptionDict[self.activePage].config(fg='#8e47e0')
            self.imgLabels[self.activePage].config(image = self.my_imgH[self.optionList.index(self.activePage)])

        master = self.Frames['Search']
        for i in master.winfo_children():
            i.destroy()
        
        self.raiseFrame(self.Frames['Search'], 'Search')

        def animation(event):
            def Mov(i):
                if(i<260):
                    self.searchBarLabel.place(x=185, y=300-i, anchor='nw')
                    self.searchEntry.place(x=230, y=320-i, anchor='nw')
                    self.after(1, lambda:Mov(i+1))
            Mov(0)
            self.searchEntry.unbind('<Button>')
            self.searchEntry.delete(0, 'end')
            self.searchEntry.config(fg='white')
            self.searchEntry.focus()


        self.searchBarLabel = Label(master, image=self.searchBar, height=60, width=645)
        self.searchBarLabel.place(x=185, y=300, anchor='nw')

        self.searchEntry = Entry(master, bd=0, fg='grey', bg='#181818', insertbackground='white',font="Arial 15 bold")
        self.searchEntry.place(x=230, y=320, anchor="nw", width=480)
        self.searchEntry.insert(END, 'Search your artworks...')
        self.searchEntry.bind("<Button>", animation)
        self.suggestionsframe = ''
        self.searchEntry.bind("<KeyRelease>",self.getSearchQuery)
        master.bind("<Return>", self.getSearchQuery)        
        pass


    def getSearchQuery(self, event):
        query = self.searchEntry.get()
        master = self.Frames['Search']

        if(type(self.suggestionsframe) != str):
            self.suggestionsframe.destroy()
        
        if (query != ''):
            query10 = 'Select title from artwork, artist where artist.user_name = \''+self.Username+'\' and artist.artist_id = artwork.artist_id and artwork.title like \'%'+query+'%\''
            artist_list = self.SQLconnection(query10)
            self.suggestions = []

            if len(artist_list) == 0:
                self.errorMessage = Label(self.Frames['Search'], text='No Results!')
                self.errorMessage.config(bg='#191919', fg='grey', font='Arial 15 bold')
                self.errorMessage.place(x=400, y=390, anchor='nw')
                self.Frames['Search'].after(1300, self.errorMessage.destroy)
        
            self.suggestionsframe = Frame(master, bg='#313131', width='300')
            self.suggestionsframe.place(x=260, y=100, anchor='nw')

            for i in range(len(artist_list)):
                self.suggestions.append(Label(self.suggestionsframe, text = artist_list[i][0], font='Arial 14 bold', bg='#313131', fg='white'))
                self.suggestions[i].pack()
                self.suggestions[i].bind("<Enter>", self.enterSug)
                self.suggestions[i].bind("<Leave>", self.LeaveSug)
                self.suggestions[i].bind("<Button>", self.ClickSug)


            def del_frame(event):
                master.focus()
                self.suggestionsframe.destroy()
                pass
            master.bind('<Button>', del_frame)     
        pass
    

    def enterSug(self, event):
        event.widget['bg'] = '#414141'
        event.widget['cursor'] = 'hand2'
        event.widget['fg'] = 'grey'
        pass

    def LeaveSug(self, event):
        event.widget['bg'] = '#313131'
        event.widget['cursor'] = 'arrow'
        event.widget['fg'] = 'white'
        pass

    def ClickSug(self, event):
        title = event.widget['text']
        self.searchEntry.delete(0, END)
        self.searchEntry.insert(END, title)
        self.picDetailsZoomed(label = title)
        pass

    def NewArtworkScreen(self, event):
        self.shift_Focus(event)
        self.raiseFrame(self.Frames['Add Artwork'], 'Add Artwork')

        master = self.Frames['Add Artwork']
        self.newArtworkEntries = {}

        for elem in range(len(self.artwork_DetailsUtil)-1):

            self.newArtLabel = Label(master, text=self.artwork_DetailsUtil[elem])
            self.newArtLabel.config(font="Arial 13 bold", fg='white', bg='#191919')
            self.newArtLabel.place(x=110, y=195+(40*elem), anchor='nw')

            tmp2 = tk.Label(master, width=41, bg='#8357FF')
            tmp2.place(x=260,y=196+(40*elem), anchor='nw')       

            self.newArtworkEntries[self.artwork_DetailsUtil[elem]] = tk.Entry(master, bd=0, 
                                font='Arial 12', fg='white',bg='#191919', insertbackground='white')
            self.newArtworkEntries[self.artwork_DetailsUtil[elem]].place(x=260,y=195+(40*elem),anchor="nw", width=300)

            # self.getEntries[elems[elem]].set('wefwe')
        
        self.chooseFileBtn = Button(master, text="Choose Image", command=self.choosePhoto)
        self.chooseFileBtn.config(bg='#6B37FA', fg='white',font="Arial 13 bold", relief='flat', width=13, height=2)
        self.chooseFileBtn.place(x=110, y=400, anchor='nw')

        self.addArtworkBtn = Button(master, text="Add Artwork", command = self.addArtworkToDatabase)
        self.addArtworkBtn.config(bg='#6B37FA', fg='white',font="Arial 13 bold", relief='flat', width=15, height=2)
        self.addArtworkBtn.place(x=460, y=550, anchor='nw')

        self.chooseFileBtn.bind('<Enter>', self.EnteredButtons)
        self.chooseFileBtn.bind('<Leave>', self.LeaveButtons)
        self.addArtworkBtn.bind('<Enter>', self.EnteredButtons)
        self.addArtworkBtn.bind('<Leave>', self.LeaveButtons)
        pass

    def choosePhoto(self):
        if type(self.picLabel) != str:
            self.picLabel.destroy()
        filetypes = (
            ('PNG files', '*.png'),
        )
        # show the open file dialog
        fname = fd.askopenfilename(title = 'Open a File', initialdir='/', filetypes=filetypes)
        self.src_path = str(fname)

        self.picLabel = Label(self.Frames['Add Artwork'], text=fname)
        self.picLabel.config(bg='#191919', fg='yellow', font='Arial 12 bold')
        self.picLabel.place(x=270, y=410, anchor='nw')
        pass


    def addArtworkToDatabase(self):
        artWorkDetailData = {}

        for elem in self.newArtworkEntries.keys():
                artWorkDetailData[elem] = self.newArtworkEntries[elem].get()
        
        if '' in artWorkDetailData.values():
            self.errorMessage = Label(self.Frames['Add Artwork'], text='Please Fill all Details!')
            self.errorMessage.config(bg='#191919', fg='red', font='Arial 12 bold')
            self.errorMessage.place(x=270, y=410, anchor='nw')
            self.Frames['Add Artwork'].after(1300, self.errorMessage.destroy)
            
        elif(type(self.picLabel) == str):
            self.errorMessage = Label(self.Frames['Add Artwork'], text='Please provide the Image!')
            self.errorMessage.config(bg='#191919', fg='red', font='Arial 12 bold')
            self.errorMessage.place(x=270, y=410, anchor='nw')
            self.Frames['Add Artwork'].after(1300, self.errorMessage.destroy)

        else:
            self.picLabel.destroy()
            for elem in self.newArtworkEntries.values():
                elem.delete(0,'end')
            
            self.success = Label(self.Frames['Add Artwork'], text='Artwork Added Successfully!')
            self.success.config(bg='#191919', fg='#00A117', font='Arial 12 bold')
            self.success.place(x=270, y=410, anchor='nw')

            self.after(1500, self.success.destroy)

            #Finding art_id
            query11 = 'Select max(art_id) from artwork'
            prev_id = self.SQLconnection(query11)
            art_id = int(prev_id[0][0])+1
            
            self.dst_path = r"paintings\\"+str(art_id)+".png"
            copy(self.src_path, self.dst_path)

            #Finding artist id
            query12 = 'Select artist_id from artist where user_name = \''+self.Username+"\'"
            artist_id = self.SQLconnection(query12)


            #Check the Category
            query13 = 'Select category_id from categories where name = \''+artWorkDetailData['Genre']+'\''
            categoryCheck = self.SQLconnection(query13)


            #if category doesnot exist, add one
            if len(categoryCheck) == 0:
                #getting Category id
                
                query14 = 'Select max(category_id) from categories'
                cat_id = self.SQLconnection(query14)
                
                categoryCheck = int(cat_id[0][0])+1

                query15 = "Insert into categories Values(\'"+str(categoryCheck)+"\',\'"+artWorkDetailData['Genre']+'\')'
                self.SQLconnection(query15)
            else:
                categoryCheck = categoryCheck[0][0]
            
            #Insert data in Database
            query16 = 'Insert into artwork values (\''+str(art_id)+"\',\'"+artWorkDetailData['Title']+"\' ,\'"+artWorkDetailData['Year Made']+"\',\'"+ artWorkDetailData['Price']+"\',\'"+str(artist_id[0][0])+"\',\'"+str(categoryCheck) +"\',0 )"
            self.SQLconnection(query16)


    def LogOutScreen(self, event):
        self.shift_Focus(event)
        self.raiseFrame(self.Frames['Log Out'], 'Log Out') 
        master = self.Frames['Log Out']

        frame = Frame(master, bg='#313131', width=600, height=300)
        frame.place(x=200,y=200,anchor='nw')
        askLabel = Label(frame, text='Are you sure you want to log out ?',bg='#313131', fg='white', font='Arial 14 bold')
        askLabel.place(x=40, y=50, anchor='nw')

        yes = Button(frame, text='Yes', fg='white',font='Arial 12 bold', bg='#6B37FA',height=2,width=15, command=exit)
        yes.place(x=135, y=180, anchor='nw')

        no = Button(frame, text='No', fg='white',font='Arial 12 bold', bg='#6B37FA',height=2,width=15, command=self.HomeScreen)
        no.place(x=305, y=180, anchor='nw')

        yes.bind("<Enter>", self.EnteredButtons)
        yes.bind("<Leave>", self.LeaveButtons)
        no.bind("<Enter>", self.EnteredButtons)
        no.bind("<Leave>", self.LeaveButtons)
        
        pass