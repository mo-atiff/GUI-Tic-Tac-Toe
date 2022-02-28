from tkinter import *
from tkinter import messagebox
import random
import time
import winsound

root = Tk()
root.geometry('1500x800')

can = Canvas(root, height=800, width=1500, bg='black')
can.pack()

count = 1
ccount = 1

def name_entry():
    def goplayer2():
        if len(pvar2.get())!=0:
            can3.destroy()
            player2.destroy()
            player2but.destroy()
            lst.append(pvar2.get())
            global choice, letsgo, select, Random
            Random = random.choice(lst)
            start_but.destroy()
            select = can.create_text(1050, 100, text=f'{Random.upper()} Select Any-Of One', font='comicsansms 15 bold', fill='white')  #650
            choice()
            letsgo = Button(root, text="LET'S GO", font='comicsansms 13 bold', bd=8, fg='red', bg='#FFD39B', command=Boarddisp)
            letsgo.place(x='985', y='315')

        else:
            messagebox.showerror('ERROR', 'Player-2 Enter Your Name !!! This is Mandatory')

    def goplayer1():
        if len(pvar1.get())!=0:
            global lst
            can2.destroy()
            player1.destroy()
            player1but.destroy()
            lst = [pvar1.get()]
        else:
            messagebox.showerror('ERROR', 'Player-1 Enter Your Name !!! This is Mandatory')

    new_root = Toplevel(root)
    new_root.title('PLAYER-1')
    can2 = Canvas(new_root, height=70, width=250, bg='black')
    can2.pack()

    new_root2 = Toplevel(root)
    new_root2.title('PLAYER-2')
    can3 = Canvas(new_root2, height=70, width=250, bg='black')
    can3.pack()

    pvar1 = StringVar()
    can2.create_text(80, 10, text='ENTER NAME OF PLAYER-1', fill='white', font='comicsansms 9 bold')
    player1 = Entry(new_root, textvariable=pvar1, fg='black', font='comicsansms 14 italic')
    player1.place(x=10, y=30)
    player1but = Button(new_root, text='Done(->)', bg='black', fg='white', bd=4, command=goplayer1)
    player1but.place(x=180, y=0)

    pvar2 = StringVar()
    can3.create_text(80, 10, text='ENTER NAME OF PLAYER-2', fill='white', font='comicsansms 9 bold')
    player2 = Entry(new_root2, textvariable=pvar2, fg='black', font='comicsansms 14 italic')
    player2.place(x=10, y=30)
    player2but = Button(new_root2, text='Done(->)', bg='black', fg='white', bd=4, command=goplayer2)
    player2but.place(x=180, y=0)


can.create_text(330, 30, text='WELCOME TO TIC-TAC-TOE', font='comicsansms 35 bold', fill='cyan')
can.create_text(710, 30, text='------', font='comicsansms 35 bold', fill='white')
can.create_text(1020, 30, text='DEVELOPED BY ATIF', font='comicsansms 35 bold', fill='cyan')

can.create_line(20, 60, 1250, 60, dash = (5, 2), fill='white')
can.create_line(830, 70, 830, 700, dash = (5, 2), fill='white')

can.create_line(10, 68, 820, 68, fill='blue', width=4)
can.create_line(820, 66, 820, 652, fill='blue', width=4)
can.create_line(10, 66, 10, 650, fill='blue', width=4)
can.create_line(10, 650, 820, 650, fill='blue', width=4)

can.create_line(840, 68, 1250, 68, fill='blue', width=4)
can.create_line(1250, 66, 1250, 651, fill='blue', width=4)
can.create_line(842, 68, 840, 650, fill='blue', width=4)
can.create_line(1250, 650, 840, 650, fill='blue', width=4)

can.create_line(720,70, 720, 660, fill='grey', width=4) # Special vertical line

def ChangeBut1():
    global count
    if text1.get() == '':
        if count%2 ==0:                                                # dict{'atif':'X', 'bot':'O'}
            signs = dict.values()
            signs = list(signs)
            text1.set(signs[1])
            winsound.Beep(800, 100)
        else:
            signs = dict.values()
            signs = list(signs)
            text1.set(signs[0])
            winsound.Beep(800, 100)
        count+=1

