from sympy import *
import numpy as np


def A (tn, dn, an, aln):
    
    M = Matrix([
            [ cos(tn), -sin(tn)*round(cos(aln),3), sin(tn)*round(sin(aln),3), an*cos(tn) ], 
            [ sin(tn), cos(tn)*round(cos(aln),3), -cos(tn)*round(sin(aln),3), an*sin(tn) ],
            [ 0, round(sin(aln),3), round(cos(aln),3), dn ],
            [0, 0, 0, 1]
            ])
    
    M.simplify()
    for a in preorder_traversal(M):
        if isinstance(a, Float):
            M = M.subs(a, round(a, 2))
    return M
    
    
#Thetas do diagrama de arrames
theta1 = Symbol('θ₁')
theta2 = Symbol('θ₂')
theta3 = Symbol('θ₃')
theta4 = Symbol('θ₄')
theta5 = Symbol('θ₅')
theta6 = Symbol('θ₆')

#Tamanho dos links do manipulador
link1 = Symbol('l₁')
link2 = Symbol('l₂')
link3 = Symbol('l₃') 
link4 = Symbol('l₄')
link5 = Symbol('l₅')
link6 = Symbol('l₆')
ds = Symbol('ds')
de = Symbol('de')

A1 = A(theta1, -830, 350, np.radians(90))

A2 = A(theta2-np.radians(90), 0, 750, np.radians(180))

A3 = A(theta3, 0, 250, np.radians(-90))

A4 = A(theta4, -1097, 0, np.radians(0))

T45 = Matrix([
    [0.5, 0, 0.866, 0],
    [0, -1, 0, 0],
    [0.866, 0, -0.5, 0],
    [0, 0, 0, 1]
])

A6 = A(theta5, 0, 0, 0)

T67 = Matrix([
    [0.5, 0, -0.866, 0],
    [0, -1, 0, 0],
    [-0.866, 0, -0.5, 0],
    [0, 0, 0, 1]
])

A8 = A(theta6, -273, 0, np.radians(0))

'''
Matriz de transformação T0_6
'''

T08 = A1@A2@A3@A4@T45@A6@T67@A8

print(T08)