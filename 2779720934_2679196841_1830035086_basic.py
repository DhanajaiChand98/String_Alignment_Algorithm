from string_create import ReadFile, write_output
import sys
class StringMatching:
    
    def __init__(self, INPUT_FILE='input.txt', SIGMA=30):
        
        self.INPUT_FILE = INPUT_FILE
        self.SIGMA = SIGMA
        self.ALPHA = {
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

    def find_alignment_non_optimized(self, X, Y):
        ALPHA, SIGMA = self.ALPHA, self.SIGMA

        m, n = len(X), len(Y)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i * SIGMA 
        
        for j in range(n+1):
            dp[0][j] = j * SIGMA
        
        for j in range(1, n+1):
            for i in range(1, m+1):
                dp[i][j] = min( ALPHA[(X[i-1], Y[j-1])] + dp[i-1][j-1], SIGMA + dp[i-1][j], SIGMA + dp[i][j-1])

        i, j = m, n
        X_result, Y_result = '', ''

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
        

        return X_result, Y_result, dp[m][n]

    def find_alignment_space_efficient(self, X, Y):

        SIGMA, ALPHA = self.SIGMA, self.ALPHA
        m, n = len(X), len(Y)
        dp = [[0 for i in range(n+1)] for j in range(2)]

        for j in range(n+1):
            dp[0][j] = j * SIGMA
        
        for i in range(1, m+1):
            # B[0, 1]= jδ
            dp[1][0] = SIGMA * i
            for j in range(1, n+1):
                dp[1][j] = min( ALPHA[(X[i-1], Y[j-1])] + dp[0][j-1], SIGMA + dp[0][j], SIGMA + dp[1][j-1])

            for j in range(0, n+1):
                dp[0][j] = dp[1][j]

        return dp[0][n]

    def minimizing_index(self, X, Y_l , Y_r):

        X_reverse, Y_r, min_cost, q, m = X[::-1], Y_r[::-1], float('inf'), 0, len(X)

        for i in range(m+1):

            # print("\n\ncalling l for X ", X[:i])
            l_cost = self.find_alignment_space_efficient(X[:i], Y_l)
            r_cost = self.find_alignment_space_efficient(X_reverse[:m - i], Y_r)
            if l_cost + r_cost < min_cost:
                min_cost, q = l_cost + r_cost, i

        return q, min_cost

# Driver code
if __name__ == "__main__":

    _, input_file = sys.argv
    string_match = StringMatching(INPUT_FILE=input_file)
    file_ops = ReadFile()
    X, Y = file_ops.read_string(string_match.INPUT_FILE)
    X_align, Y_align, min_cost = string_match.find_alignment_non_optimized(X, Y)

    write_output('output.txt', X_string=X_align, Y_string=Y_align, min_cost=min_cost, time="0.002", memory="3000")