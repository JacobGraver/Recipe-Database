import tkinter
import customtkinter

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Recipie Database")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="List of Recipes")
title.pack(padx=10, pady=10)

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # self.my_frame = MyFrame(master=self, width=300, height=200)
        # self.my_frame.grid(row=0, column=0, padx=20, pady=20)


app = App()

app.mainloop()