def ChangeBut2():
    global count
    if text2.get() == '':
        print(count)
        if count%2 == 0:
            signs = dict.values()
            signs = list(signs)
            text2.set(signs[1])
            winsound.Beep(800, 100)
            Win()
            draw()
        else:
            signs = dict.values()
            signs = list(signs)
            text2.set(signs[0])
            winsound.Beep(800, 100)
            Win()
            draw()
        count+=1

def ChangeBut3():
    global count
    if text3.get() == '':
        if count % 2 == 0:
            signs = dict.values()
            signs = list(signs)
            text3.set(signs[1])
            winsound.Beep(800, 100)
            Win()
            draw()
        else:
            signs = dict.values()
            signs = list(signs)
            text3.set(signs[0])
            winsound.Beep(800, 100)
            Win()
            draw()
        count += 1

def ChangeBut4():
    global count
    if text4.get() == '':
        if count % 2 == 0:
            signs = dict.values()
            signs = list(signs)
            text4.set(signs[1])
            winsound.Beep(800, 100)
            Win()
            draw()
        else:
            signs = dict.values()
            signs = list(signs)
            text4.set(signs[0])
            winsound.Beep(800, 100)
            Win()
            draw()
        count += 1

def ChangeBut5():
    global count
    if text5.get() == '':
        if count % 2 == 0:
            signs = dict.values()
            signs = list(signs)
            text5.set(signs[1])
            winsound.Beep(800, 100)
            Win()
            draw()
        else:
            signs = dict.values()
            signs = list(signs)
            text5.set(signs[0])
            winsound.Beep(800, 100)
            Win()
            draw()
        count += 1

def ChangeBut6():
    global count
    if text6.get() == '':
        if count % 2 == 0:
            signs = dict.values()
            signs = list(signs)
            text6.set(signs[1])
            winsound.Beep(800, 100)
            Win()
            draw()
        else:
            signs = dict.values()
            signs = list(signs)
            text6.set(signs[0])
            winsound.Beep(800, 100)
            Win()
            draw()
        count += 1

def ChangeBut7():
    global count
    if text7.get() == '':
        if count % 2 == 0:
            signs = dict.values()
            signs = list(signs)
            text7.set(signs[1])
            winsound.Beep(800, 100)
            Win()
            draw()
        else:
            signs = dict.values()
            signs = list(signs)
            text7.set(signs[0])
            winsound.Beep(800, 100)
            Win()
            draw()
        count += 1

def ChangeBut8():
    global count
    if text8.get() == '':
        if count % 2 == 0:
            signs = dict.values()
            signs = list(signs)
            text8.set(signs[1])
            winsound.Beep(800, 100)
            Win()
            draw()
        else:
            signs = dict.values()
            signs = list(signs)
            text8.set(signs[0])
            winsound.Beep(800, 100)
            Win()
            draw()
        count += 1

def ChangeBut9():
    global count
    if text9.get() == '':
        if count % 2 == 0:
            signs = dict.values()           # dict{'atif':'X', 'bot':'O'}
            signs = list(signs)
            text9.set(signs[1])
            winsound.Beep(800, 100)
            Win()
            draw()
        else:
            signs = dict.values()
            signs = list(signs)
            text9.set(signs[0])
            winsound.Beep(800, 100)
            Win()
            draw()
        count += 1

# Vertical Lines of Board
# can.create_line(240, 70, 240, 650, fill='grey', width=4)
# can.create_line(480, 70, 480, 650, fill='grey', width=4)
#
# # Horizontal Lines of Board
# can.create_line(819, 260, 10, 260, fill='grey', width=4)
# can.create_line(819, 450, 10, 450, fill='grey', width=4)

