#!/usr/bin/env python
# the checkerboard should use the initial model as background model, then add 
# some pertubations 
# remember to move MOD.true to the directory where you want to run DSurfTomo
import numpy as np
import matplotlib.pyplot as plt
#parameters you need to change
#start
nx=60
ny=60
nz=20
minvel=0.9
velgrad=0.2
dep1=np.array([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5])
anosize=0.5
amplitude=0.4
#end
nmax = np.max([nx,ny])
x=range(1,nmax+1)
y=range(1,nmax+1)
z=range(1,nz+1)
z=np.ones(nz)
bg=np.zeros((nz,nx,ny))
cross=np.zeros((nz,ny))
vs1=np.zeros(nz)
xy=np.kron(np.sin(anosize*np.array(y)),np.sin(anosize*np.array(x)))
xyz=np.kron(z,xy)
pxy=xyz.reshape(nz,nmax,nmax)
for k in range(nz):
    for j in range(ny):
        for i in range(nx):
            bg[k,i,j]= minvel+dep1[k]*velgrad
mod=np.zeros((nz*ny,nx))
for k in range(nz):
    for j in range(ny):
        for i in range(nx):
            mod[(k)*ny+j,i]=bg[k,i,j]+pxy[k,i,j]*amplitude
k=5
#plt.imshow(mod[k*ny:(k+1)*ny,:],cmap='jet_r')
np.savetxt('MOD.true',mod,fmt='%4.4f')
#plt.colorbar()
#plt.show()

