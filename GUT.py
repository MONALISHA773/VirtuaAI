from tkinter import*
from PIL import Image , ImageTk
import speechtotext
import action
root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#FFDAB9")

# ask fun
def ask():
    ask_val = speechtotext.speechtotext()
    bot_val= action.Action(ask_val)
    text.insert(END, 'User--->'+ask_val+"\n")
    if bot_val != None:
        text.insert(END,"Bot<---"+str(bot_val)+"\n")
    if bot_val=="ok sir":
        root.destroy()

def send():
    send= entry.get()
    bot=action.Action(send)
    text.insert(END,'User--->'+send+"\n")
    if bot!= None:
        text.insert(END,"Bot<---"+str(bot)+"\n")
    if bot=="ok sir":
        root.destroy()

   

def delete():
   text.delete('1.0',"end")
# frame

frame= LabelFrame(root, padx=100,pady=7, borderwidth=3 , relief="raised")
frame.config(bg="#FFDAB9")
frame.grid(row=0 , column=1, padx=55, pady=10)

# text lable

text_lable= Label(frame,text="AI Assistant" , font=("comic Sans ms" , 14, "bold") , bg="#D27D3F")
text_lable.grid(row=0, column=0, padx=20, pady=10)

# iamge

image = ImageTk.PhotoImage(Image.open("C:\\myproject\\basicproject\\VirualAI\\image\\assitant.png"))
image_label= Label(frame , image=image)
image_label.grid(row=1 , column=0 , pady=20 )

# adding a text widget
text= Text(root, font=('courier 10 bold'), bg="#D27D3F")
text.grid(row=2 , column=0)
text.place(x=100, y=375 , width=375 , height=100)
#entry widget

entry= Entry(root ,justify=CENTER)
entry.place(x=100, y=500, width=350 , height=30)

# button

Button1= Button(root , text="ASK" , bg="#D27D3F" ,pady=16 , padx=40 , borderwidth=3 , relief=SOLID, command=ask )
Button1.place(x=70 , y=575)

Button2= Button(root , text="Send" , bg="#D27D3F" ,pady=16 , padx=40 , borderwidth=3 , relief=SOLID, command=send )
Button2.place(x=400 , y=575)

Button3= Button(root , text="Delete" , bg="#D27D3F" ,pady=16 , padx=40 , borderwidth=3 , relief=SOLID, command=delete )
Button3.place(x=225 , y=575)



root.mainloop()
