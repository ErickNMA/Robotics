from sympy import *

def arredNUM(matrix):
    for a in preorder_traversal(matrix):
        if isinstance(a, Float):
            matrix = matrix.subs(a, round(a, 3))
    return matrix

def A(tn, dn, an, aln):
    M = Matrix([
            [ cos(tn), -sin(tn)*round(cos(aln),3), sin(tn)*round(sin(aln),3), an*cos(tn) ], 
            [ sin(tn), cos(tn)*round(cos(aln),3), -cos(tn)*round(sin(aln),3), an*sin(tn) ],
            [ 0, round(sin(aln),3), round(cos(aln),3), dn ],
            [0, 0, 0, 1]
            ])
    
    M.simplify()
    M = trigsimp(M)
    M = arredNUM(M)
    return M

#Thetas do diagrama de arrames
theta1 = Symbol('θ₁')
theta2 = Symbol('θ₂')
theta3 = Symbol('θ₃')
theta4 = Symbol('θ₄')
theta5 = Symbol('θ₅')
theta6 = Symbol('θ₆')

thetas = [theta1, theta2, theta3, theta4, theta5, theta6]

#Deslocamentos
d1 = Symbol('d₁')
d2 = Symbol('d₂')
d3 = Symbol('d₃') 
d4 = Symbol('d₄')
d5 = Symbol('d₅')
d6 = Symbol('d₆')

ds = [d1, d2, d3, d4, d5, d6]

#Tamanho dos links do manipulador
l1 = Symbol('l₁')
l2 = Symbol('l₂')
l3 = Symbol('l₃') 
l4 = Symbol('l₄')
l5 = Symbol('l₅')
l6 = Symbol('l₆')

ls = [l1, l2, l3, l4, l5, l6]

def printMatrix(M):
    print('\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    print('\n\n\n')
    for i in range(4):
        for j in range(4):
            print(f'\t{str(M[i][j]):^30}', end='')
        print('\n\n\n')
    print('\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

class Robot():
    T = []
    rotational = []
    def __init__(self, DH=None):
        if(DH):
            for i in DH:
                self.T.append(A(i[0], i[1], i[2], i[3]))
                try:
                    Float(i[0])
                    self.rotational.append(False)
                except:
                    self.rotational.append(True)
    
    def addDHLine(self, ti, di, ai, ali):
        self.T.append(A(ti, di, ai, ali))
        try:
            Float(ti)
            self.rotational.append(False)
        except:
            self.rotational.append(True)

    def addNonDHLine(self, dx, dy, dz, Rx, Ry, Rz):
        O = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        O = O@Matrix([[1, 0, 0, 0], [0, cos(Rx), -sin(Rx), 0], [0, sin(Rx), cos(Rx), 0], [0, 0, 0, 1]]) #Rotação em X
        O = O@Matrix([[cos(Ry), 0, sin(Ry), 0], [0, 1, 0, 0], [-sin(Ry), 0, cos(Ry), 0], [0, 0, 0, 1]]) #Rotação em Y
        O = O@Matrix([[cos(Rz), -sin(Rz), 0, 0], [sin(Rz), cos(Rx), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) #Rotação em Z
        O = O@Matrix([[1, 0, 0, dx], [0, 1, 0, dy], [0, 0, 1, dz], [0, 0, 0, 1]]) #Translação
        O.simplify()
        self.T.append(O)
        try:
            Float(Rz)
            self.rotational.append(False)
        except:
            self.rotational.append(True)
    
    def getHTM(self, a, b):
        O = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        for i in range(b-a):
            O = simplify(O@self.T[a+i])

        return arredNUM(O).tolist()
    
    def showHTM(self, a, b):
        printMatrix(self.getHTM(a, b))
    
    def showHTMElements(self, a, b):
        O = self.getHTM(a, b)
        print('\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
        for j in range(4):
            for i in range(4):
                print('a'+str(i+1)+str(j+1)+'\t = \t'+str(O[i][j])+'\n')
            print('----------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    
    def getPose(self, joints, links=None):
        pose = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        for i in range(len(joints)):
            pose = simplify(pose@self.T[i])
        if(links):
            for i in range(len(links)):
                pose = pose.subs(ls[i], links[i])
        for i in range(len(joints)):
            if(self.rotational[i]):
                pose = pose.subs(thetas[i], joints[i])
            else:
                pose = pose.subs(ds[i], joints[i])

        pose.simplify()
        return arredNUM(pose).tolist()
    
    def showPose(self, joints, links=None):
        printMatrix(self.getPose(joints, links))