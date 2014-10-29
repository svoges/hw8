def recursive(machine, hour, total):
    # the initial state
    if hour == 0:
        do_A = recursive('A', hour + 1, A_schedule[hour])
        do_B = recursive('B', hour + 1, B_schedule[hour])
        if do_A > do_B:
            movements[hour] = 'A'
        else:
            movements[hour] = 'B'
        return max(do_A, do_B)
    # the base case, when the length of the list is equal to the hour
    elif len(A_schedule) == hour + 1:
        if machine == 'A':
            if total + A_schedule[hour] > totals[hour]:
                movements[hour] = 'A'
                totals[hour] = total + A_schedule[hour]
            return total + A_schedule[hour]
        elif machine == 'B':
            if total + B_schedule[hour] > totals[hour]:
                movements[hour] = 'B'
                totals[hour] = total + B_schedule[hour]
            return total + B_schedule[hour]
        else:
            return 0
    # if the state of the machine is currently A
    elif machine == 'A':
        do_A = recursive('A', hour + 1, A_schedule[hour] + total)
        move_to_B = recursive('move_to_B', hour + 1, total)
        if do_A == totals[hour + 1] and len(movements[hour]) > 2 and movements[hour][0:4] != "move":
            movements[hour] = 'A'
            totals[hour] = do_A
        if move_to_B == totals[hour + 1] and movements[hour][0:4] != "move":
            movements[hour] = 'B'
            totals[hour] = move_to_B
        return max(do_A,move_to_B)
    # if the state of the machine is currently B
    elif machine == 'B':
        do_B = recursive('B', hour + 1, total + B_schedule[hour])
        move_to_A = recursive('move_to_A', hour + 1, total)
        if do_B == totals[hour + 1] and movements[hour][0:4] != "move":
            movements[hour] = 'B'
            totals[hour] = do_B
        if move_to_A == totals[hour + 1] and movements[hour][0:4] != "move":
            movements[hour] = 'A'
            totals[hour] = move_to_A
        return max(do_B, move_to_A)
    # if the state of the machine is the first at A
    elif machine == 'move_to_A':
        move_to_A = recursive('A', hour + 1, total + A_schedule[hour])
        if move_to_A == totals[hour + 1]:
            movements[hour - 1] = 'move_to_A'
            movements[hour] = 'A'
            totals[hour] = move_to_A
        return move_to_A
    # if the state of the machine is the first at B
    elif machine == 'move_to_B':
        move_to_B = recursive('B', hour + 1, total + B_schedule[hour])
        if move_to_B == totals[hour + 1]:
            movements[hour - 1] = 'move_to_B'
            movements[hour] = 'B'
            totals[hour] = move_to_B
        return move_to_B
    # the what the fuck why is it here state
    else:
        print "you printed this and i have absolutely no idea why"

def iterative(A_schedule, B_schedule):
    hour = len(A_schedule)

if __name__ == "__main__":
    print "---Should print 28---"
    movements = []
    totals = []
    A_schedule = [10, 1, 5, 10]
    B_schedule = [5, 2, 3, 15]
    for i in range(len(A_schedule)):
        movements.extend('i')
        movements[i] = 'a'
        totals.extend('i')
        totals[i] = 0
    print recursive('', 0, 0)
    recursive('', 0, 0)
    print movements
    # print totals
    print "---Should print 11---"
    A_schedule = [1, 2, 3, 4]
    B_schedule = [4, 3, 2, 1]
    movements = []
    totals = []

    for i in range(len(A_schedule)):
        movements.extend('i')
        movements[i] = 'a'
        totals.extend('i')
        totals[i] = 0

    print recursive('', 0, 0)
    print movements
    # print totals
    print "---Should print 17---"
    A_schedule = [1, 2, 3, 10]
    B_schedule = [4, 3, 8, 1]
    movements = []
    totals = []

    for i in range(len(A_schedule)):
        movements.extend('i')
        movements[i] = 'a'
        totals.extend('i')
        totals[i] = 0

    print recursive('', 0, 0)
    print movements

    print "---Should print 18---"
    A_schedule = [1, 2, 4, 10]
    B_schedule = [4, 3, 8, 1]
    movements = []
    totals = []

    for i in range(len(A_schedule)):
        movements.extend('i')
        movements[i] = 'a'
        totals.extend('i')
        totals[i] = 0

    print recursive('', 0, 0)
    print movements
