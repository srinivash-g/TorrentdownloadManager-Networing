from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter as tk
import socket
server="127.0.0.1"
port=8080
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((server,port))

root=Tk()
root.title("Torrent Download Manager")
root.geometry('700x400+300+200')
root.resizable(False,False)
root.configure(bg="#326273")

def submit():
        tm=TM_combobox.get()
        if tm=='Torrent File':
          client.send(str(tm).encode('utf8'))  
          tname=Torrentnamevalue.get()
          client.send(str(tname).encode('utf8'))
          name=client.recv(1024)
          Filenamevalue.set(name.decode())
          
        if tm=='Magnet Link':            
           #mlink=MagnetlinkEntry.get(1.0,END)
            client.send(str(tm).encode('utf8')) 
            mlink=Magnetlinkvalue.get()
            client.send(str(mlink).encode('utf8'))
            name=client.recv(1024)
            Filenamevalue.set(name.decode())
        

        

        messagebox.showinfo('info','Download getting started!')
     


def clear():
        Torrentnamevalue.set(' ')
        Magnetlinkvalue.set(' ')
        Filenamevalue.set(' ')
        #MagnetlinkEntry.delete(1.0,END)
        
        

#logo
icon_image=PhotoImage(file="CIT_logo.png")
root.iconphoto(False,icon_image)

#heading
Label(root,text="Please Fill out this Entry:",font="arial 13",bg="#326273",fg="#fff").place(x=20,y=20)

#Label
Label(root,text="Download Method:",font=23,bg="#326273",fg="#fff").place(x=50,y=60)
Label(root,text="Torrent File Name:",font=23,bg="#326273",fg="#fff").place(x=50,y=110)
Label(root,text="Magnet Link:",font=23,bg="#326273",fg="#fff").place(x=50,y=160)
Label(root,text="File Name:",font=23,bg="#326273",fg="#fff").place(x=50,y=210)

#Entry
Torrentnamevalue=StringVar()
Magnetlinkvalue=StringVar()
Filenamevalue=StringVar()
#Torrent or Magnet
TM_combobox=Combobox(root,values=['Torrent File','Magnet Link'],font='arial 14',state='r',width=14)
TM_combobox.place(x=250,y=60)

TorrentnameEntry= Entry(root,textvariable=Torrentnamevalue,width=37,bd=2,font=20)
MagnetlinkEntry= Entry(root,textvariable=Magnetlinkvalue,width=37,bd=2,font=20)
FilenameEntry= Entry(root,textvariable=Filenamevalue,width=37,bd=2,font=20)
#MagnetlinkEntry=Text(root,width=50,height=4,bd=4)



TorrentnameEntry.place(x=250,y=110)
MagnetlinkEntry.place(x=250,y=160)
FilenameEntry.place(x=250,y=210)

Button(root,text="Submit",bg="#326273",fg="white",width=15,height=2,command=submit).place(x=200,y=300)
Button(root,text="Clear",bg="#326273",fg="white",width=15,height=2,command=clear).place(x=340,y=300)
Button(root,text="Exit",bg="#326273",fg="white",width=15,height=2,command=lambda:root.destroy()).place(x=480,y=300)

root.mainloop()
