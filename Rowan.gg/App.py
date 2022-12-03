import Server
import customtkinter as tk
import tkinter
from tkinter import *
import tkinter.font as font
import champIcons
import os
from PIL import Image, ImageTk

class Gui:

    def __init__(self):
        self.app = tk.CTk()
        self.app.geometry("400x700")
        self.mainFrame = tk.CTkFrame(master=self.app,width=400,height=700)
        self.mainFrame.pack()
        self.frontPage()

    def frontPage(self):

        def findUser():
            summonerName = entryBox.get()
            user = Server.Global(summonerName)
            mainFrame.place_forget()
            try:
                self.profilePage(user.getData())
            except:
                self.championProfile(summonerName)
        
        def openSidebar():
            pass

        mainFrame = tk.CTkFrame(master=self.mainFrame,width=400,height=700)
        mainFrame.place(relx=0,rely=0)

        titleFrame = tk.CTkFrame(master=mainFrame,width=400,height=250)
        titleFrame.place(x=0,y=0)
        title = tk.CTkLabel(master=titleFrame, text="lolStats")
        title.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
        sidebar = tk.CTkButton(master=titleFrame,text="",width=30,height=30,command=openSidebar)
        sidebar.place(relx=0.1,rely=0.12,anchor=tkinter.CENTER)

        lookupBoxFrame = tk.CTkFrame(master=mainFrame, width=400,height=450)
        lookupBoxFrame.place(x=0,y=250)
        entryBox = tk.CTkEntry(master=lookupBoxFrame,width=250)
        lookupButton = tk.CTkButton(master=lookupBoxFrame,command=findUser,width=30,height=30,text="go")
        entryBox.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)
        lookupButton.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)
    
    def profilePage(self,userData):

        def openSidebar():
            pass

        def findUser():
            summonerName = entryBox.get()
            user = Server.Global(summonerName)
            mainFrame.place_forget()
            self.profilePage(user.getData())

        #Header
        basic = userData[0]
        level = basic["level"]
        mainFrame = tk.CTkFrame(master=self.app,height=700,width=400)
        mainFrame.place(relx=0,rely=0)
        titleFrame = tk.CTkFrame(master=mainFrame,width=400,height=150)
        titleFrame.place(relx=0,rely=0)
        sidebar = tk.CTkButton(master=titleFrame,text="",width=30,height=30)
        sidebar.place(relx=0.1,rely=0.19,anchor=tkinter.CENTER)
        entryBox = tk.CTkEntry(master=titleFrame,width=100)
        entryBox.place(relx=0.8,rely=0.19,anchor=tkinter.CENTER)
        lookupButton = tk.CTkButton(master=titleFrame,command=findUser,width=30,height=20,text="")
        lookupButton.place(relx=0.80,rely=0.38,anchor=tkinter.CENTER)
        username = tk.CTkLabel(master=titleFrame,text=basic["username"])
        username.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        level = tk.CTkLabel(master=titleFrame, text=f"Level: {level}")
        level.place(relx=0.5, rely=0.8, anchor= tkinter.CENTER)

        #Mastery
        mastery = userData[1]
        masteryFrame = tk.CTkFrame(master=mainFrame, width=175, height=250)
        masteryFrame.place(relx= 0.75,rely=0.45, anchor=tkinter.CENTER)
        for i in range(5):
            def findMasteryLength(champPoints):
                champ = mastery[0]
                maxChampPoints = champ["Mastery Points"]
                maxChampPoints = int(maxChampPoints)
                champPoints = int(champPoints)
                length = champPoints / maxChampPoints * 115
                return length
            champ = mastery[i]
            champName = champ["Champion Name"]
            champPoints = champ["Mastery Points"]
            image2 = ImageTk.PhotoImage(Image.open(f"{str(os.getcwd())}/Rowan.gg/champIcons/{champName}.png").resize([32,32]), Image.ANTIALIAS)
            y = 0.1 + (i*0.2)
            championFrame = tk.CTkFrame(master=masteryFrame,width=170,height=45)
            championFrame.place(relx=0.5,rely=y,anchor = tkinter.CENTER)
            champImage = tk.CTkButton(master=championFrame,width=35,height=35,image=image2,command=self.championProfile(champName),text="")
            champImage.place(relx=0.15,rely=0.475, anchor=tkinter.CENTER)
            masteryBar= tk.CTkFrame(master=championFrame, width = findMasteryLength(champPoints), height=15,fg_color="blue")
            masteryBar.place(relx=0.30,rely=0.07)
            champPointsLabel = tk.CTkLabel(master=championFrame,text=champPoints,width=75,height=15)
            champPointsLabel.place(rely=0.75, relx=0.55, anchor=tkinter.CENTER)


        #Ranked
        rankedFrame = tk.CTkFrame(master=mainFrame, width=175, height=250)
        rankedFrame.place(relx= 0.25,rely=0.45, anchor=tkinter.CENTER)

        #Match History
        historyFrame = tk.CTkFrame(master=mainFrame, width=350, height=220)
        historyFrame.place(relx= 0.5, rely= 0.82, anchor=tkinter.CENTER)
    
    def championProfile(self,champname):
        pass
        
    def keepOpen(self):
        self.app.mainloop()



def runApp():
   UI = Gui()
   UI.keepOpen()




