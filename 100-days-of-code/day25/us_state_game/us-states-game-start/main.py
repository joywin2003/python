import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
print(all_states)
answer = 0
answered_state = []
while answer != 50:
    answer_state = screen.textinput(title=f"{answer}/50 Guess the state", prompt="What's another states name").title()
    if answer_state == "Exit":
        unanswered_state = [state for state in all_states if state not in answered_state]
        print(unanswered_state)
        # for state in all_states:
        #     if state not in answered_state:
        #         unanswered_state.append(state)

        df = pandas.DataFrame(unanswered_state)
        df.to_csv("states_to_learn1.csv")
        break
    for state in all_states:
        if answer_state not in answered_state:
            if answer_state == state:
                answered_state.append(state)
                x_cor = int(states[states.state == state].x)
                y_cor = int(states[states.state == state].y)
                print(x_cor, y_cor)
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(x_cor, y_cor)
                t.write(state)
                answer += 1


