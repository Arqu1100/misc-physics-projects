from vpython import *
import numpy as np

first_Sphere = sphere(radians = 0.1,pos=vec(-5,0.25,0), color=color.blue,velocity=vec(1,0,0),mass=0)
second_Sphere = sphere(radians = 0.1,pos=vec(5,0,0), color = color.red,velocity=vec(-2,0,0),mass=0)

#pointVectorList = []
#for i in range(20):
#    pointVectorList.append(vec(-10 + i, 0, 0))
#grid = points(pos=pointVectorList, color=color.white)

leftBox = box(height=20, pos=vec(-10,0,0), color = color.green, isTop = False)
rightBox = box(height=20, pos=vec(10,0,0), color = color.green, isTop = False)
topBox = box(length = 20, pos=vec(0,10,0), color = color.green, isTop = True)
bottomBox = box(length = 20, pos=vec(0,-10,0), color = color.green, isTop = True)

dt = 0.1

first_Sphere.mass = 1
second_Sphere.mass = 2

def zero_accl():
    return vec(0,0,0)

def velocity_Update(object_velocity, acelFunc):

    return object_velocity + acelFunc * dt

def pos_Update(object1):
    
    return object1.pos + velocity_Update(object1.velocity, zero_accl()) * dt

def direction(origin, object):

    return hat(object.pos - origin.pos)

def delta_postion(origin, object):
    return object.pos - origin.pos

def velocity_return(object1, mass1, object2, mass2):

    velocity_object1 = object1.velocity - (2*mass2)/(mass1 + mass2) * (dot( (object1.velocity - object2.velocity), (object1.pos - object2.pos) )) / mag(object1.pos - object2.pos)**2 * (object1.pos - object2.pos)
    velocity_object2 = object2.velocity - (2*mass1)/(mass1 + mass2) * (dot( (object2.velocity - object1.velocity), (object2.pos-object1.pos))) / mag(object2.pos - object1.pos)**2 * (object2.pos - object1.pos)

    return velocity_object1, velocity_object2

def wall_collision(object):
    object.velocity.x = -1 * object.velocity.x

def ceiling_collision(object):
    object.velocity.y = -1 * object.velocity.y

def boundery(object):

    if abs(object.pos.x + object.radius) > 9:
        wall_collision(object)
    elif abs(object.pos.y + object.radius) > 9:
        ceiling_collision(object)

while True:
    rate(60)

    if mag(delta_postion(first_Sphere, second_Sphere)) < 2*first_Sphere.radius:

        first_Sphere.velocity, second_Sphere.velocity = velocity_return(first_Sphere, first_Sphere.mass, second_Sphere, second_Sphere.mass)

    print(delta_postion(first_Sphere,second_Sphere), delta_postion(second_Sphere, first_Sphere))

    boundery(first_Sphere)
    boundery(second_Sphere)

    first_Sphere.pos = pos_Update(first_Sphere)
    second_Sphere.pos = pos_Update(second_Sphere)
    