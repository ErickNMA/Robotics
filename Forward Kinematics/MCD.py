from FKM import *

# Tabela de Denavit Hartenberg do robô:
RRPRRRG = Robot((
    [theta1, 0, 0, rad(-90)],
    [theta2+rad(90), 0, 0, rad(90)],
    [0, d3+l2+l4, 0, 0],
    [theta4+rad(90), 0, 0, rad(-90)],
    [theta5, 0, 0, rad(90)],
    [theta6+rad(180), l5+l6, 0, 0]
))

# Configuração desejada para validação:
PEDIDA = [rad(90), 0, .45, rad(90), 0, rad(90)]
LINKS = [0, .164, 0, .05, .143, .12]

# Condição em HOME:
HOME = [0, 0, 0, 0, 0, 0]

#Obtenção da Matriz de Transformação Homogênea, do frame 6 em relação ao frame 0:
print("\n\n\nModelo Cinemático Direto:")
RRPRRRG.showHTMElements(0, 6)

# Pose final do robô em HOME:
print("\n\n\nValidação para HOME:")
RRPRRRG.showPose(HOME)

#Pose final do robô na configuração desejada de validação:
print("\n\n\nValidação para posição pedida e links informados:")
RRPRRRG.showPose(PEDIDA, LINKS)