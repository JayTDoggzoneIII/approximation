# -*- coding: utf-8 -*-
from sympy import Symbol, sqrt, cos, pi
from math import prod, fabs, pi as num_pi, cos as num_cos
from random import uniform
from sympy.plotting import plot, plot_implicit
from sympy.polys.polytools import poly
x = Symbol('x', real = True)

def f(t:float) -> float:
    return 3*t - num_cos(t) - 1;

def main() -> int:
    global s, s1
    a,b = 0, num_pi/2
    for n in [3,10,20]:
        h = b/n
        nodes = {k*h:f(k*h) for k in range(n)}
        nodes_list = list(nodes)
        s = 0
        for i in range(n):
    
            l_i = poly(1,x)
            for j in range(i):
                l_i *= (x - nodes_list[j])/(nodes_list[i] - nodes_list[j])
            for j in range(i+1,n):
                l_i *= (x - nodes_list[j])/(nodes_list[i] - nodes_list[j])
    
            s += l_i*nodes[nodes_list[i]]
        print("L%d ="%n, s.as_expr())
        r = -1
        h = b/1000
        x_m = 0
        for i in range(1000):
            tmp = uniform(a,b)
            r_l_n = fabs(f(tmp) - s(tmp))
            if (r_l_n > r): 
                r = r_l_n
                x_m = tmp
        print("Отклонение %.9f в точке %.6f"%(r,x_m))
        
        p3 = plot(s.as_expr(), xlim = (-5,5), ylim = (-17,14), show = False, line_color = "RED", title = "L%d"%n)
        p4 = plot(3*x - cos(x) - 1, xlim = (-5,5), ylim = (-17,14), show = False)
        p5 = plot((x-pi/2)*10**9, xlim = (-5,5), ylim = (-17,14), show = False, line_color = "GREEN")
        p6 = plot(x*10**9, xlim = (-5,5), ylim = (-17,14), show = False, line_color = "GREEN")
        p3.append(p4[0])
        p3.append(p5[0])
        p3.append(p6[0])
        p3.show()        
    
    
    for n in [3,10,20]:
        x_s = sorted([((b-a)*num_cos(num_pi*(2*i+1)/(2*n+2)) + (b+a))/2 for i in range(n)])
        nodes = {x_s[i]:f(x_s[i]) for i in range(n)}
        nodes_list = list(nodes)
        s = 0
        for i in range(n):
    
            l_i = poly(1,x)
            for j in range(i):
                l_i *= (x - nodes_list[j])/(nodes_list[i] - nodes_list[j])
            for j in range(i+1,n):
                l_i *= (x - nodes_list[j])/(nodes_list[i] - nodes_list[j])
    
            s += l_i*nodes[nodes_list[i]]
        print("Lopt%d ="%n, s.as_expr())
        r = -1
        h = b/1000
        x_m = 0
        for i in range(1000):
            tmp = uniform(a,b)
            r_l_n = fabs(f(tmp) - s(tmp))
            if (r_l_n > r): 
                r = r_l_n
                x_m = tmp
        print("Отклонение %.9f в точке %.6f"%(r,x_m))        
        
        p3 = plot(s.as_expr(), xlim = (-5,5), ylim = (-17,14), show = False, line_color = "RED", title = "Lopt%d"%n)
        p4 = plot(3*x - cos(x) - 1, xlim = (-5,5), ylim = (-17,14), show = False)
        p5 = plot((x-pi/2)*10**9, xlim = (-5,5), ylim = (-17,14), show = False, line_color = "GREEN")
        p6 = plot(x*10**9, xlim = (-5,5), ylim = (-17,14), show = False, line_color = "GREEN")
        p3.append(p4[0])
        p3.append(p5[0])
        p3.append(p6[0])
        p3.show()        
    #p4.show()    
    
    return 0;

if (__name__ == "__main__"):
    main()