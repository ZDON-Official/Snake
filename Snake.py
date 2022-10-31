from tkinter import Canvas


class Snake:
    def __init__(self, canvas, body_parts, space_size, color) -> None:
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []
        self.space_s = space_size
        self.color = color

        for _ in range(0, body_parts):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + space_size, y+space_size, fill = color, tag='snake')
            self.squares.append(square)

    def reset(self, canvas: Canvas) -> None:
        space_size = self.space_s

        self.coordinates.clear() # clear the coordinates
        for _ in range(0, self.body_size):
            self.coordinates.append([0,0])
        
        self.squares.clear() # clear body parts
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + space_size, y+space_size, fill = self.color, tag='snake')
            self.squares.append(square)
        