# -*- coding: utf-8 -*-

import numpy as np

def pt_milieu(f,a,b,n):
    """Quadrature de \int_a^b f(x)dx par la méthode du point milieu sur
    [a,b] découpé en n sous-intervalles égaux.

    """
    h = (b-a)/n
    xm = a + (0.5+np.arange(n))*h
    Q = h*np.sum(f(xm))
    return Q

# Définir ci-dessous les autres méthodes de quadrature

Objet: fontions test

# -*- coding: utf-8 -*-

import numpy as np

def pt_milieu(f,a,b,n):
"""Quadrature de \int_a^b f(x)dx par la méthode du point milieu sur
[a,b] découpé en n sous-intervalles égaux.

"""
h = (b-a)/n
xm = a + (0.5+np.arange(n))*h
Q = h*np.sum(f(xm))
return Q

# Définir ci-dessous les autres méthodes de quadrature

def trapezes(f,a,b,n):
s=0
for i in range(0,n):
x_1 = a + (b-a)*i/float(n)
x_2 = a + (b-a)*(i+1)/float(n)
s +=(f(x_1) + f(x_2))/2.0*(x_1 - x_2)
return s

# Définir ci-dessous les autres méthode de simpson
def Simpson(f,a,b,n):
s=0
for i in range(0,n):
x_1 = a + (b-a)*i/float(n)
x_2 = a + (b-a)*(i+1)/float(n)
s +=(f(x_1) + 4*(f(x_1 + x_2)/2.0) + f(x_2)*(x_1 - x_2)/6.0
return s
#definir ci-dessous les methode de gauss-legendre
def gauss_legendre2(f,a,b,n):
h=(b-a)/flaot(n)
z=(f(a)-f(b))
for i in range(1,n)
z=z+f(a+i*h*(-sqrt(3)+3/6)
return h*z
print(gauss_legendre2(f,0,1,10)

