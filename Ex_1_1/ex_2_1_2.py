#################################imports#############################################
import numpy as np
import matplotlib . pyplot as plt

#################################function############################################
def force(mass, gravity):
    '''Calculate the force according to the mass and g of earth'''
    f=np.array([0.0, -mass*gravity])
    return f

def step_euler(x,v,dt,mass,gravity,f):
    '''Calculate the position and the velocity according to Euler's scheme'''
    #x=x+v*dt
    x+=v*dt
    v+=f*dt/mass
    return x,v

##############################Main##################################################

#parameters
x=np.array([0.0,0.0])## 1d array with two zero Values [0,0]
v=np.array([60.0,60.0])## m/sec
trajectory=[] ## A python list
gravity=9.81 # m/sec^2
mass=2 # kg
dt=0.1# sec

#############################running simulation multiple times#################################
fig = plt.figure(figsize=(6, 4))  ## inches
for mass in [2,3,4,5,6]:
    #while loop that create the trajectory of the cannonball
    while x[1]>=0:
        x,v= step_euler(x, v, force(mass, gravity), dt)
        trajectory.append(x.copy())
    ##end of the loop
    trajectory=np.array(trajectory)

##creat the figure
    plt.plot(trajectory[:,0], trajectory[:,1],label='Mass of {:} kg'.format(mass))
plt.legend(loc='best')
plt.grid()
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.savefig('exercise_2_1_multiple_times.eps', format='eps')
plt.show()