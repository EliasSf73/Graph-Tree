# Checking basic test cases
# This is not going to be used for grading

import os
import sys
from pathlib import Path
import timeit
from miniexam5 import problem1, simulate_problem2

TIME_LIMIT = 5

def readline(f):
    return f.readline().strip()
def read_links(f, n):
    return [tuple(int(x) for x in readline(f).split()) for _ in range(n)]

def read_p1_input(file_path):
    with open(file_path) as f:
        n = int(readline(f))
        links = read_links(f, n)
    return links,
def read_p2_input(file_path):
    with open(file_path) as f:
        n, k = (int(x) for x in readline(f).split())
        links = read_links(f, n)
    return links, k
def read_output(file_path):
    with open(file_path) as f:
        n = int(readline(f))
        indices = [int(readline(f)) for _ in range(n)]
    return indices

def run_test(input_fn, problem_fn, input_path, output_path):
    inputs = input_fn(input_path)
    
    start = timeit.default_timer()
    output = problem_fn(*inputs)
    end = timeit.default_timer()

    solution = read_output(output_path)

    if end-start > TIME_LIMIT:
        result = 'Timeout'
    elif set(output) != set(solution):
        result = 'Wrong'
    else:
        result = 'Correct!'
    
    print(f'Testcase {tc_name:5s} - {result} ({end-start:.3f} sec)')

if __name__ == '__main__':
    sys.setrecursionlimit(3000)

    tc1_path = Path('tc1')
    tc2_path = Path('tc2')

    tc1 = []
    tc2 = []
    
    for file in os.listdir(tc1_path):
        if file.startswith('in') and file.endswith('.txt'):
            tc_name = file[2:-4]
            tc1.append(tc_name)
    for file in os.listdir(tc2_path):
        if file.startswith('in') and file.endswith('.txt'):
            tc_name = file[2:-4]
            tc2.append(tc_name)
    tc1.sort()
    tc2.sort()
    print('Testing Problem 1')
    for tc_name in tc1:
        in_path = tc1_path / f'in{tc_name}.txt'
        out_path = tc1_path / f'out{tc_name}.txt'
        run_test(read_p1_input, problem1, in_path, out_path)
    print('Testing Problem 2')
    for tc_name in tc2:
        in_path = tc2_path / f'in{tc_name}.txt'
        out_path = tc2_path / f'out{tc_name}.txt'
        run_test(read_p2_input, simulate_problem2, in_path, out_path)
