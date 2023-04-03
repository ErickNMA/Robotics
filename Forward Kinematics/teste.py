from FKM import *

"""threeR = Robot((
    [theta1, 0, l1, 0],
    [theta2, 0, l2, 0],
    [theta3, 0, l3, 0]
))"""

#threeR.showHTM(0, 3)

"""RP = Robot((
    [theta1+rad(90), 0, l2, rad(90)],
    [0, l1+l3+d2, 0, 0]
))"""

"""RP = Robot()

RP.addDHLine(theta1+rad(90), 0, l2, rad(90))
RP.addNonDHLine(0, 0, l1+l3+d2, 0, 0, 0)

RP.showHTM(0, 2)
RP.showPose([rad(0), 5])"""

valid = Robot([
    [theta1, 0, 0, rad(-90)],
    [theta2, 0, l2, 0],
    [theta3-rad(90), 0, 0, rad(-90)],
    [theta4+rad(90), l3, 0, rad(90)],
    [theta5, 0, 0, rad(-90)],
    [theta6, 0, 0, 0]
])

valid.showHTM(0, 3)