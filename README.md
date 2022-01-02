# DNA MATCHING USING STRING ALIGNMENT ALGORITHM
Introduction

Basic algorithm implementation
The basic algorithm uses a 2d matrix of size n*m to store the similarity between string X -> [0…i] and Y -> [0…j] for i -> [0, n] and j -> [0, m]. We set initial values as SIGMA*k for both row 1 and column 1 of OPT array. Then, using two nested loops, we compute OPT values, OPT[i][j], using minimum of cases of using both the string and incurring a penalty of ALPHA[i][j] or matching either character X[i] or Y[j] with a gap. After obtaining the optimal results, we backtrack using a while loop and at each step we construct the matched string for both X and Y, combing the characters with each other or with gaps depending on the OPT value of the current step and the value in possible predecessors.

Space Efficient algorithm
The space efficient algorithm computes the matched string but using a constant number of rows thereby reducing the space complexity of O(m + n). For constructing the results, we use divide and conquer wherein we divide the Y string into half and divide the X string based on an optimal point ‘q’ which minimizes the penalty for Y_left, X -> [1…q]  and Y_right (reversed), X -> [q+1…m] (reversed). To find this ‘q’ value we pass the X and Y string to subroutine ‘minimizing index’ where the cost is calculated for each split of X string and the minimizing index is returned. The algorithm proceeds to recursively call the routine for Y_left, X -> [1…q]  and Y_right (reversed), X -> [q+1…m]. On getting the results from recursive calls, we simply combine the results and return. The base case is called when either X or Y is of length 2. For the base case we pass the strings to our basic algorithm as the base case will find the optimal solution in efficient space, because either the number of rows or columns in the OPT array will be of length 2.
 

Testing
The implemented algorithms were tested using the sample test cases provided and the results were matched. Also, created multiple test cases manually and using random string generate script which was given as input to the programs. Manual test cases included strings of smaller length whose misalignment cost were calculated manually and verified using the developed algorithms.
 

Time and Space complexity analysis
The time complexity of the basic and efficient algorithm for sequence alignment is O(m*n) (where m and n denote the length of input string X and y respectively).
The overall space complexity of the basic algorithm is O(m*n) whereas for the efficient algorithm it is O(m + n) whichever form the rows.
 

Results and Discussions
A random set of strings of varying length were generated to evaluate the overall CPU memory (in Kb) usage and CPU runtime (in seconds) plot against the problem size. Implemented a random input string generation module which returns 18 pairs of strings of varying length (starting from length = 1 and incrementing it by 60 till 1024). The generated strings only include the DNA characters (A, C, T and G). The generated strings are used as input for both the basic and efficient string alignment algorithm to derive the CPU memory and time usage stats which is used for plotting the line graph. Prominent python plotting library, Matplotlib, was used to draw comparison of the overall CPU memory and time usage against the problem size (which denotes the product length of output strings). In order to reduce noise and generalize our data points, the basic and efficient algorithms were run multiple times (>10) using the same input files to generate statistics. The results were averaged before plotting the data.
 

CPU time vs Problem Size plot
A separate module has been implemented in the ‘script.py’ file (inside graph_plot folder), which measures the time taken to execute the basic algorithm and generate output files using the ‘time’ Python library. The difference in the monitored start and end time is written into an output file in seconds rounded upto 3 decimals. We can observe in the plot (fig 1: CPUPlot.png) that the time taken by the space efficient version algorithm is approximately double of the time taken by the basic version. The basic implementation has execution time much lower compared to the efficient implementation. The reason being that the number of underlying operations involved in the efficient algorithm is much higher when compared to the basic implementation. Also, it is necessary to highlight the multiple recursive and method calls involved in the space efficient algorithm which leads to increased time taken as compared to the basic implementation.
 

CPU memory usage vs Problem Size plot
In the same ‘script.py’ file, we are monitoring the CPU memory usage of the algorithms using the ‘psutil’ library which helps in getting the Resident Set Size (RSS) memory info for the current process using the current process id. Using the ‘.rss()’ method we get the RSS value in Bytes which is converted into Kilobytes (dividing by 1024) before plotting the line graph. We can infer from the memory plot (fig 2: MemoryPlot.png) that the basic version consumes higher memory than the efficient algorithm because the basic algorithm uses n time m rows table for computation as opposed to the efficient algorithm which only requires a table size 2*(length of X string). Therefore, as input size increases to very large values, we are expected to have much more memory consumption for the basic version which may take more time to process also.


Steps to run the project:
Requirements: Python 3.7+
1) Set up a python3 virtualenv using the venv command.
2) Install necessary packages from the requirements.txt using the below command:
	‘pip install -r requirements.txt’
3) Ensure the ‘input.txt’ file is created and present in the root directory of the project.
4) Run the basic and efficient algorithms using the below command:
	‘python3 2779720934_2679196841_1830035086_basic.py input.txt`
	‘python3 2779720934_2679196841_1830035086_efficient.py input.txt’
    Alternatively, the program can be run using the below shell commands:
	‘sh 2779720934_2679196841_1830035086_basic.sh’
	‘sh 2779720934_2679196841_1830035086_efficient.sh’
5) To generate the graph plot, visit the ‘graph_plot’ folder and run the ‘script.py’ files inside the folder.



Individual contribution
Dhananjai Chand:  Contributions include but not limited to:
	- Algorithm implementation & testing for space efficient and basic versions of the string matching algorithm.
	- Minor contributions in project report write-up, input string generation and graph plotting.
Sahil Vartak:  Contributions include but not limited to:
	- Code cleaning and worked on converting it to reusable and object oriented code.
	- Contributed towards generating plots, code testing and read/write operations of inputs and outputs to text files.
Vikrame Krishnan: Contributions include but not limited to:
	- Creating a script to generate random strings for testing and graph plotting.
	- Implemented a module to calculate the time and memory usage for the both the basic and efficient algorithm implementation. Further, coded the module to generate a time and memory usage plot and draw a comparison between the two algorithms.
	- Created the bash script, prepared the project report, contributed to input/ output operations to files and was involved in the algorithm testing using both custom and computer generated test cases.
