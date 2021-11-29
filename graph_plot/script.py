import os
import random
from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt

def plot(opt_df, non_opt_df):
    # gca stands for 'get current axis'
    ax = plt.gca()
    opt_df.plot(kind='line',x='problem_size',y='time',ax=ax, marker='o')
    non_opt_df.plot(kind='line',x='problem_size',y='time', color='red', ax=ax, marker='o')
    plt.xlabel('Problem size')
    plt.ylabel('CPU time (in seconds)')
    plt.title('CPU time vs Problem size')
    plt.legend(['Time taken by efficient version (in s)', 'Time taken by basic version (in s)'])
    plt.savefig('CPUPlot.png')
    plt.show()
    ax = plt.gca()
    opt_df.plot(kind='line',x='problem_size',y='memory',ax=ax, marker='o')
    non_opt_df.plot(kind='line',x='problem_size',y='memory', color='red', ax=ax, marker='o')
    plt.xlabel('Problem size')
    plt.ylabel('Memory (in Kb)')
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
    ct = 100
    string_list = generate_random_strings(ct)
    writeToFile(string_list)
    optimized, non_optimized = [], []
    for ct in range(len(string_list)):
        os.system(f'python efficient.py ./files/input{ct+1}.txt ./files/efficient/output{ct+1}.txt')
        os.system(f'python basic.py ./files/input{ct+1}.txt ./files/basic/output{ct+1}.txt')
        time, memory, X_len, Y_len = readfile(f'./files/efficient/output{ct+1}.txt')
        optimized.append({'time': time, 'memory': memory, 'X_len': X_len, 'Y_len': Y_len, 'problem_size': X_len*Y_len})
        time, memory, X_len, Y_len = readfile(f'./files/basic/output{ct+1}.txt')
        non_optimized.append({'time': time, 'memory': memory, 'X_len': X_len, 'Y_len': Y_len, 'problem_size': X_len*Y_len})
    opt_pd = pd.DataFrame(optimized)
    non_opt_pd = pd.DataFrame(non_optimized)
    plot(opt_pd, non_opt_pd)

if __name__ == '__main__':
    main()