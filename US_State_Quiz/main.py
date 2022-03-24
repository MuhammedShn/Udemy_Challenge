import turtle
import pandas

FONT = ("Arial",8, "normal")
SCREEN_SIZE = [725, 491]

data = pandas.read_csv("50_states.csv")
guessed_state = []


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
screen.addshape(image)
turtle.shape(image)

while len(guessed_state) < 51:

    answer = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?")
    answer = answer.title()

    if answer == "Exit":
        state_to_learn = data["state"].to_list()
        state_to_learn = [states for states in state_to_learn if states not in guessed_state]
        state_to_learn = {"state": state_to_learn}
        data_frame = pandas.DataFrame(state_to_learn)
        data_frame.to_csv("state_to_learn.csv")
        break
    if answer in data["state"].values:
        if answer not in guessed_state:
            state = turtle.Turtle()
            state.hideturtle()
            state.penup()
            state_data = data[data.state == answer]
            guessed_state.append(answer)
            state.goto(int(state_data.x),int(state_data.y))
            state.write(arg=state_data.state.item(), move=False, align="center", font=FONT)
        else:
            pass
    else:
        pass


