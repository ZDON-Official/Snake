import random

class Food:
    def __init__(self, canvas, height, width, space_size, color) -> None:
        x = random.randint(0, (height/space_size)-1) * space_size
        y = random.randint(0, (width/space_size)-1) * space_size

        self.coordinates = [x, y]

        canvas.create_oval(x,y,x+space_size, y+space_size, fill = color, tag = 'food')