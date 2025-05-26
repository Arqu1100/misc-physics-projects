from vpython import *

first_Sphere = sphere(radians = 0.1,pos=vec(-5,0,0), color=color.blue,velocity=vec(0,0,0))
second_Sphere = sphere(radians = 0.1,pos=vec(5,0,0), color = color.red,velocity=vec(-1,0,0))

dt = 0.1

mass_first = 5
mass_second = 10

def velocity_Update(object_velocity, accleration, direction):

    return object_velocity + accleration * dt * direction

def pos_Update(object):
    
    return object.pos + velocity_Update(object.velocity, 0, vec(0,0,0)) * dt

def direction(origin, object):

    return hat(object.pos - origin.pos)

def delta_postion(origin, object):
    return object.pos - origin.pos

def velocity_collision(object1, mass1, object2, mass2):

    velocity_object1_final = (mass1-mass2)/(mass1 + mass2) * object1.velocity + (2*mass2)/(mass1+mass2)*object2.velocity
    velocity_object2_final = (2*mass1)/(mass1 + mass2)*object1.velocity + (mass2 - mass1)/(mass1+mass2)*object2.velocity

    return velocity_object1_final, velocity_object2_final

while True:
    rate(60)

    

    if mag(delta_postion(first_Sphere, second_Sphere)) < 2*first_Sphere.radius:
        first_Sphere.velocity, second_Sphere.velocity = velocity_collision(first_Sphere, mass_first, second_Sphere, mass_second)

    first_Sphere.pos = pos_Update(first_Sphere, first_Sphere.velocity)
    second_Sphere.pos = pos_Update(second_Sphere, second_Sphere.velocity)
    
    print(first_Sphere.velocity, second_Sphere.velocity)
