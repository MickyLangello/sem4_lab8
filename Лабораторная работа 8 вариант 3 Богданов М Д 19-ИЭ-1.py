from tkinter import *
from math import sqrt

root = Tk()
root.geometry("525x600")
root['bg'] = 'LightYellow'
root.title('Лабораторная работа №8')

def changeDiap(event):
	global x1, y1, x2, y2, R
	R = diap_scale.get()
	c.delete("all")	
	rememberState()

def showRast(event):
        global x1, y1, x2, y2
        rast = sqrt((event.x-x1)**2 + (event.y-y2)**2)
        rast_label["text"] = str('{:.1f}'.format(rast))

def changePlace(event):
        global DOWN, UP, x1, x2, y1, y2, k
        x1,x2,y1,y2 = event.x, event.x, event.y, event.y
        c.delete('all')     
        rememberState()             

def mirror(event):
        global k, UP, DOWN, x1, x2, y1, y2, R
        c.delete('all')
        k += 1
        rememberState()      

def restart(*args):
        global k, UP, DOWN, x1, x2 ,y1 ,y2, R
        c.delete('all')
        x1, y1, x2, y2 = 250, 250, 250, 250
        diap_scale.set(50)
        rast_label['text'] = ''
        R = 50
        rast = 25
        k = 0
        DOWN = c.create_arc(x1-R, y1-R, x2+R, y2+R ,extent = 180, start = 130, fill = 'Blue')
        UP = c.create_arc(x1-R, y1-R, x2+R, y2+R ,extent = 180, start = 310, fill = 'Yellow')
        c.tag_bind(UP, '<Button-3>', showRast)
        c.tag_bind(DOWN, '<Button-1>', changePlace)

def rememberState():
        global k
        if k % 2 == 0:
                DOWN = c.create_arc(x1-R, y1-R, x2+R, y2+R ,extent = 180, start = 130, fill = 'Blue')
                UP = c.create_arc(x1-R, y1-R, x2+R, y2+R ,extent = 180, start = 310, fill = 'Yellow')
        else:
                DOWN = c.create_arc(x1-R, y1-R, x2+R, y2+R ,extent = 180, start = 230, fill = 'Blue')
                UP = c.create_arc(x1-R, y1-R, x2+R, y2+R ,extent = 180, start = 50, fill = 'Yellow')

        c.tag_bind(UP, '<Button-3>', showRast)
        c.tag_bind(DOWN, '<Button-1>', changePlace)      

c = Canvas(width = 500, height = 500)
c.place(x = 10, y = 10)
	
diap_scale = Scale(from_=50, to = 100, orient = "horizontal", length = 250, command = changeDiap)

root.bind('<Insert>', mirror)
root.bind('<Delete>', restart)

rast_label = Label(text = '', width = 10, bg = "Black", fg = "White")
rast_label.place(x = 217, y = 10)
diap_scale.place(x = 129, y = 530)

restart()
root.mainloop()
