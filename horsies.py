from horse_race import horse_race
import matplotlib.pyplot as plt
import random
# from matplotlib import style
from matplotlib.pyplot import plot, draw, show


x_axis = [2,3,4,5,6,7,8,9,10,11,12]
y_axis_winners = [0,0,0,0,0,0,0,0,0,0,0]
y_axis_dead_horses = [0,0,0,0,0,0,0,0,0,0,0]


for i in range (0,1000):
    print('\nRunning Race #', i+1)
    dead_horses, winning_horse = horse_race()

    y_axis_winners[winning_horse - 2] += 1
    for j in dead_horses:
        y_axis_dead_horses[j-2] += 1
    if i % 10 == 0:
        # style.use('fivethirtyeight')
        plt.subplot(2, 1, 1)
        plt.bar(x_axis, y_axis_winners)
        plt.title('Horsies Outcomes')
        plt.ylabel('Winning Horses')
        # for i,j in zip(x_axis,y_axis_winners):
            # plt.annotate(str(j),xy=(i,j+3))
        
        plt.subplot(2, 1, 2)
        plt.bar(x_axis, y_axis_dead_horses)
        plt.xlabel('Horse Number')
        plt.ylabel('Dead Horses')
        # for i,j in zip(x_axis,y_axis_dead_horses):
            # plt.annotate(str(j),xy=(i,j+3))
        # plt.figure(figsize=(10,10)) 
        plt.show()
