from vpython import *

first_Sphere = sphere(radians = 0.1,pos=vec(-5,-5,0), color=color.blue,)
second_Sphere = sphere(radians = 0.1,pos=vec(5,5,0), color = color.red)

mass_first = 2*10**10
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

first_Velocity = vec(0,0.2,0)
second_Velocity = vec(0,-0.2,0)

print(gravityAcclMag(mass_first, first_Sphere, second_Sphere))

while True:
    rate(60)
    sphere2_to_sphere1 = hat(first_Sphere.pos - second_Sphere.pos)
    sphere1_to_sphere2 = hat(second_Sphere.pos - first_Sphere.pos)

    first_Velocity = first_Velocity + gravityAcclMag(mass_second, first_Sphere, second_Sphere) * dt * sphere1_to_sphere2
    second_Velocity = second_Velocity + gravityAcclMag(mass_first, first_Sphere, second_Sphere) * dt * sphere2_to_sphere1

    print(first_Velocity, second_Velocity)

    first_Sphere.pos = pos_Update(first_Sphere, first_Velocity)
    second_Sphere.pos = pos_Update(second_Sphere, second_Velocity)

    """
    first_Sphere.pos = first_Sphere.pos + 1/2* (gravityAcclMag(mass_second, first_Sphere, second_Sphere)) * dt**2 * sphere1_tosphere2
    second_Sphere.pos = second_Sphere.pos + 1/2 * (gravityAcclMag(mass_first, first_Sphere, second_Sphere)) * dt**2 * sphere2_to_sphere1
    """