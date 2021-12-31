import matplotlib as mpl
import matplotlib.pyplot as plt
from itertools import product

from IPython.display import display
from z3 import *

ca_solver = Solver()  # create an instance of a Z3 CSP solver

F = Int('F')  # create an z3.Int type variable instance called "F"
ca_solver.add(0 <= F, F <= 9)  # add constraints to the solver: 0 <= F <= 9
O = Int('O')
ca_solver.add(0 <= O, O <= 9)
U = Int('U')
ca_solver.add(0 <= U, U <= 9)
R = Int('R')
ca_solver.add(0 <= R, R <= 9)
T = Int('T')
ca_solver.add(0 <= T, T <= 9)
W = Int('W')
ca_solver.add(0 <= W, W <= 9)

# Add constraints prohibiting leading digits F & T from taking the value 0
ca_solver.add(F != 0, T != 0)

# Add a Distinct constraint for all the variables
ca_solver.add(Distinct([F, O, R, T, U, W]))
# ca_solver.add(F != O, O != U, U != R, R != T, T != W)

# Required variables and/or constraints to solve the cryptarithmetic puzzle
# Alternate solution using column-wise sums with carry values
c10 = Int('c10')
c100 = Int('c100')
c1000 = Int('c1000')

ca_solver.add(*[And(c >= 0, c <= 9) for c in [c10, c100, c1000]])
ca_solver.add(O + O == R + 10 * c10)
ca_solver.add(W + W + c10 == U + 10 * c100)
ca_solver.add(T + T + c100 == O + 10 * c1000)
ca_solver.add(F == c1000)

# Primary solution using single constraint for the cryptarithmetic equation
# ca_solver.add((T + T)*10**2 + (W + W)*10**1 + (O + O)*10**0 == F*10**3 + O*10**2 + U*10**1 + R*10**0)

assert ca_solver.check(
) == sat, "Uh oh...the solver did not find a solution. Check your constraints."
print("\n")
print("  T W O  :    {} {} {}".format(ca_solver.model()
                                      [T], ca_solver.model()[W], ca_solver.model()[O]))
print("+ T W O  :  + {} {} {}".format(ca_solver.model()
                                      [T], ca_solver.model()[W], ca_solver.model()[O]))
print("-------- :  -------")
print("F O U R  :  {} {} {} {}".format(ca_solver.model()[
      F], ca_solver.model()[O], ca_solver.model()[U], ca_solver.model()[R]))

"""
    S E N D
+   M O R E
_______________
  M O N E Y
"""
ca_solver2 = Solver()  # create an instance of a Z3 CSP solver

S = Int('S')
ca_solver2.add(0 <= S, S <= 9)
E = Int('E')
ca_solver2.add(0 <= E, E <= 9)
N = Int('N')
ca_solver2.add(0 <= N, N <= 9)
D = Int('D')
ca_solver2.add(0 <= D, D <= 9)
M = Int('M')
ca_solver2.add(0 <= M, M <= 9)
OO = Int('OO')
ca_solver2.add(0 <= OO, OO <= 9)
RR = Int('RR')
ca_solver2.add(0 <= RR, RR <= 9)
Y = Int('Y')
ca_solver2.add(0 <= Y, Y <= 9)

ca_solver2.add(S != 0)
ca_solver2.add(M != 0)

ca_solver2.add(Distinct([S, E, N, D, M, OO, RR, Y]))

C10 = Int('C10')
C100 = Int('C100')
C1000 = Int('C1000')
C10000 = Int('C10000')

ca_solver2.add(*[And(C >= 0, C <= 9) for C in [C10, C100, C1000, C10000]])
ca_solver2.add(D + E == Y + 10 * C10)
ca_solver2.add(N + RR + C10 == E + 10 * C100)
ca_solver2.add(E + OO + C100 == N + 10 * C1000)
ca_solver2.add(S + M + C1000 == OO + 10 * C10000)
ca_solver2.add(M == C10000)

assert ca_solver2.check(
) == sat, "Uh oh...the solver did not find a solution. Check your constraints."
print("\n")
print("  S E N D  :    {} {} {} {} ".format(ca_solver2.model()
                                            [S], ca_solver2.model()[E], ca_solver2.model()[N], ca_solver2.model()[D]))
print("+ M O R E  :  + {} {} {} {}".format(ca_solver2.model()
                                           [M], ca_solver2.model()[OO], ca_solver2.model()[RR], ca_solver2.model()[E]))
print("---------  :  ---------")
print("M O N E Y  :  {} {} {} {} {}".format(ca_solver2.model()[
      M], ca_solver2.model()[OO], ca_solver2.model()[N], ca_solver2.model()[E], ca_solver2.model()[Y]))


