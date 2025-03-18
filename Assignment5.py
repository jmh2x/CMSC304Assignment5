#Govan Henry CMSC304 Assignment 5 3/15/2025
import tkinter
from rectpack import newPacker
import sys

# Class CustomCanvas
class CustomCanvas:
     def __init__(self, height: int, width: int): #constructor with height and width as ints
        self.root =tkinter.Tk() #creates window
        self.canvas = tkinter.Canvas(self.root, height=height, width=width, bg="black") #creates canvas, black background
        self.canvas.pack() #adds canvas in window

     def display(self): #display canvas in window
        self.root.mainloop()

# Class Rectangle
class Rectangle:
    def __init__(self, height: int, width: int, x: int = 0, y: int = 0): #constructor with height width as ints, x and y = 0
        self.height = height
        self.width = width
        self.x = x
        self.y = y
    
    def draw(self,canvas): #draw rectangle on canvas
        x1, y1 = self.x, self.y #top left corner
        x2, y2 = x1 + self.width, y1 + self.height #bottom right corner
        canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue") #draw rectangle, blue fill and black outline

# pack function
def pack(allRect, canvasSize):
    packer = newPacker()  #Create new packer

    # Add rectangle
    for rect in allRect:
        packer.add_rect(rect.width, rect.height)  
 
    packer.add_bin(canvasSize[1], canvasSize[0])  #(Width, Height)
    
    packer.pack()#Run packer

    packed_rectangles = []
    for rect_bin in packer: #each bin
        for rect in rect_bin: #each rect
            width, height, x, y = rect.width, rect.height, rect.x, rect.y
            packed_rectangles.append(Rectangle(width, height, x, y))  #add new rectangle to list

    return packed_rectangles  #Return list

# main function
def main():
    file_path = sys.argv[1]  #read file path

    with open(file_path) as file: #read file
            lines = file.readlines() 
            canvas_height, canvas_width = map(int, lines[0].strip().split(","))#first line = canvas size
            rectangles = [
                Rectangle(int(w), int(h)) for h, w in (line.strip().split(",") for line in lines[1:])
            ]  # Read all rectangles
    

    # Pack the rectangles
    packed_rects = pack(rectangles, (canvas_height, canvas_width))

    # Create canvas
    canvas = CustomCanvas(canvas_height, canvas_width)

    # Draw each rectangle on the canvas
    for rect in packed_rects:
        rect.draw(canvas.canvas)

    # Display the canvas
    canvas.display()

if __name__ == "__main__":
    main()  # Run the main function