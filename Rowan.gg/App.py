import Server
import customtkinter as tk
import tkinter
import tkinter.font as font

class Gui:

    def __init__(self):
        self.app = tk.CTk()
        self.app.geometry("400x700")
        self.mainFrame = tk.CTkFrame(master=self.app,width=400,height=700)
        self.mainFrame.pack()
        
    def frontPage(self):

        def findUser():
            summonerName = entryBox.get()
            user = Server.Global(summonerName)
            mainFrame.place_forget()
            self.profilePage(user.getData())
        
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




    
    def keepOpen(self):
        self.app.mainloop()



def runApp():
   UI = Gui()
   UI.frontPage()
   UI.keepOpen()




