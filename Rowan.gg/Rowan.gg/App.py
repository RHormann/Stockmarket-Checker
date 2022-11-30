import Server
import customtkinter as tk

class Gui:

    def __init__(self) -> None:
        pass

    def frontPage(self):
        app = tk.CTk()
        app.geometry("400x700")

        def button_function():
            name = entry.get()
            user = Server.Global(name)
            print(user.getData())
            page1.pack_forget()
            profile.pack()

        page1 = tk.CTkFrame(master=app)
        page1.pack()
        profile = tk.CTkFrame(master=app)
        button = tk.CTkButton(master=page1, text="Search", command=button_function)
        button.pack()
        entry = tk.CTkEntry(master=page1, width=200,height=28)
        entry.pack()
        test = tk.CTkLabel(master=profile, text= "Testing")
        test.pack()

        app.mainloop()

def runApp():
   UI = Gui()
   UI.frontPage()




