#!/usr/bin/env python
# how to run:
# ./GenerateIniMOD.py
# remember to move MOD to the directory where you want to run DSurfTomo
import numpy as np

#parameters need to be changed
#start
nx=60
ny=60
minvel=0.8
velgrad=0.15
nz = 20
#dep1=np.linspace(0, 9, nz)#np.array([0,0.2,0.4,0.6,0.8,1.1,1.4,1.8,2.5])
dep1 = np.array([0, 0.5, 1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0,
                 7.5, 8.0, 8.5, 9.0, 9.5])

vel1 = np.ones(nz) * 0.85
#vel1 = np.linspace(1.0, 2.1, len(dep1))
#vel1 = np.array([0.93882721, 0.94200928, 0.94519135, 0.9596064 , 0.97402145,
#                 0.97195738, 0.96989331, 0.97769207, 0.98549082, 1.01804579,
#                 1.05060077, 1.13208166, 1.21356256, 1.36531657, 1.51707058,
#                 1.68084972, 1.84462886, 1.99959501, 2.15456116, 2.28180107])

#dep1=np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.1,1.3,1.5,1.8,2.1,2.5])
#nz=len(dep1)
#end
vs1=np.zeros(nz)
mod=np.zeros((nz*ny,nx))
for k in range(nz):
  for j in range(ny):
    for i in range(nx):
      mod[k*ny+j,i]= vel1[k] #minvel+dep1[k]*velgrad
with open('MOD','w') as fp:
    for i in range(nz):
        fp.write('%5.1f' % dep1[i])
    fp.write('\n')
    for k in range(nz):
        for j in range(ny):
            for i in range(nx):
                fp.write('%7.3f' % mod[k*ny+j,i])
            fp.write('\n')
for i in range(nz):
  print (dep1[i]),
