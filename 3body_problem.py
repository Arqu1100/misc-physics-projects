from vpython import *

pointVectorList = []
for i in range(40):
    pointVectorList.append(vec(-20 + i, 0, 0))
for i in range(40):
    pointVectorList.append(vec(0,-20+i,0))
grid = points(pos=pointVectorList, color=color.white,radius=1)

num_object = 3

objectList = []

dt = 0.1

first_sphere = sphere(radians = 0.1,pos=vec(0,0,0), color = color.blue, acceleration=vec(0,0,0), velocity=vec(0,0,0), mass=2*10**12)
second_sphere = sphere(radians = 0.1,pos=vec(10,0,0), color = color.red, acceleration=vec(0,0,0), velocity=vec(-1,1,0), mass=2*10**10)
third_sphere = sphere(radians = 0.1,pos=vec(-10,0,0), color = color.yellow, acceleration=vec(0,0,0), velocity=vec(1,-1,0), mass=2*10**10)

def ini_vel(evt):
    if evt.id is "x":
        print(evt.object.velocity)
        evt.object.velocity = vec(0,evt.value,0)

def direction(origin, object):

    return hat(object.pos - origin.pos)

def gravityAcclMag(object1, object2):

    g = 6.67430 * 10**(-11)

    accl = object2.mass * g / (mag(object1.pos - object2.pos))**2 * direction(object1, object2)

    return accl

def sum_accel(object1, object2, object3):

    total_accel = gravityAcclMag(object1, object2) + gravityAcclMag(object1, object3)
    return total_accel

def velocity_Update(object, accleration):

    return object.velocity + accleration * dt

def pos_update(object, velocity):
    
    return object.pos + velocity * dt

#first_sphere_slider = slider(bind = ini_vel, max =1, min=-1, step=0.01, value=first_sphere.velocity.x, id ="x", object = first_sphere)
#second_sphere_slider = slider(bind= ini_vel, max=1,min=-1, step=0.01, value = second_sphere.velocity.y, id="x",  object = second_sphere)
#third_sphere_slider = slider(bind= ini_vel, max=1,min=-1, step=0.01, value = third_sphere.velocity.y, id="x",  object = third_sphere)


def animation():
    while True:
        rate(30)
        k = keysdown()

        first_sphere.pos = pos_update(first_sphere, velocity_Update(first_sphere, sum_accel(first_sphere, second_sphere, third_sphere)))
        second_sphere.pos = pos_update(second_sphere, velocity_Update(second_sphere, sum_accel(second_sphere, first_sphere, third_sphere)))
        third_sphere.pos = pos_update(third_sphere, velocity_Update(third_sphere, sum_accel(third_sphere, first_sphere, second_sphere)))

        if "p" in k:
            print("Pausing")
            break

while True:
    k = keysdown()
    if "y" in k:
        animation()
