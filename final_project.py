# constants
INPUT_FILE = "input.txt"
SIGMA = 30
ALPHA = {
        ('A', 'A') : 0,
        ('A', 'C') : 110,
        ('A', 'G') : 48,
        ('A', 'T') : 94,
        ('C', 'A') : 110,
        ('C', 'C') : 0,
        ('C', 'G') : 118,
        ('C', 'T') : 48,
        ('G', 'A') : 48,
        ('G', 'C') : 118,
        ('G', 'G') : 0,
        ('G', 'T') : 110,
        ('T', 'A') : 94,
        ('T', 'C') : 48,
        ('T', 'G') : 110,
        ('T', 'T') : 0,
}

def find_alignment_non_optimized(X, Y):
    global ALPHA, SIGMA

    # print("X : ", X)
    # print("Y : ", Y)

    m = len(X)
    n = len(Y)

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i * SIGMA 
    
    for j in range(n+1):
        dp[0][j] = j * SIGMA
    
    for j in range(1, n+1):
        for i in range(1, m+1):
            dp[i][j] = min( ALPHA[(X[i-1], Y[j-1])] + dp[i-1][j-1], SIGMA + dp[i-1][j], SIGMA + dp[i][j-1])

    # answer in dp[m, n]
    # backtracking

    i = m
    j = n

    # print("cost of alignment: ", dp[m][n])

    X_result = ''
    Y_result = ''

    while i > 0 and j > 0:

        if (dp[i][j] == ALPHA[(X[i-1], Y[j-1])] + dp[i-1][j-1]):
            X_result = X[i-1] + X_result 
            Y_result = Y[j-1] + Y_result
            i -= 1
            j -= 1
            
        elif (dp[i][j] == SIGMA + dp[i-1][j]):
            X_result = X[i-1] + X_result
            Y_result = '_' + Y_result    
            i -= 1

        else:
            X_result = '_' + X_result
            Y_result = Y[j-1] + Y_result
            j -= 1

        pass
    
    if i > 0:
        while i != 0:
            X_result = X[i-1] + X_result
            Y_result = '_' + Y_result
            i -= 1
        
    elif j > 0:
        while j != 0:
            X_result = '_' + X_result
            Y_result = Y[j-1] + Y_result
            j -= 1
    
    # print("X aligned : ", X_result)
    # print("Y aligned : ", Y_result)

    return X_result, Y_result, dp[m][n]

def find_alignment_space_efficient(X, Y):

    m = len(X)
    n = len(Y)

    # print("x : ", X)
    # print("y : ", Y)


    dp = [[0 for i in range(n+1)] for j in range(2)]

    for j in range(n+1):
        dp[0][j] = j * SIGMA
    

    # dp[1][0]  = SIGMA

    for i in range(1, m+1):
        # B[0, 1]= jδ
        dp[1][0] = SIGMA * i
        for j in range(1, n+1):
            dp[1][j] = min( ALPHA[(X[i-1], Y[j-1])] + dp[0][j-1], SIGMA + dp[0][j], SIGMA + dp[1][j-1])

        for j in range(0, n+1):
            dp[0][j] = dp[1][j]

    # print("space optimized cost of alignment: ", dp[0][n])
    return dp[0][n]

def minimizing_index(X, Y_l , Y_r):

    Y_r = Y_r[::-1]

    X_reverse = X[::-1]

    min_cost = float("inf")
    q = 0

    # print("Y_l : ", Y_l)
    # print("Y_r : ", Y_r)
    # print("X : ", X)
    # print("X_reverse : ", X_reverse)

    m = len(X)

    for i in range(m+1):

        # print("\n\ncalling l for X ", X[:i])
        l_cost = find_alignment_space_efficient(X[:i], Y_l)
        # print("lcost, ", l_cost)
        # print("calling r for X_rev: ", X_reverse[:m - i])
        r_cost = find_alignment_space_efficient(X_reverse[:m - i], Y_r)
        # print("rcost, ", r_cost)
        # print("at ", i, " l_cost: ", l_cost, " r_cost : ", r_cost)
        if l_cost + r_cost < min_cost:
            # print("resetting min")
            min_cost = l_cost + r_cost
            q = i

    return q, min_cost

def find_alignment_binary_search_optimized(X, Y):
    global ALPHA, SIGMA

    m = len(X)
    n = len(Y)

    if m <= 2 or n <=2:
        return find_alignment_non_optimized(X, Y)

    q, min_cost = minimizing_index(X, Y[ : n//2], Y[n//2 :])

    X_left, Y_left, _ = find_alignment_binary_search_optimized(X[ : q], Y[ : n//2])
    X_right, Y_right, _ = find_alignment_binary_search_optimized(X[q : ], Y[n//2 : ])

    return X_left + X_right, Y_left + Y_right, min_cost


def main():
    global ALPHA

    with open(INPUT_FILE, "rb") as f:
        lines = f.readlines()

        str_b1 = lines[0]

        str_b2 = lines[1]

    Y = "ACAAT"
    X = "ACTAA"

    X_align, Y_align, min_cost = find_alignment_non_optimized(X, Y)
    # X_align, Y_align, min_cost = find_alignment_binary_search_optimized(X, Y)
    
    print("X aligned: ", X_align)
    print("Y aligned: ", Y_align)
    print("final cost: ", min_cost)

if __name__ == "__main__":
    main()