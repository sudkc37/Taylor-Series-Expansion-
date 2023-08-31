# -*- coding: utf-8 -*-
""" Taylor_series.ipynb

Automatically generated by Collaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VaWRJzSUTk5yBf4SpacDlF6CrTpgSGV9

#Understanding the Dynamic of Taylor Series Expansion.
By definition:
f(x) = f(a) + f'(a)x + f''(a)(x^2/2!) + f'''(a)(x^3/3!) + f''''(a)(x^4/4!) + .......
where,
a = 0
"""

Approximating the Sin function using Taylor Series Expansion, we get,
f(x) = x - (x^3/3!) + (x^5/5!) - (x^7/7!) + ......

import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
x = np.linspace(-10, 10, 2000)
y = np.sin(x)
plt.plot(x, y, 'k', linewidth=2)

first = [1,0]
firts_order = np.polyval(first,x)
plt.plot(x, firts_order, 'b--', label='1st order')

third = x-(x**3)/np.math.factorial(3)
plt.plot(x, third, 'r--', label='3rd order')

fifth = x-(x**3)/np.math.factorial(3) + (x**5)/np.math.factorial(5)
plt.plot(x, fifth, 'g--', label='5th order')

seventh = x-(x**3)/np.math.factorial(3) + (x**5)/np.math.factorial(5) - (x**7)/np.math.factorial(7)
plt.plot(x, seventh, 'm--', label='7th order' )

nineth = x-(x**3)/np.math.factorial(3) + (x**5)/np.math.factorial(5) - (x**7)/np.math.factorial(7) + (x**9)/np.math.factorial(9)
plt.plot(x, nineth, 'c--', label='8th order')

eleventh = x-(x**3)/np.math.factorial(3) + (x**5)/np.math.factorial(5) - (x**7)/np.math.factorial(7) + (x**9)/np.math.factorial(9) - (x**11)/np.math.factorial(11)
plt.plot(x, eleventh, 'k--', label='11th order')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.ylim(-10,10)
plt.xlim(-10,10)
plt.legend()
plt.xlabel('x')
plt.ylabel('function values')
plt.title('Taylor Series Expansion of sin(x)')
plt.grid(False)
plt.show()


Approximating the Cosin function using Taylor Series Expansion, we get,
f(x) = 1 - (x^2/2!) + (x^4/4!) - (x^6/6!) + ...... 

plt.figure(figsize=(10,6))
x = np.linspace(-10,10, 2000)
y = np.cos(x)
plt.plot(x,y, 'k', label='cos')

second = 1-(x**2)/np.math.factorial(2)
plt.plot(x, second, 'b--', label='2nd order')

forth = 1-(x**2)/np.math.factorial(2) + (x**4)/np.math.factorial(4)
plt.plot(x, forth, 'c--', label='4th order')

sixth = 1-(x**2)/np.math.factorial(2) + (x**4)/np.math.factorial(4) - (x**6)/np.math.factorial(6)
plt.plot(x, sixth, 'm--', label='6th order')

eighth = 1-(x**2)/np.math.factorial(2) + (x**4)/np.math.factorial(4) - (x**6)/np.math.factorial(6) + (x**8)/np.math.factorial(8)
plt.plot(x, eighth, 'g--',label='8th order')

teenth = 1-(x**2)/np.math.factorial(2) + (x**4)/np.math.factorial(4) - (x**6)/np.math.factorial(6) + (x**8)/np.math.factorial(8) - (x**10)/np.math.factorial(10)
plt.plot(x, teenth, 'r--',label='10th order')

twelvth = 1-(x**2)/np.math.factorial(2) + (x**4)/np.math.factorial(4) - (x**6)/np.math.factorial(6) + (x**8)/np.math.factorial(8) - (x**10)/np.math.factorial(10) + (x**12)/np.math.factorial(12)
plt.plot(x, twelvth, 'y--',label='10th order')

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.legend()
plt.xlabel('x')
plt.ylabel('function values')
plt.title('Taylor Series Expansion of Cos(x)')
plt.grid(False)
plt.show()


# Approximating e^x function:
f(e^x) = 1 + x + (x^2/2!) + (x^3/3!) + (x^4/4!) + .......

x = np.linspace(-10, 10 ,2000)
y = np.exp(x)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.plot(x,y)

second = 1+ x + (x**2)/np.math.factorial(2)
plt.plot(x, second, 'b--', label='2nd order')

third = 1+ x + (x**2)/np.math.factorial(2) + (x**3)/np.math.factorial(3)
plt.plot(x, third, 'r--', label='2nd order')

forth = 1+ x + (x**2)/np.math.factorial(2) + (x**3)/np.math.factorial(3) + (x**4)/np.math.factorial(4)
plt.plot(x, forth, 'c--', label='2nd order')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.legend()
plt.xlabel('x')
plt.ylabel('function values')
plt.title('Taylor Series Expansion of e^x')
plt.grid(False)
plt.show()

# This can be achieved using a loop
# using loop

plt.figure(figsize=(10,6))
x= np.linspace(-10,10,1000)
exp = np.exp(x)
plt.plot(x, exp, 'k', linewidth=3, label='exp^x')

for i in range(1, 12):
  y = 1
  for j in range(1, i + 1):
      y += (x**j) / np.math.factorial(j)
  label = f'{i}nd order'
  plt.plot(x, y, linestyle='--', label = label)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlim(-10,10)
plt.ylim(-10, 10)
plt.legend()
plt.xlabel('x')
plt.ylabel('Function Value')
plt.title('Taylor Series Approximation of exp^x')
plt.show()

#Taylor series expansion is valid and holds for any delta x until it hits a point where the derivatives are discontinuous. 
