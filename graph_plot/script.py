import os
import random
from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt

# The scale parameter converts the Y-axis to logarithmic scale
def plot(opt_df, non_opt_df, scale_y=True):
    # gca stands for 'get current axis'
    y_label = 'Scaled time(Logarithmic)' if scale_y else 'time'
    ax = plt.gca()
    opt_df.plot(kind='line',x='problem_size',y='time',ax=ax, marker='o')
    non_opt_df.plot(kind='line',x='problem_size',y='time', color='red', ax=ax, marker='o')
    if scale_y:
        plt.yscale('log')
    plt.xlabel('Problem size')
    plt.ylabel(f'CPU {"Log Scaled" if scale_y else ""} time (in seconds)')
    plt.title('CPU time vs Problem size')
    plt.legend(['Time taken by efficient version (in s)', 'Time taken by basic version (in s)'])
    plt.savefig('CPUPlot.png')
    plt.show()

    ax = plt.gca()
    opt_df.plot(kind='line',x='problem_size',y='memory',ax=ax, marker='o')
    non_opt_df.plot(kind='line',x='problem_size',y='memory', color='red', ax=ax, marker='o')
    plt.xlabel('Problem size')
    plt.ylabel(f'Memory usage (in Kb)')
    plt.title('Memory usage vs Problem size')
    plt.legend(['Memory usage by efficient version (in Kb)', 'Memory usage by basic version (in Kb)'])
    plt.savefig('MemoryPlot.png')
    plt.show()


DNA_CHARACTERS = 'ACTG'

def generate_random_strings(ct: int, varying_length=False) -> list:
    strings = []
    for ct in range(1, ct+1, 4):
        x = ''.join(random.choices(DNA_CHARACTERS, k=ct))
        y = ''.join(random.choices(DNA_CHARACTERS, k=ct))
        strings.append((x, y))
    return strings

def writeToFile(strings_list):
    for i in range(len(strings_list)):
        with open(f'./files/input{i+1}.txt', 'w') as f:
            f.write(f'{strings_list[i][0]} {strings_list[i][1]}')
    
def readfile(file_name):
    m = ''
    with open(file_name, 'r') as f:
        m = f.read()
    m = m.split('\n')
    time, memory, str = float(m[-3]), float(m[-2]), m[-1]
    X_len, Y_len = list(map(int, str.split(' ')))
    return time, memory, X_len, Y_len

def main():
    ct, iterations = 10, 20
    params = {}
    for itr in range(iterations):
        ct = 100
        string_list = generate_random_strings(ct)
        writeToFile(string_list)

        optimized, non_optimized = [], []
        for ct in range(len(string_list)):
            os.system(f'python efficient.py ./files/input{ct+1}.txt ./files/efficient/output{ct+1}.txt')
            os.system(f'python basic.py ./files/input{ct+1}.txt ./files/basic/output{ct+1}.txt')
            time, memory, X_len, Y_len = readfile(f'./files/efficient/output{ct+1}.txt')
            optimized.append({'time': time, 'memory': memory, 'X_len': X_len, 'Y_len': Y_len, 'problem_size': X_len+Y_len})
            time, memory, X_len, Y_len = readfile(f'./files/basic/output{ct+1}.txt')
            non_optimized.append({'time': time, 'memory': memory, 'X_len': X_len, 'Y_len': Y_len, 'problem_size': X_len+Y_len})
    
        if params.get(f'input'):
            opt, non_opt = params[f'input']
            params[f'input'] = [add_values(opt, optimized, iterations), add_values(non_opt, non_optimized, iterations)]
        else:
            params[f'input'] = [divide(optimized, iterations), divide(non_optimized, iterations)]

        print(f'Iteration {itr+1}/{iterations} done')
    optimized, non_optimized = params['input'][0], params['input'][1]
    opt_pd = pd.DataFrame(optimized)
    non_opt_pd = pd.DataFrame(non_optimized)
    plot(opt_pd, non_opt_pd, scale_y=False)


def add_values(prev, current, iterations=10):
    result = []
    for element in zip(prev, current):
        temp = {'time': element[0]['time'] + element[1]['time']/iterations,
                'memory': element[0]['memory'] + element[1]['memory']/iterations,
                'X_len': element[0]['X_len'] + element[1]['X_len']//iterations,
                'Y_len': element[0]['Y_len'] + element[1]['Y_len']//iterations,
                'problem_size': element[0]['problem_size'] + element[1]['problem_size']//iterations}
        result.append(temp)
    return result

def divide(result, iterations=10):
    for element in result:
        element['time'], element['memory'] = element['time']/iterations, element['memory']/iterations
        element['X_len'], element['Y_len'], element['problem_size'] = element['X_len']//iterations, element['Y_len']//iterations, element['problem_size']//iterations
    return result

if __name__ == '__main__':
    main()