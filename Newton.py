# -*- coding: utf-8 -*-
from sympy import Symbol, sqrt, cos, pi, Abs
from math import prod, fabs, pi as num_pi, cos as num_cos
from random import uniform
from sympy.plotting import plot, plot_implicit
from sympy.polys.polytools import poly
x = Symbol('x', real = True)

def f(t:float) -> float:
    return 3*t - num_cos(t) - 1;

def div_dif(itr) -> float:
    if (len(itr) == 2): return (f(itr[1]) - f(itr[0]))/(itr[1] - itr[0])
    return (div_dif(itr[1:]) - div_dif(itr[:-1]))/(itr[-1] - itr[0])

def main() -> int:
    global s, s1
    a,b = 0, num_pi/2
    for n in [3,10,20]:
        h = b/n
        nodes = {k*h:f(k*h) for k in range(n)}
        nodes_list = list(nodes)
        s = f(nodes_list[0])
        prods = [poly(1,x)]
        for i in range(1,n):
            prods.append((x - nodes_list[i-1])*prods[i-1])
            n_i = div_dif(nodes_list[:i+1])*prods[i]
    
            s += n_i
        print("N%d ="%n, s.as_expr())
        r = -1
        h = b/1000
        x_m = 0
        for i in range(1000):
            tmp = uniform(a,b)
            r_l_n = fabs(f(tmp) - s.subs(x,tmp))
            if (r_l_n > r): 
                r = r_l_n
                x_m = tmp
        print("Отклонение %.6f в точке %.6f"%(r,x_m))
        
        p3 = plot(s.as_expr(), xlim = (-5,5), ylim = (-17,14), show = False, line_color = "RED", title = "N%d"%n)
        p4 = plot(3*x - cos(x) - 1, xlim = (-5,5), ylim = (-17,14), show = False)
        p5 = plot((x-pi/2)*10**9, xlim = (-5,5), ylim = (-17,14), show = False, line_color = "GREEN")
        p6 = plot(x*10**9, xlim = (-5,5), ylim = (-17,14), show = False, line_color = "GREEN")
        p3.append(p4[0])
        p3.append(p5[0])
        p3.append(p6[0])
        p3.show()        
    error = Abs(3*x - cos(x) - 1 - s.as_expr())
    p3 = plot(error, xlim = (0,pi/2), ylim = (0,1e-10), show = True, line_color = "RED", title = "Error with %d points"%n)

    for n in [3,10,20]:
        x_s = sorted([((b-a)*num_cos(num_pi*(2*i+1)/(2*n+2)) + (b+a))/2 for i in range(n)])
        nodes = {x_s[i]:f(x_s[i]) for i in range(n)}
        nodes_list = list(nodes)
        s = f(nodes_list[0])
        prods = [poly(1,x)]
        for i in range(1,n):
            prods.append((x - nodes_list[i-1])*prods[i-1])
            n_i = div_dif(nodes_list[:i+1])*prods[i]
    
            s += n_i
        print("Nopt%d ="%n, s.as_expr())
        r = -1
        x_m = 0
        for i in range(1000):
            tmp = uniform(a,b)
            r_l_n = fabs(f(tmp) - s(tmp))
            if (r_l_n > r): 
                r = r_l_n
                x_m = tmp
        print("Отклонение %.9f в точке %.6f"%(r,x_m))        
        
        p3 = plot(s.as_expr(), xlim = (-5,5), ylim = (-17,14), show = False, line_color = "RED", title = "Nopt%d"%n)
        p4 = plot(3*x - cos(x) - 1, xlim = (-5,5), ylim = (-17,14), show = False)
        p5 = plot((x-pi/2)*10**9, xlim = (-5,5), ylim = (-17,14), show = False, line_color = "GREEN")
        p6 = plot(x*10**9, xlim = (-5,5), ylim = (-17,14), show = False, line_color = "GREEN")
        p3.append(p4[0])
        p3.append(p5[0])
        p3.append(p6[0])
        p3.show()        
    #p4.show()  
    error = Abs(3*x - cos(x) - 1 - s.as_expr())
    p3 = plot(error, xlim = (0,pi/2), ylim = (0,1e-10), show = True, line_color = "RED", title = "Error with %d Opt points"%n)    
    return 0;

if (__name__ == "__main__"):
    #pass
    main()