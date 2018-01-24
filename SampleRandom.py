import random
import easygui

# random.seed(20)
# random.seed(random.random())

# (0, 1) To (50, 100)
run = True
while run == True:
    seed = easygui.integerbox(msg="Enter The Seed:", title="Fuck You Bitch", default=random.random(), lowerbound=0)
    random.seed(seed)
    for i in range(0, 10):
        print (50 * random.random()) + 50

    choice = easygui.ynbox(msg="Do You Want To Fuck Off(y/n)")
    if choice == True:
        easygui.msgbox("Thank You For Leaving Me Alone")
        run = False
