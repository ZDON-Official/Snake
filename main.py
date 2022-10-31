# this is the main file for the game
from tkinter import *
from traceback import print_tb
from Snake import Snake
from Food import Food

# these are constants 
GAME_WIDTH =  700
GAME_HEIGHT = 700
SPEED = 100 # snake speed / fps
SPACE_SIZE = 50 # size of food and body parts
BODY_PARTS = 3 # num of body parts at the start
SNAKE_COLOR = 'blue'
FOOD_COLOR = 'red'
BACKGROUND = 'black'


def next_turn(window:Tk, canvas:Canvas, label:Label, snake:Snake, food:Food, speed, space_size, color):
    # print('speed is ', SPEED)
    global direction
    
    x,y = snake.coordinates[0]

    if direction == 'up':
        y -= space_size
    elif direction == 'down':
        y += space_size
    elif direction == 'left':
        x -= space_size
    elif direction == 'right':
        x += space_size

    snake.coordinates.insert(0, (x,y))

    square = canvas.create_rectangle(x,y, x+space_size, y+space_size, fill=color)

    snake.squares.insert(0, square)

    # eating food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score 
        score += 1

        label.config(text='Score:{}'.format(score))

        canvas.delete('food')

        food = Food(canvas, GAME_HEIGHT, GAME_WIDTH, SPACE_SIZE, FOOD_COLOR)
    else:    
        # delete last body part
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        # print('game over')
        global status
        status = True
        game_over(window, canvas, snake, food)

    window.after(speed, next_turn, window, canvas, label, snake, food, speed, space_size, color)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

    return direction

def check_collision(snake: Snake):
    # print('pos ', snake.coordinates)
    x,y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True


    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False

status = True
def game_over(window:Tk, canvas: Canvas, snake, food):
    global status
    if status == True:
        canvas.delete('all')
        canvas.create_text(
            canvas.winfo_width()/2, 
            canvas.winfo_height()/2,
            font=('consolas', 70),
            text='GAME OVER',
            fill='red',
            tags='game_over'
        )
        # window.quit()
        # print('game over')
    else:
        # print('in game over ', status)  
        pass

    # restart game 
    window.bind('<space>', lambda event: window.quit())

def restart(window:Tk, canvas:Canvas, snake: Snake, food):
    print('in restart')
    canvas.delete('all')
    global direction, score, status
    direction = 'down'
    score = 0
    status = False
    snake.reset(canvas)
    run(window, canvas, snake, food)


def bind_keys(window:Tk):
    global direction

    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))


direction = 'down'
score = 0
def run(window:Tk, canvas:Canvas, snake:Snake, food:Food):
    print('running')
    window.title('Snake')
    window.resizable(False, False)

    # score and initial direction
    global score
    global direction
   

    label = Label(window, text='Score:{}'.format(score), font=('sans', 40))
    label.pack()

    # canvas = Canvas(window, bg=BACKGROUND, height=GAME_HEIGHT, width=GAME_WIDTH)
    # canvas.pack()

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    window.geometry(f'{window_width}x{window_height}+{x}+{y}')  

    # bind arrow keys
    bind_keys(window)
    

    # snake and object
    # snake = Snake(canvas, BODY_PARTS, SPACE_SIZE, SNAKE_COLOR)
    # food = Food(canvas, GAME_HEIGHT, GAME_WIDTH, SPACE_SIZE, FOOD_COLOR)

    next_turn(window, canvas, label, snake, food, SPEED, SPACE_SIZE, SNAKE_COLOR)

    window.mainloop()  

def main():
    window = Tk()

    # label = Label(window, text='Score:{}'.format(score), font=('sans', 40))
    # label.pack()

    canvas = Canvas(window, bg=BACKGROUND, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()


    snake = Snake(canvas, BODY_PARTS, SPACE_SIZE, SNAKE_COLOR)
    food = Food(canvas, GAME_HEIGHT, GAME_WIDTH, SPACE_SIZE, FOOD_COLOR)
    run(window, canvas, snake, food)                          


if __name__ == '__main__':
    main()