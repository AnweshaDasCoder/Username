from tkinter import *
root =Tk()
root.geometry("500x300")
root.configure(background="lightblue")

label_show_name["text"] = "Name: " + self.username
btn2.place(relx=0.5, rely=0.1, anchor=CENTER)
label_password["text"] = "Password: " + self.password
label2.place(relx=0.5, rely=0.3, anchor=CENTER)
label_captcha["text"] = "Captch: " + self.captcha
label_captcha.place(relx=0.5, rely=0.5, anchor=CENTER)
btn = Button(root, font=("Yu Gothic Light", 14, "bold"), text="Update Login Details", command = update)
btn.place(relx=0.5, rely=0.7, anchor=CENTER)
password= input("")
name = input("")

def update():
    user.username=input_name.get
    user.password=input_password.get

self.username = "James"
self.password = "gregory"
self.captcha = "2wtgdy782uh"
root.mainloop()