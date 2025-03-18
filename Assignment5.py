#Govan Henry CMSC304 Assignment 5 3/15/2025
import tkinter
from rectpack import newPacker
import sys

#class CustomCanvas
class CustomCanvas:
    def __init__(self, height: int, width: int):#constructor with height and width as ints
        self.root = tkinter.Tk()#creates window
        self.canvas = tkinter.Canvas(self.root, height=height, width=width, bg="black")#create canvas, black
        self.canvas.pack()#pack canvas in window

    def display(self):#display canvas in window
        self.root.mainloop()

#class Rectangle
class Rectangle:
    def __init__(self,height: int,width: int, x: int = 0, y: int = 0): #constructor with height width as ints, x and y = 0
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, canvas):#draw rectangle on canvas
        x1 = self.x#top left corner,x coord
        y1 = self.y#top left corner,y coord
        x2 = x1 + self.width#bottom right corner,x coord
        y2 = y1 + self.height#bottom right corner,y coord
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")#draw rectangle, blue

#pack function
def pack(allRect, canvasSize):
    p = newPacker()#create packer

    #add rectangle
    for rect in allRect:
        p.add_rect(rect.width, rect.height)

    p.add_bin(canvasSize[1], canvasSize[0]) #(width, height)

    p.pack()#run packer

    packrects = []#create list
    for rect_bin in p:#each bin in packer
        for rect in rect_bin:#each rect in bin
            x = rect.x
            y = rect.y
            width = rect.width
            height = rect.height
            packrects.append(Rectangle(height, width, x, y)) #add new rectangle to list

    return packrects #return list

#main function
def main():
    file_path = sys.argv[1]#read file path

    with open(file_path) as file:#open and read file
        lines = file.readlines()
        canvas_height, canvas_width = map(int, lines[0].strip().split(","))#first line = canvas size , split by commma
        rectangles = [
            Rectangle(int(h), int(w)) #create rectangle
            for h, w in (line.strip().split(",") #split by comma
                         for line in lines[1:])#all lines after first line
        ]
    
    packed_rects = pack(rectangles, (canvas_height, canvas_width))#pack rectanges

    canvas = CustomCanvas(canvas_height, canvas_width)#create canvas

    for rect in packed_rects:#draw rect on canvas
        rect.draw(canvas.canvas)

    canvas.display()#dipslay canvas

if __name__ == "__main__":
    main() #run main
