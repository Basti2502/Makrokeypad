from tkinter import *
import time

def buttonBerechnenClick():
    
    Key1 = (entryKey1.get())
    Key2 = (entryKey2.get())
    Key3 = (entryKey3.get())
    Key4 = (entryKey4.get())
    Key5 = (entryKey5.get())
    Key6 = (entryKey6.get())
    Key7 = (entryKey7.get())
    Key8 = (entryKey8.get())
    Key9 = (entryKey9.get())
    Key10 = (entryKey10.get())
    
    print(Key1)
    print(Key2)
    print(Key3)
    print(Key4)
    print(Key5)
    print(Key6)
    print(Key7)
    print(Key8)
    print(Key9)
    print("saved")
    
    if Key10 == "LOL":
        labelKey12 = Label(master=tkFenster, bg='#FE2EF7', text='TEST TEST')
        labelKey12.place(x=500, y=104, width=200, height=27)
    
    
    datei = open('key1.txt','w')
    datei.write(Key1)
    datei.close()
    
    datei = open('key2.txt','w')
    datei.write(Key2)
    datei.close()
    
    datei = open('key3.txt','w')
    datei.write(Key3)
    datei.close()
    
    datei = open('key4.txt','w')
    datei.write(Key4)
    datei.close()

    datei = open('key5.txt','w')
    datei.write(Key5)
    datei.close()
    
    datei = open('key6.txt','w')
    datei.write(Key6)
    datei.close()
    
    datei = open('key7.txt','w')
    datei.write(Key7)
    datei.close()
    
    datei = open('key8.txt','w')
    datei.write(Key8)
    datei.close()
    
    datei = open('key9.txt','w')
    datei.write(Key9)
    datei.close()
    

tkFenster = Tk()
tkFenster.title('BMI')
tkFenster.geometry('300x450')

labelKey1 = Label(master=tkFenster, bg='#FFCFC9', text='Key1:')
labelKey1.place(x=54, y=24, width=100, height=27)

entryKey1 = Entry(master=tkFenster, bg='white')
entryKey1.place(x=164, y=24, width=100, height=27)

labelKey2 = Label(master=tkFenster, bg='#FFCFC9', text='Key2:')
labelKey2.place(x=54, y=64, width=100, height=27)

entryKey2 = Entry(master=tkFenster, bg='white')
entryKey2.place(x=164, y=64, width=100, height=27)

labelKey3 = Label(master=tkFenster, bg='#FFCFC9', text='Key3:')
labelKey3.place(x=54, y=104, width=100, height=27)

entryKey3 = Entry(master=tkFenster, bg='white')
entryKey3.place(x=164, y=104, width=100, height=27)




labelKey4 = Label(master=tkFenster, bg='#FFCFC9', text='Key4:')
labelKey4.place(x=54, y=144, width=100, height=27)

entryKey4 = Entry(master=tkFenster, bg='white')
entryKey4.place(x=164, y=144, width=100, height=27)

labelKey5 = Label(master=tkFenster, bg='#FFCFC9', text='Key5:')
labelKey5.place(x=54, y=184, width=100, height=27)

entryKey5 = Entry(master=tkFenster, bg='white')
entryKey5.place(x=164, y=184, width=100, height=27)

labelKey6 = Label(master=tkFenster, bg='#FFCFC9', text='Key6:')
labelKey6.place(x=54, y=224, width=100, height=27)

entryKey6 = Entry(master=tkFenster, bg='white')
entryKey6.place(x=164, y=224, width=100, height=27)




labelKey1 = Label(master=tkFenster, bg='#E6E6E6', text='Made by: Basti_2502 & Namenlos112') #Secret
labelKey1.place(x=500, y=24, width=200, height=27)

entryKey10 = Entry(master=tkFenster, bg='white')
entryKey10.place(x=500, y=64, width=200, height=27)



labelKey7 = Label(master=tkFenster, bg='#FFCFC9', text='Key7:')
labelKey7.place(x=54, y=264, width=100, height=27)

entryKey7 = Entry(master=tkFenster, bg='white')
entryKey7.place(x=164, y=264, width=100, height=27)

labelKey8 = Label(master=tkFenster, bg='#FFCFC9', text='Key8:')
labelKey8.place(x=54, y=304, width=100, height=27)

entryKey8 = Entry(master=tkFenster, bg='white')
entryKey8.place(x=164, y=304, width=100, height=27)

labelKey9 = Label(master=tkFenster, bg='#FFCFC9', text='Key9:')
labelKey9.place(x=54, y=344, width=100, height=27)

entryKey9 = Entry(master=tkFenster, bg='white')
entryKey9.place(x=164, y=344, width=100, height=27)

buttonBerechnen = Button(master=tkFenster, bg='#FFFF00', text='save', command=buttonBerechnenClick)
buttonBerechnen.place(x=54, y=384, width=210, height=27)

tkFenster.mainloop()



