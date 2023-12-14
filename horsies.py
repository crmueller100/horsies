from utils import *

def main():
    x_axis = [2,3,4,5,6,7,8,9,10,11,12]
    y_axis_winners = [0,0,0,0,0,0,0,0,0,0,0]
    y_axis_scratched_horses = [0,0,0,0,0,0,0,0,0,0,0]

    number_of_races = 10000

    for i in range (0,number_of_races):

        # print('\nRunning Race #', i+1)
        scratched_horses, winning_horse = race()

        # need -2 in index because of 0 based indexing and the first horse is labeled 2
        y_axis_winners[winning_horse - 2] += 1
        for j in scratched_horses:
            y_axis_scratched_horses[j-2] += 1
    
    plot_frequency_of_winners_and_scratchers(x_axis, y_axis_winners, y_axis_scratched_horses, number_of_races)
    plot_probability_of_winning(x_axis, y_axis_winners, number_of_races)

if __name__ == '__main__':
    main()
