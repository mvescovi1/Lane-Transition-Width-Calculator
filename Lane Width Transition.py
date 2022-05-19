from tkinter import *
from tkinter import messagebox




root = Tk()
root.title('Lane Width Transition Calculator')
root.geometry('600x600')

    
    
def enter_ex_lane_width():
    global ex_lane_width 
    ex_lane_width = int(entrybox_ex.get())
    mylabel = Label(root, text=ex_lane_width)
    mylabel.pack()
   # root.quit
    
   
def enter_prop_lane_width():
    global prop_lane_width 
    prop_lane_width = int(entrybox_prop.get())
    mylabel = Label(root, text=prop_lane_width)
    mylabel.pack()
    

def enter_design_speed():
    global design_speed 
    design_speed = int(entrybox_speed.get())
    mylabel = Label(root, text=design_speed)
    mylabel.pack()


def calc_trans_length():
    global trans_length 
    
    if (design_speed >= 45):
        trans_length = (prop_lane_width-ex_lane_width)*design_speed
    else:
        trans_length = ((prop_lane_width-ex_lane_width)*design_speed**2)/60
    mylabel = Label(root, text=('transition length=',trans_length))
    mylabel.pack()
    

def exit_program():
    root.destroy()
    root.quit()
    


Label(root, text='Enter Existing Lane Width').pack()
entrybox_ex = Entry(root, width=50)
entrybox_ex.pack()

buttoncommit_ex = Button(root, text='commit existing lane width', command = enter_ex_lane_width)
buttoncommit_ex.pack()

Label(root, text='Enter Proposed Lane Width').pack()
entrybox_prop = Entry(root, width=50)
entrybox_prop.pack()

buttoncommit_prop = Button(root, text='commit existing lane width', command = enter_prop_lane_width)
buttoncommit_prop.pack()

Label(root, text='Enter Design Speed').pack()
entrybox_speed = Entry(root, width=50)
entrybox_speed.pack()

buttoncommit_speed = Button(root, text='commit design speed', command = enter_design_speed)
buttoncommit_speed.pack()

buttoncommit_calculate = Button(root, text='calculate transition length', command = calc_trans_length)
buttoncommit_calculate.pack()

buttoncommit_exit = Button(root, text='Exit Program', command = exit_program)
buttoncommit_exit.pack()


root.mainloop()



#message = Tk()
#message.withdraw()
#messagebox.showinfo('Calculations', message=('Transition Length=',trans_length,'ft'))


