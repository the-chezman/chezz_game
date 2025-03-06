print("barGraph module loaded successfully!")

def runFunction():
    import matplotlib.pyplot as plt # type: ignore
    import numpy as np # type: ignore

    # ^^^ doesnt put error message


    daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    hoursSpent = []

    for i in range(7):
        hours = int(input("how many hours on " + str(daysOfWeek[i]) + "?: "))
        hoursSpent.append(hours)

    plt.bar(daysOfWeek, hoursSpent)
    plt.title('Hours Spent per Day of the Week')
    plt.xlabel('Days of the Week')
    plt.ylabel('Hours Spent')
    plt.show()
