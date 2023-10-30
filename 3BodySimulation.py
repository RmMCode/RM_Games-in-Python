import turtle
import math

def dist(x1,y1,x2,y2):
    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

def grav_mag(m1,x1,y1,m2,x2,y2):
    return m1*m2/dist(x1,y1,x2,y2)**2

screen = turtle.Screen()
screen.screensize(700,700) #the size of the screen in pixels
screen.setworldcoordinates(-5,-5,5,5) #sets bottom left and top right of screen coordinate system

r = 1

m1 = 1
m2 = 1
m3 = 1
 
vx3,vy3 = -0.93240737*r, -0.86473146*r
vx1,vy1 = -vx3/2,-vy3/2
vx2,vy2 = vx1,vy1

x1,y1 = 0.97000436*r, -0.24308753*r
x2,y2 = -x1,-y1
x3,y3 = 0, 0 

t_step = .001

pointer1 = turtle.Turtle()
pointer1.up()
pointer1.shape("circle")
pointer1.color("red")
pointer1.speed(0)
pointer1.goto(x1,y1)
pointer1.down()

pointer2 = turtle.Turtle()
pointer2.up()
pointer2.shape("circle")
pointer2.color("green")
pointer2.speed(0)
pointer2.goto(x2,y2)
pointer2.down()

pointer3 = turtle.Turtle()
pointer3.up()
pointer3.shape("circle")
pointer3.color("blue")
pointer3.speed(0)
pointer3.goto(x3,y3)
pointer3.down()

i = 0

while True:
    i += 1

    #Calculate gravity
    f12 = grav_mag(m1,x1,y1,m2,x2,y2)
    f12_theta = math.atan2(y2-y1,x2-x1)
    f13 = grav_mag(m1,x1,y1,m3,x3,y3)
    f13_theta = math.atan2(y3-y1,x3-x1)
    f23 = grav_mag(m2,x2,y2,m3,x3,y3)
    f23_theta = math.atan2(y3-y2, x3-x2)

    #update positions
    x1,y1 = vx1*t_step+x1, vy1*t_step+y1
    x2,y2 = vx2*t_step+x2, vy2*t_step+y2
    x3,y3 = vx3*t_step+x3, vy3*t_step+y3
    
    #update velocities
    vx1 += f12*math.cos(f12_theta)/m1*t_step + f13*math.cos(f13_theta)/m1*t_step
    vy1 += f12*math.sin(f12_theta)/m1*t_step + f13*math.sin(f13_theta)/m1*t_step
 
    vx2 += f12*math.cos(f12_theta+math.pi)/m2*t_step + f23*math.cos(f23_theta)/m2*t_step 
    vy2 += f12*math.sin(f12_theta+math.pi)/m2*t_step + f23*math.sin(f23_theta)/m2*t_step 

    vx3 += f13*math.cos(f13_theta+math.pi)/m3*t_step + f23*math.cos(f23_theta+math.pi)/m3*t_step
    vy3 += f13*math.sin(f13_theta+math.pi)/m3*t_step + f23*math.sin(f23_theta+math.pi)/m3*t_step

    if i%200 == 0:
        pointer1.goto(x1,y1)
        pointer2.goto(x2,y2)
        pointer3.goto(x3,y3)