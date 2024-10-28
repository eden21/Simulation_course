#################################imports#############################################
import numpy as np
import matplotlib . pyplot as plt

#################################function############################################
def force(m, g):
    '''Calculate the force according to the mass and g of earth'''
    return np.array([0, -m*g])

def one_step_euler(x,v,f,dt):
    '''Calculate the position and the velocity according to Euler's schem'''
    #x=x+v*dt
    x+=v*dt
    v+=f*dt/m
    return x,v


##############################Main##################################################

#parameters
x=np.array([0.0,0.0])## 1d array with two zero Values [0,0]
v=np.array([60.0,60.0])## m/sec
trajectory=[] ## A python list
g=9.81 # m/sec^2
m=2 # kg
dt=0.1# sec

#############################running simulation once#################################
fig = plt.figure(figsize=(6, 4))  ## inches
while x[1]>=0:
    x,v=one_step_euler(x,v,force(m,g),dt)
    trajectory.append(x.copy())
##end of the loop
trajectory=np.array(trajectory)
##creat the figure
plt.plot(trajectory[:,0], trajectory[:,1],label='trajectory Mass {:} kg'.format(m))
plt.grid()
plt.legend(loc='best')

#############################running simulation multiple times#################################
fig = plt.figure(figsize=(6, 4))  ## inches
for mass in [2,3,4,5,6]:
    #while loop that create the trajectory of the cannonball
    while x[1]>=0:
        x,v=one_step_euler(x,v,force(mass,g),dt)
        trajectory.append(x.copy())
    ##end of the loop
    trajectory=np.array(trajectory)

##creat the figure
    plt.plot(trajectory[:,0], trajectory[:,1],label='trajectory Mass {:} kg'.format(mass))
plt.legend(loc='best')
plt.grid()
plt.show()

