import numpy as np

#Links do robô:
l1 = 150
l2 = 450
l3 = 590
l4 = 130
l5 = 647.07
l6 = 95

def getAngles(pose):

    #Simplificação:
    gamma = np.arctan2(l5, l4)
    H = np.sqrt((l4**2)+(l5**2))

    # Desacoplamento cinemático:
    xc = (pose[0][3] - (l6*pose[0][2]))
    yc = (pose[1][3] - (l6*pose[1][2]))
    zc = (pose[2][3] - (l6*pose[2][2]))

    # Auxiliares:
    r = np.sqrt((xc**2) + (yc**2))
    T = (r-l1)
    U = (zc-l2)
    S = np.sqrt((T**2) + (U**2))
    alpha = np.arctan2(U, T)

    #vetor para armazenar a solução:
    thetas = (np.ones(6)*np.nan)

    # Theta 1:
    thetas[0] = -np.arctan2(yc, xc)

    # Theta 3:
    cb = (((S**2)+(l3**2)-(H**2))/(2*S*l3))
    beta = np.arctan2(np.sqrt(1-(cb**2)), cb)
    c3g = (((S**2)-(H**2)-(l3**2))/(2*H*l3))
    thetas[2] = (gamma - np.arctan2(np.sqrt(1-(c3g**2)), c3g) - (np.pi/2))

    # Theta 2:
    thetas[1] = ((np.pi/2) - beta - alpha)

    # Orientação:
    c5 = ((np.cos(thetas[0])*np.sin(thetas[1]-thetas[2])*pose[0][2]) - (np.sin(thetas[0])*np.sin(thetas[1]-thetas[2])*pose[1][2]) + (np.cos(thetas[1]-thetas[2])*pose[2][2]))
    #Caso geral:
    if (abs(abs(c5)-1) >= 1e-3):
        #Theta 4:
        sign = -1   #sinal de s5: arbitrado que theta5 será sempre negativo (ou nulo)
        dy = ((-np.cos(thetas[0])*pose[1][2]) - (np.sin(thetas[0])*pose[0][2]))
        dx = ((np.cos(thetas[0])*np.cos(thetas[1]-thetas[2])*pose[0][2]) - (np.cos(thetas[1]-thetas[2])*np.sin(thetas[0])*pose[1][2]) - (np.sin(thetas[1]-thetas[2])*pose[2][2]))
        thetas[3] = np.arctan2(sign*dy, sign*dx)
        #Theta 5:
        s4 = np.sin(thetas[3])
        c4 = np.cos(thetas[3])
        #Descontinuidade em 0:
        if (abs(s4) >= 1e-3):
            s5 = (((-np.cos(thetas[0])*pose[1][2]) - (np.sin(thetas[0])*pose[0][2]))/s4)
        else:
            s5 = (((np.cos(thetas[0])*np.cos(thetas[1]-thetas[2])*pose[0][2]) - (np.sin(thetas[0])*np.cos(thetas[1]-thetas[2])*pose[1][2]) - (np.sin(thetas[1]-thetas[2])*pose[2][2]))/c4)
        thetas[4] = np.arctan2(s5, c5)
        #Theta 6:
        s5_sign = round(s5/abs(s5+1e-12))
        dy = ((-np.cos(thetas[0])*np.sin(thetas[1]-thetas[2])*pose[0][1]) - (np.cos(thetas[1]-thetas[2])*pose[2][1]) + (np.sin(thetas[0])*np.sin(thetas[1]-thetas[2])*pose[1][1]))
        dx = ((-np.cos(thetas[0])*np.sin(thetas[1]-thetas[2])*pose[0][0]) - (np.cos(thetas[1]-thetas[2])*pose[2][0]) + (np.sin(thetas[0])*np.sin(thetas[1]-thetas[2])*pose[1][0]))
        thetas[5] = np.arctan2(s5_sign*dy, s5_sign*dx)
    #Singularidade do punho:
    else:
        #Theta 4:
        thetas[3] = 0
        #Theta 5:
        thetas[4] = 0
        #Theta 6:
        s6 = -((np.cos(thetas[0])*pose[1][0]) + (np.sin(thetas[0])*pose[0][0]))
        c6 = ((np.cos(thetas[0])*pose[1][1]) + (np.sin(thetas[0])*pose[0][1]))
        thetas[5] = np.arctan2(s6, c6)

    return thetas