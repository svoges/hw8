def recursive(machine, hour, total):
    # the initial state
    if hour == 0:
        do_A = recursive('A', hour + 1, A_schedule[hour])
        do_B = recursive('B', hour + 1, B_schedule[hour])
        return max(do_A, do_B)
    # the base case, when the length of the list is equal to the hour
    elif len(A_schedule) == hour + 1:
        if machine == 'A':
            return total + A_schedule[hour]
        elif machine == 'B':
            return total + B_schedule[hour]
        else:
            return 0
    # if the state of the machine is currently A
    elif machine == 'A':
        do_A = recursive('A', hour + 1, A_schedule[hour] + total)
        move_to_B = recursive('move_to_B', hour + 1, total)
        return max(do_A,move_to_B)
    # if the state of the machine is currently B
    elif machine == 'B':
        do_B = recursive('B', hour + 1, total + B_schedule[hour])
        move_to_A = recursive('move_to_A', hour + 1, total)
        return max(do_B, move_to_A)
    # if the state of the machine is the first at A
    elif machine == 'move_to_A':
        return recursive('A', hour + 1, total + A_schedule[hour])
    # if the state of the machine is the first at B
    elif machine == 'move_to_B':
        return recursive('B', hour + 1, total + B_schedule[hour])
    # the what the fuck why is it here state
    else:
        print "you printed this and i have absolutely no idea why"

def iterative(A_schedule, B_schedule):
    hour = len(A_schedule)

if __name__ == "__main__":
    print "---Should print 28---"
    movements = []
    A_schedule = [10, 1, 5, 10]
    B_schedule = [5, 2, 3, 15]
    # for i in range(len(A_schedule)):
    #     movements.extend('i')
    #     movements[i] = i
    print recursive('', 0, 0)
    # print movements
    print "---Should print 11---"
    A_schedule = [1, 2, 3, 4]
    B_schedule = [4, 3, 2, 1]
    print recursive('', 0, 0)
    print "---Should print 17---"
    A_schedule = [1, 2, 3, 10]
    B_schedule = [4, 3, 8, 1]
    print recursive('', 0, 0)