# def Compvsyou():
#     text1.set(''), text2.set(''), text3.set(''), text4.set(''), text5.set(''), text6.set(''), text7.set(''), text8.set(''), text9.set('')
#     possiblemoves = []
#     dictai = {1:text1.get(), 2:text2.get(), 3:text3.get(), 4:text4.get(), 5:text5.get(), 6:text6.get(), 7:text7.get(), 8:text8.get(), 9:text9.get()}
#     for o, l in dictai.items():
#         if l == '':
#             possiblemoves.append(o)
#     You = dict[Random]
#     Comp = dict[s]
#     for m in possiblemoves:             # dict{'atif':'X', 'bot':'O'}   1-You , 2-Comp
#         messagebox.showinfo('INFO', 'This Part is Under Development\nNikal Pehli Fursat Me *****')
#         break


def draw():
    if text1.get() != '' and text2.get() != '' and text3.get() != '' and text4.get() != '' and text5.get() != '' and text6.get() != '' and text7.get() != '' and text8.get() != '' and text9.get() != '':
        global wsl, wsl2
        wsl = can.create_text(950, 190, text='Tie', fill='white', font='comicsansms 12 bold')
        wsl2 = can.create_text(1170, 190, text='Tie', fill='white', font='comicsansms 12 bold')
        messagebox.showerror('TIE', "CONGRATULATIONS YOU BOTH PLAYED WELL IT'S A TIE")

