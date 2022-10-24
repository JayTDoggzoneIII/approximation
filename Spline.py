# -*- coding: utf-8 -*-
from sympy import Symbol, sqrt, cos, pi, nan
from math import prod, fabs, pi as num_pi, cos as num_cos
from random import uniform
from sympy.plotting import plot, plot_implicit
from sympy.polys.polytools import poly
from sympy.solvers import solve
from sympy.functions.elementary.piecewise import Piecewise
x = Symbol('x', real = True)

def f(t:float) -> float:
    return 3*t - num_cos(t) - 1;

def main() -> int:
    global l_ans, piece, deform
    a,b = 0, num_pi/2
    for n in [3,10,20]:
        print("with %d points"%n)
        h = b/(n-1)
        nodes = {k*h:f(k*h) for k in range(n)}
        nodes_list = list(nodes)
        l_s = []
        a_s = []
        for i in range(n-1):
            ai1, ai0 = Symbol('a%d1'%(i+1), real = True), Symbol('a%d0'%(i+1), real = True)
            a_s.append(ai1)
            a_s.append(ai0)
            l_s.append(ai1*x + ai0)
        to_solve = [l_s[0].subs(x,nodes_list[0]) - nodes[nodes_list[0]], l_s[-1].subs(x,nodes_list[-1]) - nodes[nodes_list[-1]]]
        for i in range(1,n-1):
            to_solve.append(l_s[i-1].subs(x,nodes_list[i]) - nodes[nodes_list[i]])
            to_solve.append(l_s[i].subs(x,nodes_list[i]) - nodes[nodes_list[i]])
        #for v in to_solve: print(v,'= 0')
        ans = solve(to_solve,*a_s)
        print(ans)
        l_ans = []
        for i in range(n-1):
            ai1, ai0 = Symbol('a%d1'%(i+1), real = True), Symbol('a%d0'%(i+1), real = True)
            l_ans.append((l_s[i].subs([(ai1,ans[ai1]),(ai0,ans[ai0])]),nodes_list[i],nodes_list[i+1]))
        for func,start,end in l_ans:
            print("S1,0(x) = %s,  from %.6f to %.6f"%(func, start, end))
        deform = []
        for i in range(n-1):
            #deform.append((l_ans[i][0],l_ans[i][1] <= x))
            deform.append((l_ans[i][0],x < l_ans[i][2]))
        piece = Piecewise(*deform)
        #print(piece)
        print()
        
    return 0;

if (__name__ == "__main__"):
    main()