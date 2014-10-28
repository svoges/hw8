def recursive_subsequence(A, B):
    if len(B) == 0 and len(A) != 0:
        return False
    if len(A) == 0:
        return True
    if A[-1] == B[-1]:
        return recursive_subsequence(A[:-1], B[:-1])
    else:
        return recursive_subsequence(A, B[:-1])


def iterative_subsequence(A, B):
    for i in range(len(B)):
        if len(A) >= 1:
            if A[0] == B[i]:
                A = A[1:]
    if len(A) == 0:
        return True
    return False

if __name__ == "__main__":
    #recursive test
    print "---recursive test---"
    A = "yes"
    B = "well ysdfes dad"
    print "True: " + str(recursive_subsequence(A, B))
    A = "no"
    B = "well ysdfes dad"
    print "False: " + str(recursive_subsequence(A, B))

    #iterative test
    print "---recursive test---"
    A = "yes"
    B = "well ysdfes dad"
    print "True: " + str(iterative_subsequence(A, B))
    A = "no"
    B = "well ysdfes dad"
    print "False: " + str(iterative_subsequence(A, B))