def Win():
    if (text1.get() == text2.get() == text3.get() == 'X') or (text1.get() == text5.get() == text9.get() == 'X') or (text1.get() == text4.get() == text7.get() == 'X'):
        if dict[Random] == 'X':
            messagebox.showinfo('INFO', f'CONGRATULATIONS {Random.upper()} YOU WON')
            global wl,wl2
            wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            return
        else:
            messagebox.showinfo('INFO', f'CONGRATULATIONS {s.upper()} YOU WON')
            wl = can.create_text(950, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Won', fill='white', font='comicsansms 12 bold')
        return

    elif (text2.get() == text5.get() == text8.get() == 'X'):
        if dict[Random] == 'X':
            messagebox.showinfo('INFO', f'CONGRATULATIONS {Random.upper()} YOU WON')
             
            wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            return
        else:
            messagebox.showinfo('INFO', f'CONGRATULATIONS {s.upper()} YOU WON')
            #  
            wl = can.create_text(950, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Won', fill='white', font='comicsansms 12 bold')
            return

    elif (text3.get() == text6.get() == text9.get() == 'X') or (text3.get() == text5.get() == text7.get() == 'X'):
        if dict[Random] == 'X':
            messagebox.showinfo('INFO', f'CONGRATULATIONS {Random.upper()} YOU WON')
             
            wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            return
        else:
            messagebox.showinfo('INFO', f'CONGRATULATIONS {s.upper()} YOU WON')
            #  
            wl = can.create_text(950, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Won', fill='white', font='comicsansms 12 bold')
            return

    elif (text4.get() == text5.get() == text6.get() == 'X'):
        if dict[Random] == 'X':
            messagebox.showinfo('INFO', f'CONGRATULATIONS {Random.upper()} YOU WON')
             
            wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            return
        else:
            messagebox.showinfo('INFO', f'CONGRATULATIONS {s.upper()} YOU WON')
            #  
            wl = can.create_text(950, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Won', fill='white', font='comicsansms 12 bold')
            return

    elif (text7.get() == text8.get() == text9.get() == 'X'):
        if dict[Random] == 'X':
            messagebox.showinfo('INFO', f'CONGRATULATIONS {Random.upper()} YOU WON')
             
            wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            return
        else:
            messagebox.showinfo('INFO', f'CONGRATULATIONS {s.upper()} YOU WON')
            #  
            wl = can.create_text(950, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Won', fill='white', font='comicsansms 12 bold')
            return

    elif (text1.get() == text2.get() == text3.get() == 'O') or (text1.get() == text5.get() == text9.get() == 'O') or (
            text1.get() == text4.get() == text7.get() == 'O'):
        if dict[Random] == 'O':
            messagebox.showinfo('INFO', f'CONGRATULATIONS {Random.upper()} YOU WON')
             
            wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            return
        else:
            messagebox.showinfo('INFO', f'CONGRATULATIONS {s.upper()} YOU WON')
            #  
            wl = can.create_text(950, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Won', fill='white', font='comicsansms 12 bold')
            return

    elif (text2.get() == text5.get() == text8.get() == 'O'):
        if dict[Random] == 'O':
            messagebox.showinfo('INFO', f'CONGRATULATIONS {Random.upper()} YOU WON')
             
            wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            return
        else:
            messagebox.showinfo('INFO', f'CONGRATULATIONS {s.upper()} YOU WON')
            #  
            # wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl = can.create_text(950, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Won', fill='white', font='comicsansms 12 bold')
            return

    elif (text3.get() == text6.get() == text9.get() == 'O') or (text3.get() == text5.get() == text7.get() == 'O'):
        if dict[Random] == 'O':
            messagebox.showinfo('INFO', f'CONGRATULATIONS {Random.upper()} YOU WON')
             
            wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            return
        else:
            messagebox.showinfo('INFO', f'CONGRATULATIONS {s.upper()} YOU WON')
            wl = can.create_text(950, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Won', fill='white', font='comicsansms 12 bold')
            return

    elif (text4.get() == text5.get() == text6.get() == 'O'):
        if dict[Random] == 'O':
            messagebox.showinfo('INFO', f'CONGRATULATIONS {Random.upper()} YOU WON')
            wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            return
        else:
            messagebox.showinfo('INFO', f'CONGRATULATIONS {s.upper()} YOU WON')
            wl = can.create_text(950, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Won', fill='white', font='comicsansms 12 bold')
            return

    elif (text7.get() == text8.get() == text9.get() == 'O'):
        if dict[Random] == 'X':
            messagebox.showinfo('INFO', f'CONGRATULATIONS {Random.upper()} YOU WON')
            wl = can.create_text(950, 190, text='Won', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            return
        else:
            messagebox.showinfo('INFO', f'CONGRATULATIONS {s.upper()} YOU WON')
            wl = can.create_text(950, 190, text='Lost', fill='white', font='comicsansms 12 bold')
            wl2 = can.create_text(1170, 190, text='Won', fill='white', font='comicsansms 12 bold')
            return

def reset():
    text1.set('')
    text2.set('')
    text3.set('')
    text4.set('')
    text5.set('')
    text6.set('')
    text7.set('')
    text8.set('')
    text9.set('')
    try:
        can.itemconfigure(wl, text='')
        can.itemconfigure(wl2, text='')
    except Exception:
        can.itemconfigure(wsl, text='')
        can.itemconfigure(wsl2, text='')

def exitthegame():
    quests = messagebox.askquestion('Confirm Exit???', 'ARE YOU SURE YOU WANT TO QUIT')
    if quests == 'yes':
        exit()
    else:
        pass

def Boarddisp():
    global but1, but2, but3, but4, but5, but6, but7, but8, but9, text1, text2, text3, text4, text5, text6, text7, text8, text9
    text1 = StringVar()
    text2 = StringVar()
    text3 = StringVar()
    text4 = StringVar()
    text5 = StringVar()
    text6 = StringVar()
    text7 = StringVar()
    text8 = StringVar()
    text9 = StringVar()

    X_But.destroy()
    O_But.destroy()
    letsgo.destroy()
    can.delete(s1)
    can.delete(s2)
    can.delete(select)

    can.create_text(1060, 80, text='Score-Board', fill='white', font='comicsansms 16 italic')
    dash = '-' * 90
    can.create_text(1050, 175, text=dash, fill='white', font='comicsansms 12 bold')
    can.create_text(1060, 250, text='|\n|\n|\n|\n|\n|\n|\n|', fill='white', font='comicsansms 12 bold')

    can.create_text(950, 160, text=f'{Random.upper()}-({dict[Random]})', fill='white', font='comicsansms 12 bold')
    can.create_text(1170, 160, text=f'{s.upper()}-({dict[s]})', fill='white', font='comicsansms 12 bold')

    resetgame = Button(root, text='New Game', fg='red', bg='#FFD39B', padx=105, font='comicsansms 15 italic', command=reset)
    resetgame.place(x=890, y=380)

    # Comp = Button(root, text='you Vs computer', fg='red', bg='#FFD39B', padx=105, font='comicsansms 15 italic', command=Compvsyou)
    # Comp.place(x=890, y=450)

    exitgame = Button(root, text='Quit', fg='red', bg='black', padx=133, font='comicsansms 15 bold', command=exitthegame)
    exitgame.place(x=890, y=520)

    messagebox.showinfo('INFO', f'{Random.upper()} START THE GAME')

    but1 = Button(root, text='  ', font='comicsansms 15 bold', fg='black', bg='pink', padx=107, pady=76, textvariable=text1, command= ChangeBut1)
    but1.place(x='21', y='69')
    but2 = Button(root, text='  ', font='comicsansms 15 bold', fg='black', bg='pink', padx=111, pady=76, textvariable=text2, command=ChangeBut2)
    but2.place(x='253', y='69')
    but3 = Button(root, text='  ', font='comicsansms 15 bold', fg='black', bg='pink', padx=111, pady=76, textvariable=text3, command=ChangeBut3)
    but3.place(x='493', y='69')
    but4 = Button(root, text='  ', font='comicsansms 15 bold', fg='black', bg='pink', padx=107, pady=76, textvariable=text4, command=ChangeBut4)
    but4.place(x='21', y='261')
    but5 = Button(root, text='  ', font='comicsansms 15 bold', fg='black', bg='pink', padx=111, pady=76, textvariable=text5, command=ChangeBut5)
    but5.place(x='253', y='261')
    but6 = Button(root, text='  ', font='comicsansms 15 bold', fg='black', bg='pink', padx=111, pady=76, textvariable=text6, command=ChangeBut6)
    but6.place(x='493', y='261')
    but7 = Button(root, text='  ', font='comicsansms 15 bold', fg='black', bg='pink', padx=107, pady=76, textvariable=text7, command=ChangeBut7)
    but7.place(x='21', y='453')
    but8 = Button(root, text='  ', font='comicsansms 15 bold', fg='black', bg='pink', padx=111, pady=76, textvariable=text8, command=ChangeBut8)
    but8.place(x='253', y='453')
    but9 = Button(root, text='  ', font='comicsansms 15 bold', fg='black', bg='pink', padx=111, pady=76, textvariable=text9, command=ChangeBut9)
    but9.place(x='493', y='453')

start_but = Button(root, text='START GAME', font='comicsansms 15 bold', command=name_entry, fg='white', bg='black')
start_but.place(x=930, y=100)

def atif():
    global s1, s2, s, dict
    dict = {}
    s1 = can.create_text(1030, 250, text=f'{Random.upper()} You Selected : "X" ', font='comicsansms 12 bold', fill='white')
    lst.remove(Random)
    s=''
    s = s.join(lst)
    s2 = can.create_text(1030, 290, text=f'{s.upper()} You Selected : "O" ', font='comicsansms 12 bold', fill='white')
    lst.insert(0, Random)
    dict[Random] = 'X'
    dict[s] = 'O'
    print(dict)
def atifA():
    global s1, s2, s, dict
    dict = {}
    s1 = can.create_text(1030, 250, text=f'{Random.upper()} You Selected : "O" ', font='comicsansms 12 bold', fill='white')
    lst.remove(Random)
    s = ''
    s = s.join(lst)
    s2 = can.create_text(1030, 290, text=f'{s.upper()} You Selected : "X" ', font='comicsansms 12 bold', fill='white')
    lst.insert(0, Random)
    dict[Random] = 'O'
    dict[s] = 'X'

def choice():
    global X_But, O_But
    X_But = Button(root, text='X', font='comicsansms 15 bold', fg='red', padx=32, pady=15, bg='purple', command=atif)
    X_But.place(x=950, y=150)
    O_But = Button(root, text='O', font='comicsansms 15 bold', fg='white', padx=30, pady=15, bg='purple', command=atifA)
    O_But.place(x=1045, y=150)

root.mainloop()