"""
   T  H  I  S
+        I  S
      H  I  S
--------------
C  L  A  I  M
"""

ca_solver3 = Solver()

TT = Int('T')
ca_solver3.add(0 <= TT, TT <= 9)
H = Int('H')
ca_solver3.add(0 <= H, H <= 9)
I = Int('I')
ca_solver3.add(0 <= I, I <= 9)
SS = Int('S')
ca_solver3.add(0 <= SS, SS <= 9)
CC = Int('C')
ca_solver3.add(0 <= CC, CC <= 9)
L = Int('L')
ca_solver3.add(0 <= L, L <= 9)
A = Int('A')
ca_solver3.add(0 <= A, A <= 9)
MM = Int('M')
ca_solver3.add(0 <= MM, MM <= 9)

ca_solver3.add(TT != 0, I != 0, H != 0, CC != 0)
ca_solver3.add(Distinct([TT, H, I, SS, CC, L, A, MM]))

x10 = Int('c10')
x100 = Int('c100')
x1000 = Int('c1000')
x10000 = Int('c10000')

ca_solver3.add(* [And(x >= 0, x <= 9)
                  for x in [x10, x100, x1000, x10000]])

ca_solver3.add(SS + SS + SS == MM + 10 * x10)
ca_solver3.add(I + I + I + x10 == I + 10 * x100)
ca_solver3.add(H + H + x100 == A + 10 * x1000)
ca_solver3.add(TT + x1000 == L + 10 * x10000)
ca_solver3.add(CC == x10000)

assert ca_solver3.check(
) == sat, "Uh oh...the solver did not find a solution. Check your constraints."
print("\n")
print("  T H I S  :    {} {} {} {} ".format(ca_solver3.model()
                                            [TT], ca_solver3.model()[H], ca_solver3.model()[I], ca_solver3.model()[SS]))
print("+     I S  :  +     {} {}".format(ca_solver3.model()
                                         [I], ca_solver3.model()[SS]))
print("+   H I S  :  +   {} {} {}".format(ca_solver3.model()
                                          [H], ca_solver3.model()[I], ca_solver3.model()[SS]))
print("---------  :  ---------")
print("C L A I M  :  {} {} {} {} {}".format(ca_solver3.model()[
      CC], ca_solver3.model()[L], ca_solver3.model()[A], ca_solver3.model()[I], ca_solver3.model()[M]))

"""
   H  E  R  E
+     S  H  E
-------------
C  O  M  E  S
"""

ca_solver4 = Solver()

hh = Int('H')
ca_solver4.add(0 <= hh, hh <= 9)
ee = Int('E')
ca_solver4.add(0 <= ee, ee <= 9)
rr = Int('R')
ca_solver4.add(0 <= rr, rr <= 9)
ss = Int('S')
ca_solver4.add(0 <= ss, ss <= 9)
cc = Int('C')
ca_solver4.add(0 <= cc, cc <= 9)
oo = Int('O')
ca_solver4.add(0 <= oo, oo <= 9)
mm = Int('M')
ca_solver4.add(0 <= mm, mm <= 9)

ca_solver4.add(hh != 0, ss != 0, cc != 0)
ca_solver4.add(Distinct([hh, ee, rr, ss, cc, oo, mm]))

y10 = Int('c10')
y100 = Int('c100')
y1000 = Int('c1000')
y10000 = Int('c10000')

ca_solver4.add(* [And(y >= 0, y <= 9) for y in (y10, y100, y1000, y10000)])

ca_solver4.add(ee + ee == ss + 10 * y10)
ca_solver4.add(rr + hh + y10 == ee + 10 * y100)
ca_solver4.add(ee + ss + y100 == mm + 10 * y1000)
ca_solver4.add(hh + y1000 == oo + 10 * y10000)
ca_solver4.add(cc == y10000)

assert ca_solver4.check(
) == sat, "Uh oh...the solver did not find a solution. Check your constraints."
print("\n")
print("  H E R E  :    {} {} {} {} ".format(ca_solver4.model()
                                            [hh], ca_solver4.model()[ee], ca_solver4.model()[rr], ca_solver4.model()[ee]))
print("+   S H E  :  +   {} {} {}".format(ca_solver4.model()
                                          [ss], ca_solver4.model()[hh], ca_solver4.model()[ee]))
print("---------  :  ---------")
print("C O M E S  :  {} {} {} {} {}".format(ca_solver4.model()[
      cc], ca_solver4.model()[oo], ca_solver4.model()[mm], ca_solver4.model()[ee], ca_solver4.model()[ss]))
print("\n")

"WHAT + WAS + THY == CAUSE"

"HIS + HORSE + IS == SLAIN"

"HERE + SHE == COMES"

"FOR + LACK + OF == TREAD"

"I + WILL + PAY + THE == THEFT"
