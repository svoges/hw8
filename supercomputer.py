def recursive(machine, hour):
    # the initial state
    if hour == 0:
        return max(
        A_schedule[hour] + recursive('A', hour + 1),
        B_schedule[hour] + recursive('B', hour + 1)
        )
    # the base case, when the length of the list is equal to the hour
    elif len(A_schedule) == hour + 1:
        if machine == 'A':
            return A_schedule[hour]
        if machine == 'B':
            return B_schedule[hour]
        else:
            return 0
    # if the state of the machine is currently A
    elif machine == 'A':
        return max(
        A_schedule[hour] + recursive('A', hour + 1),
        0 + recursive('move_to_B', hour + 1)
        )
    # if the state of the machine is currently B
    elif machine == 'B':
        return max(
        B_schedule[hour] + recursive('B', hour + 1),
        0 + recursive('move_to_A', hour + 1)
        )
    # if the state of the machine is the first at A
    elif machine == 'move_to_A':
        return A_schedule[hour] + recursive('A', hour + 1)
    # if the state of the machine is the first at B
    elif machine == 'move_to_B':
        return B_schedule[hour] + recursive('B', hour + 1)
    # the what the fuck why is it here state
    else:
        print "you printed this and i have absolutely no idea why"

def iterative(A_schedule, B_schedule):
    hour = len(A_schedule)




if __name__ == "__main__":
    print "---Should print 28---"
    A_schedule = [10, 1, 5, 10]
    B_schedule = [5, 2, 3, 15]
    print recursive('', 0)
    print "---Should print 11---"
    A_schedule = [1, 2, 3, 4]
    B_schedule = [4, 3, 2, 1]
    print recursive('', 0)
    print "---Should print 17---"
    A_schedule = [1, 2, 3, 10]
    B_schedule = [4, 3, 8, 1]
    print recursive('', 0)