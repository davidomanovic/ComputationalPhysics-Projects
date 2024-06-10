import matplotlib.pyplot as plt
import numpy as np
    
#Constants
L = 1.00  #Length of rod (m)
m = 1.00  #Mass (kg)
g = 9.81  #Acceleration of gravity (m/s^2)
w0 = np.sqrt(g/L) #Harmonic frequency (1/s)
T0 = 2*np.pi/w0 #Oscillation period (s)
N = 10000 #Number of timesteps
dt = (T0/N)*3  #Timestep (s)
A = 0.05*L # Amplitude

def solveODE(gamma, horizontal, theta0):
    #Initialize arrays
    theta = np.zeros(N)
    v = np.zeros(N)
    F = np.zeros(N)
    t = np.zeros(N)
    kinetic = np.zeros(N)
    potential = np.zeros(N)
    
    #Initial conditions
    theta[0] = theta0 #Initial angle (rad)
    v[0] = 0.0 #Initial angular velocity (rad/s)
    t[0] = 0.0 #Initial time (s)
    kinetic[0] = 0.5*m*(L*v[0])**2
    potential[0] = m*g*L*(1-np.cos(theta[0]))
    
    for i in range(0, N-1, 1):
        if horizontal == True:
            F[i] = - w0**2 * np.sin(theta[i]) + ((A*gamma**2/L) * np.cos(gamma*t[i]) * np.cos(theta[i]))
        else:
            F[i] = - w0**2*np.sin(theta[i]) + ((A*gamma**2/L) * np.cos(gamma*(t[i]+dt)) * np.sin(theta[i]))
        
        v2 = v[i] + F[i]*dt/2
        
        theta[i+1] = theta[i] + v2*dt
        
        if horizontal == True:
            F[i+1] = - w0**2*np.sin(theta[i+1]) + ((A*gamma**2/L) * np.cos(gamma*(t[i]+dt)) * np.cos(theta[i+1]))
        else:
            F[i+1] = - w0**2*np.sin(theta[i+1]) + ((A*gamma**2/L) * np.cos(gamma*(t[i]+dt)) * np.sin(theta[i+1]))

        
        v[i+1] = v2 + F[i+1]*dt/2
        
        t[i+1] = t[i] + dt
        
        kinetic[i+1]=0.5*m*(L*v[i+1])**2
        
        potential[i+1]=m*g*L*(1-np.cos(theta[i+1]))
        
    return theta, t, v, potential, kinetic

gamma = [0.2,10,20]


# horizontal kapitza
plt.figure('Horizontal Kapitza Angle',figsize=(10,6))
for i in gamma:
    theta, t, v, potential, kinetic = solveODE(i, True, 0.1)
    plt.plot(t, theta, label=rf"$\gamma = {i}$")
    plt.plot()

#Plotting
plt.title('Angle',fontsize=20)
plt.xlabel('Time (s)',fontsize=20)
plt.ylabel('Angle (rad)',fontsize=20)
plt.legend()
plt.grid()
plt.show()

# Create a figure and define the subplot grid
# The arguments to `plt.subplots` specify the number of rows and columns of subplots
# In this example, we have 1 row and 2 columns, so there will be 2 subplots side by side
fig, axes = plt.subplots(nrows=1, ncols=2)

for i in range(2):
    theta, t, v, potential, kinetic = solveODE(gamma[i], True, 0.1)
    axes[i].plot(t, kinetic, t, potential, t, kinetic+potential)
    axes[i].set_title(rf'E($\gamma$), $\gamma$ = {gamma[i]}')

# Adjust the spacing between subplots
plt.tight_layout()
plt.show()


plt.figure('Horizontal Kapitza Angle',figsize=(10,6))
for i in gamma:
    theta, t, v, potential, kinetic = solveODE(i, True, 0.001)
    plt.plot(t, theta, label=rf"$\gamma = {i}$")

#Plotting
plt.title('Horizontal Kapitza Angle',fontsize=20)
plt.xlabel('Time (s)',fontsize=20)
plt.ylabel('Angle (rad)',fontsize=20)
plt.legend()
plt.grid()
plt.show()

#frick off



