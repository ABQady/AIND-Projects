import matplotlib as mpl
import matplotlib.pyplot as plt
import time

from itertools import product
from IPython.display import display
from util import displayBoard
from z3 import *
from itertools import chain

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from sympy import *

runtimes = []
solutions = []
sizes = [8, 16, 32, 64]


def Abs(x):
    return If(x >= 0, x, -x)


def nqueens(N):
    nq_solver = Solver()
    queens = [Int('Q{}'.format(i)) for i in range(N)]
    nq_solver.add(*chain(*[(0 <= q, q < N)
                           for q in queens]))  # valid range constraint
    nq_solver.add(Distinct(queens))  # different row constraint
    for i, q1 in enumerate(queens):
        for j, q2 in enumerate(queens):
            if i == j:
                continue
            # different diagonal constraint
            nq_solver.add(Abs(q1 - q2) != abs(i - j))
    return nq_solver


for N in sizes:
    nq_solver = nqueens(N)
    start = time.perf_counter()
    assert nq_solver.check(
    ), "Uh oh...The solver failed to find a solution. Check your constraints."
    end = time.perf_counter()
    print("{}-queens: {}ms".format(N, (end-start) * 1000))
    runtimes.append((end - start) * 1000)
    solutions.append(nq_solver.model())

plt.plot(sizes, runtimes)

s = solutions[0]
displayBoard([(int(str(v)[1:]), s[v].as_long()) for v in s], len(s))
