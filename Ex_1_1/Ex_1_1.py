import numpy as np
import matplotlib . pyplot as plt



def force(m, g):
    return np.array([0, -m*g])
def one_step_euler(x,v,f,dt):
    #x=x+v*dt
    x+=v*dt
    v+=f*dt/m
    return x,v

x=np.array([0.0,0.0])## 1d array with two zero Values [0,0]
v=np.array([60.0,60.0])## m/sec
trajectory=[] ## A python list
g=9.81 # m/sec^2
m=2 # kg
dt=0.1# sec
while x[1]>=0:
    x,v=one_step_euler(x,v,force(m,g),dt)
    trajectory.append(x.copy())
    ##end of the loop
trajectory=np.array(trajectory)
fig=plt.figure(figsize=(6,4))## inches
plt.plot(trajectory[:,0], trajectory[:,1], 'ro',label='trajectory')
plt.legend(loc='best')
plt.grid()
plt.show()