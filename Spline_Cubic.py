# -*- coding: utf-8 -*-
from sympy import Symbol, sqrt, cos, pi, nan, Abs
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
            ai3, ai2, ai1, ai0 = Symbol('a%d3'%(i+1), real = True), Symbol('a%d2'%(i+1), real = True), Symbol('a%d1'%(i+1), real = True), Symbol('a%d0'%(i+1), real = True)
            a_s.append(ai3)
            a_s.append(ai2)
            a_s.append(ai1)
            a_s.append(ai0)
            l_s.append(ai3*x*x*x + ai2*x*x + ai1*x + ai0)
        to_solve = [l_s[0].subs(x,nodes_list[0]) - nodes[nodes_list[0]], l_s[-1].subs(x,nodes_list[-1]) - nodes[nodes_list[-1]], ((l_s[0].diff(x)).diff(x)).subs(x,nodes_list[0]), ((l_s[-1].diff(x)).diff(x)).subs(x,nodes_list[-1])]
        for i in range(1,n-1):
            to_solve.append(l_s[i].subs(x,nodes_list[i]) - nodes[nodes_list[i]])
            to_solve.append(l_s[i-1].subs(x,nodes_list[i]) - l_s[i].subs(x,nodes_list[i]))
            to_solve.append((l_s[i-1].diff(x)).subs(x,nodes_list[i]) - (l_s[i].diff(x)).subs(x,nodes_list[i]))
            to_solve.append(((l_s[i-1].diff(x)).diff(x)).subs(x,nodes_list[i]) - ((l_s[i].diff(x)).diff(x)).subs(x,nodes_list[i]))
        #for v in to_solve: print(v,'= 0')
        ans = solve(to_solve,*a_s)
        print(ans)
        l_ans = []
        for i in range(n-1):
            ai3, ai2, ai1, ai0 = Symbol('a%d3'%(i+1), real = True), Symbol('a%d2'%(i+1), real = True), Symbol('a%d1'%(i+1), real = True), Symbol('a%d0'%(i+1), real = True)
            l_ans.append((l_s[i].subs([(ai3,ans[ai3]), (ai2,ans[ai2]), (ai1,ans[ai1]),(ai0,ans[ai0])]),nodes_list[i],nodes_list[i+1]))
        for func,start,end in l_ans:
            print("S3,2(x) = %s,  from %.6f to %.6f"%(func, start, end))
        deform = []
        for i in range(n-1):
            #deform.append((l_ans[i][0],l_ans[i][1] <= x))
            deform.append((l_ans[i][0],x < l_ans[i][2]))
        piece = Piecewise(*deform)
        r = -1
        x_m = 0
        for i in range(1000):
            tmp = uniform(a,b)
            r_l_n = fabs(f(tmp) - piece.subs(x,tmp))
            if (r_l_n > r): 
                r = r_l_n
                x_m = tmp
        print("Отклонение %.9f в точке %.6f"%(r,x_m))        
        #print(piece)
        print()
    error = Abs(3*x - cos(x) - 1 - piece)
    p3 = plot(error, xlim = (0,pi/2), ylim = (0,0.001), show = True, line_color = "RED", title = "Error with %d points"%n)
    
    for n in [3,10,20]:
        print("with %d points"%n)
        x_s = sorted([((b-a)*num_cos(num_pi*(2*i+1)/(2*n+2)) + (b+a))/2 for i in range(n)])
        nodes = {x_s[i]:f(x_s[i]) for i in range(n)}
        nodes_list = list(nodes)        
    
        l_s = []
        a_s = []
        for i in range(n-1):
            ai3, ai2, ai1, ai0 = Symbol('a%d3'%(i+1), real = True), Symbol('a%d2'%(i+1), real = True), Symbol('a%d1'%(i+1), real = True), Symbol('a%d0'%(i+1), real = True)
            a_s.append(ai3)
            a_s.append(ai2)
            a_s.append(ai1)
            a_s.append(ai0)
            l_s.append(ai3*x*x*x + ai2*x*x + ai1*x + ai0)
        to_solve = [l_s[0].subs(x,nodes_list[0]) - nodes[nodes_list[0]], l_s[-1].subs(x,nodes_list[-1]) - nodes[nodes_list[-1]], ((l_s[0].diff(x)).diff(x)).subs(x,nodes_list[0]), ((l_s[-1].diff(x)).diff(x)).subs(x,nodes_list[-1])]
        for i in range(1,n-1):
            to_solve.append(l_s[i].subs(x,nodes_list[i]) - nodes[nodes_list[i]])
            to_solve.append(l_s[i-1].subs(x,nodes_list[i]) - l_s[i].subs(x,nodes_list[i]))
            to_solve.append((l_s[i-1].diff(x)).subs(x,nodes_list[i]) - (l_s[i].diff(x)).subs(x,nodes_list[i]))
            to_solve.append(((l_s[i-1].diff(x)).diff(x)).subs(x,nodes_list[i]) - ((l_s[i].diff(x)).diff(x)).subs(x,nodes_list[i]))
        #for v in to_solve: print(v,'= 0')
        ans = solve(to_solve,*a_s)
        print(ans)
        l_ans = []
        for i in range(n-1):
            ai3, ai2, ai1, ai0 = Symbol('a%d3'%(i+1), real = True), Symbol('a%d2'%(i+1), real = True), Symbol('a%d1'%(i+1), real = True), Symbol('a%d0'%(i+1), real = True)
            l_ans.append((l_s[i].subs([(ai3,ans[ai3]), (ai2,ans[ai2]), (ai1,ans[ai1]),(ai0,ans[ai0])]),nodes_list[i],nodes_list[i+1]))
        for func,start,end in l_ans:
            print("S3,2(x) = %s,  from %.6f to %.6f"%(func, start, end))
        deform = []
        for i in range(n-1):
            #deform.append((l_ans[i][0],l_ans[i][1] <= x))
            deform.append((l_ans[i][0],x < l_ans[i][2]))
        piece = Piecewise(*deform)
        r = -1
        x_m = 0
        for i in range(1000):
            tmp = uniform(a,b)
            r_l_n = fabs(f(tmp) - piece.subs(x,tmp))
            if (r_l_n > r): 
                r = r_l_n
                x_m = tmp
        print("Отклонение %.9f в точке %.6f"%(r,x_m))        
        #print(piece)
        print()
    error = Abs(3*x - cos(x) - 1 - piece)
    p3 = plot(error, xlim = (0,pi/2), ylim = (0,0.001), show = True, line_color = "RED", title = "Error with %d Opt points"%n)
    return 0;

if (__name__ == "__main__"):
    #pass
    main()