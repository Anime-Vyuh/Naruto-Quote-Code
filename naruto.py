import tkinter as tk
from tkinter import Canvas, ttk
from PIL import Image,ImageTk
import pyttsx3 as ts
from iconic_dialouges import iconic_dialouges_naruto

root=tk.Tk()
root.geometry('810x600+255+50')
root.resizable(False,False)
root.title('Naruto Series Dialouges')
dialouges=ts.init()
voices = dialouges.getProperty('voices')
dialouges.setProperty('voice', 'english+f11')
newVoiceRate = 145
dialouges.setProperty('rate',newVoiceRate)

def dialouge(character):
    dialouges.say(iconic_dialouges_naruto[character])
    dialouges.runAndWait()
def Naruto():
    dialouge('Naruto')
def Sasuke():
    dialouge('Sasuke')
def Madara():
    dialouge('Madara')
def Itachi():
    dialouge('Itachi')
def Nagato():
    dialouge('Nagato')
def Kakashi():
    dialouge('Kakashi')
def Obito():
    dialouge('Obito')
def Jiraiya():
    dialouge('Jiraiya')
def Guy():
    dialouge('Guy')
def Lee():
    dialouge('Lee')
def Orochimaru():
    dialouge('Orochimaru')
def Pain():
    dialouge('Pain')
def Shikamaru():
    dialouge('Shikamaru')
def Gaara():
    dialouge('Gaara')
def Neji():
    dialouge('Neji')

def images(character):
    image = Image.open('images/{}.png'.format(character))
    image = image.resize((250, 250), Image.ANTIALIAS)
    return image

def main():
    frame=tk.Frame(root)
    frame.pack(fill="both",expand=1)

    canva = tk.Canvas(frame)
    canva.pack(side="left",fill="both",expand=1)

    scroll_bar = ttk.Scrollbar(frame,orient="vertical",command=canva.yview)
    scroll_bar.pack(side="right",fill="y")

    canva.configure(yscrollcommand=scroll_bar.set)
    canva.bind('<Configure>',lambda scroll:canva.configure(scrollregion=canva.bbox("all")))

    secondframe = tk.Frame(canva)
    canva.create_window((0,0),window=secondframe,anchor="n")

    naruto_img = ImageTk.PhotoImage(images('naruto'))
    sasuke_img = ImageTk.PhotoImage(images('sasuke'))
    itachi_img = ImageTk.PhotoImage(images('itachi'))
    madara_img = ImageTk.PhotoImage(images('madara'))
    jiraiya_img = ImageTk.PhotoImage(images('jiraiya'))
    obito_img = ImageTk.PhotoImage(images('obito'))
    guy_img =  ImageTk.PhotoImage(images('guy'))
    lee_img =  ImageTk.PhotoImage(images('rocklee'))
    orochi_img =  ImageTk.PhotoImage(images('orochimaru'))
    nagato_img =  ImageTk.PhotoImage(images('nagato'))
    pain_img =  ImageTk.PhotoImage(images('pain'))
    kakashi_img =  ImageTk.PhotoImage(images('kakashi'))
    neji_img =  ImageTk.PhotoImage(images('neji'))
    gaara_img =  ImageTk.PhotoImage(images('gaara'))
    shikamaru_img =  ImageTk.PhotoImage(images('shikamaru'))

    naruto=tk.Button(secondframe,image=naruto_img,command=Naruto,bg='yellow').grid(row=0,column=1,ipadx=5,ipady=5)
    sasuke=tk.Button(secondframe,image=sasuke_img,command=Sasuke,bg='blue').grid(row=0,column=2,ipadx=5,ipady=5)
    itachi=tk.Button(secondframe,image=itachi_img,command=Itachi,bg='orangered').grid(row=0,column=3,ipadx=5,ipady=5)
    madara=tk.Button(secondframe,image=madara_img,command=Madara,bg='black').grid(row=1,column=1,ipadx=5,ipady=5)
    orochi=tk.Button(secondframe,image=orochi_img,command=Orochimaru,bg='gray').grid(row=1,column=2,ipadx=5,ipady=5)
    obito=tk.Button(secondframe,image=obito_img,command=Obito,bg='violet').grid(row=1,column=3,ipadx=5,ipady=5)
    jiraiya=tk.Button(secondframe,image=jiraiya_img,command=Jiraiya,bg='white').grid(row=2,column=1,ipadx=5,ipady=5)
    kakashi=tk.Button(secondframe,image=kakashi_img,command=Kakashi,bg='purple').grid(row=2,column=2,ipadx=5,ipady=5)
    guy=tk.Button(secondframe,image=guy_img,command=Guy,bg='green').grid(row=2,column=3,ipadx=5,ipady=5)
    pain=tk.Button(secondframe,image=pain_img,command=Pain,bg='orange').grid(row=3,column=1,ipadx=5,ipady=5)
    nagato=tk.Button(secondframe,image=nagato_img,command=Nagato,bg='red').grid(row=3,column=2,ipadx=5,ipady=5)
    lee=tk.Button(secondframe,image=lee_img,command=Lee,bg='green').grid(row=3,column=3,ipadx=5,ipady=5)
    neji=tk.Button(secondframe,image=neji_img,command=Neji,bg='indigo').grid(row=4,column=1,ipadx=5,ipady=5)
    gaara=tk.Button(secondframe,image=gaara_img,command=Gaara,bg='brown').grid(row=4,column=2,ipadx=5,ipady=5)
    shikamaru=tk.Button(secondframe,image=shikamaru_img,command=Shikamaru,bg='skyblue').grid(row=4,column=3,ipadx=5,ipady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
