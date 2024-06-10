import numpy as np
import matplotlib.pyplot as plt
#-----------------SKRIV DIN LØSNING HER--------------------------------------------------------------#
def init_v(N,v0):
    v=np.zeros((N,N))
    v[:, 0] = v0
    return v

iterations = 10000
N=100
v0=10
v=init_v(N,v0)

for i in range(iterations):
    v_l = v[:, i-1:i]
    v_r = v[:, i:]
    v_u = np.roll(v,1,axis=0)[:, i:i+1]
    v_d = np.roll(v[:,i:i+1],-1,axis=0)
    
    v[:, 1:-1] = 1/4 * (v_l + v_r + v_u + v_d)

plt.imshow(v)
plt.colorbar()