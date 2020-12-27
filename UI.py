import tkinter
from tkinter import *
from tkinter import messagebox
import json
data = json.load(open("data.json"))


window = Tk()
window.title("Find Your Words Here!")


def search():
  val = word_value.get()
  val = val.lower()
  
  if val in data:
          display_text.insert(END,data[val])
          word = val.capitalize()
          messagebox.showinfo("Meaning of "+word+": ",data[val])
          print(data[val])
  elif val == "":
    messagebox.showwarning("Warning","Enter word")
    
  elif val == " ":
    messagebox.showerror("Warning","You entered no word")


  else:
     display_text.insert(END,"This mini dictionary has no word like you want. AS you Entered wrong word ")
     messagebox.showerror("Warning","This mini dictionary has no word like you want . AS you Entered wrong want")

  display_text.delete("1.0", "end")





window.geometry('300x500')
window.configure(background = "green yellow")


head = Label(window ,text = "MINI DICTIONARY",bg = "black",fg = "green yellow",height = 4,width = 400,pady= 0,font = ("bold",16)) #for displaying the message
head.place(relx=0.5, rely=0.1,anchor=CENTER)


word = Label(window,text = "Enter the word you want the meaning off:",bg = "green yellow",font = ("bold",12))
word.place(relx = 0.5,rely = 0.3,anchor=CENTER)


word_value = Entry(window,width = 30)
word_value.place(relx = 0.5,rely = 0.37,anchor = CENTER)

#this is the button which will search the value
search = Button(window ,text="Search",bg = "black",fg = "green yellow",padx = 6 ,pady  =3 ,width= 13,command=search) #submit button
search.place(relx=0.5,rely=0.5,anchor=CENTER)


display=Label(window,text = "Your Word Means ",fg = "black",bg = "green yellow",font = ("bold",12))
display.place(relx = 0.5,rely = 0.74,anchor = CENTER)


display_text = Text(window,height = 6,width=38,bg = "black",fg = "green yellow",font = ("bold",11))
display_text.place(relx = 0.5,rely = 0.9,anchor = CENTER)

window.mainloop()
