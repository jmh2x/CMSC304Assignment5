#Govan Henry CMSC304 Assignment 5 3/15/2025
import tkinter
from rectpack import newPacker
import sys 

#class CustomCanvas
class CustomCanvas:
     def __init__(self, height: int, width: int): #constructor with height and width as ints
        self.root =tkinter.Tk() #creates window
        self.canvas = tkinter.Canvas(self.root, height=height, width=width, bg="black") #create canvas, black
        self.canvas.pack() #add canvas in window

     def display(self): #display canvas in window
        self.root.mainloop()

#class Rectangle
class Rectangle:
    def __init__(self, height: int, width: int, x: int = 0, y: int = 0): #constructor with height width as ints, x and y = 0
        self.height = height 
        self.width = width 
        self.x = x 
        self.y = y 
    
    def draw(self,canvas): #draw rectangle on canvas
        x1, y1 = self.x, self.y #top left corner
        x2, y2 = x1 + self.width, y1 + self.height #bottom right corner
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue") #draw rectangle, blue

#pack function
def pack(allRect, canvasSize):
    p = newPacker(rotation=False)  #create packer, disable rotation

    #add rectangle
    for rect in allRect:
        p.add_rect(rect.width, rect.height)  
 
    p.add_bin(canvasSize[1], canvasSize[0])  #(width, height)
    
    p.pack()#run packer

    packrects = [] #create list
    for rect_bin in p: #each bin
        for rect in rect_bin: #each rect
            width, height, x, y = rect.width, rect.height, rect.x, rect.y
            packrects.append(Rectangle(width, height, x, y))  #add new rectangle to list

    return packrects  #Return list

#main function
def main():
    file_path = sys.argv[1]  #read file path

    with open(file_path) as file: #open and read file
            lines = file.readlines() 
            canvas_height, canvas_width = map(int, lines[0].strip().split(","))#first line = canvas size , split by commma
            rectangles = [
                Rectangle(int(w), int(h)) #create rectangle
                for h, w in (line.strip().split(",") #split by comma
                             for line in lines[1:])#after first line
            ]  
            #sum of all rectangles
            max_width = max(rect.width for rect in rectangles)
            max_height = max(rect.height for rect in rectangles)
            total_width = sum(rect.width for rect in rectangles)
            total_height = sum(rect.height for rect in rectangles)

            #canvas size
            canvas_width = max(max_width, total_width)
            canvas_height = max(max_height, total_height)

    #pack rectanges
    packrects = pack(rectangles, (canvas_height, canvas_width))

    #create canvas
    canvas = CustomCanvas(canvas_height, canvas_width)

    #draw rect on canvas
    for rect in packrects:
        rect.draw(canvas.canvas)

    #dipslay canvas
    canvas.display()

if __name__ == "__main__":
    main()  #run main