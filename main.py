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

scrollable_frame = customtkinter.CTkScrollableFrame(app, width=400, height=350)
scrollable_frame.pack(padx=10, pady=10)

app.mainloop()