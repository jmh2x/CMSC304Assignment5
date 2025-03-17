import tkinter as tkin


#Class CustomCanvas
class CustomCanvas:
     def __init__(self, height: int, width: int):
        self.canvas = tkin.Canvas(height=height, width=width)

#Class Rectangle
class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

#def pack(allRect, canvasSize)

#def main()