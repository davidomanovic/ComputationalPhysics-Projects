# -*- coding: utf-8 -*-
#TFY4345 Classical Mechanics 2023
#Assignment 3
#Simple pendulum. Velocity Verlet algorithm.

import matplotlib.pyplot as plt
import numpy as np

#Constants
L = 1.00  #Length of rod (m)
m = 1.00  #Mass (kg)
g = 9.81  #Acceleration of gravity (m/s^2)
omega0 = np.sqrt(g/L) #Harmonic frequency (1/s)
T0 = 2*np.pi/omega0 #Oscillation period (s)
N = 500 #Number of timesteps
dt = (T0/N)*5  #Timestep (s)

#Initialize arrays
theta = np.zeros(N)
v = np.zeros(N)
F = np.zeros(N)
t = np.zeros(N)
kinetic = np.zeros(N)
potential = np.zeros(N)

#Initial conditions
theta[0] = 0.01 #Initial angle (rad)
v[0] = 0.0 #Initial angular velocity (rad/s)
t[0] = 0.0 #Initial time (s)
kinetic[0] = 0.5*m*(L*v[0])**2
potential[0] = m*g*L*(1-np.cos(theta[0]))

for i in range(0,N-1,1):
    F[i] = -omega0**2*np.sin(theta[i])
    v2 = v[i] + F[i]*dt/2
    theta[i+1] = theta[i] + v2*dt
    F[i+1] = -omega0**2*np.sin(theta[i+1])
    v[i+1] = v2 + F[i+1]*dt/2
    t[i+1] = t[i] + dt
    kinetic[i+1]=0.5*m*(L*v[i+1])**2
    potential[i+1]=-m*g*L*(1-np.cos(theta[i+1]))

#Plotting
plt.figure('Angle')
plt.plot(t,theta)
plt.title('Angle',fontsize=20)
plt.xlabel('Time (s)',fontsize=20)
plt.ylabel('Angle (rad)',fontsize=20)
plt.grid()
plt.show()

plt.figure('Angular velocity')
plt.plot(t,v)
plt.title('Angular velocity',fontsize=20)
plt.xlabel('Time (s)',fontsize=20)
plt.ylabel('Angular velocity (rad/s)',fontsize=20)
plt.grid()
plt.show()

plt.figure('Energy')
plt.plot(t,kinetic,t,potential,t,kinetic+potential)
plt.title('Energy',fontsize=20)
plt.xlabel('Time (s)',fontsize=20)
plt.ylabel('Energy (J)',fontsize=20)
plt.grid()
plt.show()