import turtle
import pandas

def myVersion():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "states.gif"
    screen.setup(width=725, height=491, startx=20, starty=20)
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("50_states.csv")
    total_states = data.state.to_list()
    all_states = data.state.to_list()

    state = None

    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()

    finish_game = False

    states_to_show = 0

    def drawStates(state):
        states_to_show = len(total_states) - len(all_states)
        screen_title = f"{states_to_show}/{len(all_states)} States Remaining"
        while state is None:
            answer_state = screen.textinput(title=screen_title, prompt="What's another state's name?")
            #print(f"answer_state: {answer_state}")

            if answer_state != "":
                for state_item in all_states:
                    if state_item.lower() == answer_state.lower():
                        state = answer_state.title()

        #print(f"state: {state}")
        state_data = data[data.state == state]
        #print(f"state_data: {state_data}")
        state_x = int(state_data.x.iloc[0])
        state_y = int(state_data.y.iloc[0])
        #print(f"state_x: {state_x}, state_y: {state_y}")

        state_turtle.goto(state_x, state_y)
        state_turtle.write(state)
        all_states.remove(state)

    while finish_game is False:
        drawStates(state)

        if state == "Exit":
            finish_game = True

# def get_mouse_click_coor(x, y):
#     #print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
    turtle.mainloop()
