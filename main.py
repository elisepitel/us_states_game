from turtle import Turtle
import turtle
import pandas


# Set Screen with map
screen = turtle.Screen()
screen.title("U.S States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # Get coordinate of states on images
# def get_mouse_click_coor(x, y):
#    print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# access data from 50_states.csd
us_states = pandas.read_csv('50_states.csv')
us_states_name = us_states.state
us_states_x = us_states.x
us_states_y = us_states.y

us_states_list = []
for state in range(len(us_states_name)):
    us_states_list.append(us_states_name[state])
print(us_states_list)


# user score
score = 0
guessed_states = []
while score < 50:
    # open prompt for user question
    answer_state = screen.textinput(title=f"{score}/50 States",
                                    prompt="What's another State's name?").title()
    if answer_state.title() == "Exit":
        # generate list of non guessed states
        missing_states = [state for state in us_states_list if state not in guessed_states]
        # generate a csv file with all states user couldn't name
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        # exit prompt
        break
    # check in all the states name
    for nb in range(len(us_states_name)):

        # check if user answer match with one of US States name
        if str(answer_state) == str(us_states_name[nb]):
            guessed_states.append(answer_state)
            # write name of the state at the state coor, increase score
            name_on_map = Turtle()
            name_on_map.hideturtle()
            name_on_map.penup()
            name_on_map.goto(us_states_x[nb],us_states_y[nb])
            name_on_map.write(f"{answer_state}", font=("Calibri", 8, "bold"))
            score += 1


turtle.mainloop()
