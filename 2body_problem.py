from vpython import *

first_Sphere = sphere(radians = 0.1,pos=vec(-10,0,0), color=color.blue)
second_Sphere = sphere(radians = 0.1,pos=vec(0,0,0), color = color.red)

pointVectorList = []
for i in range(40):
    pointVectorList.append(vec(-20 + i, 0, 0))
for i in range(40):
    pointVectorList.append(vec(0,-20+i,0))
grid = points(pos=pointVectorList, color=color.white,radius=1)

mass_first = 2*10**5
mass_second = 2*10**10

dt = 1

def gravityAcclMag(m1,  object1, object2):

    g = 6.67430 * 10**(-11)

    accl = m1 * g / (mag(object1.pos - object2.pos))**2

    return accl

def velocity_Update(object_velocity, accleration, direction):

    return object_velocity + accleration * dt * direction

def pos_Update(object, velocity):
    
    return object.pos + velocity * dt

def direction(origin, object):

    return hat(object.pos - origin.pos)

first_Velocity = vec(0,0.4,0)
second_Velocity = vec(0,0,0)

while True:
    rate(60)
    sphere2_to_sphere1 = direction(second_Sphere, first_Sphere)
    sphere1_to_sphere2 = direction(first_Sphere, second_Sphere)

    first_Velocity = velocity_Update(first_Velocity, gravityAcclMag(mass_second, first_Sphere, second_Sphere), sphere1_to_sphere2)
    second_Velocity = velocity_Update(second_Velocity, gravityAcclMag(mass_first, first_Sphere, second_Sphere), sphere2_to_sphere1)

    first_Sphere.pos = pos_Update(first_Sphere, first_Velocity)
    second_Sphere.pos = pos_Update(second_Sphere, second_Velocity)
