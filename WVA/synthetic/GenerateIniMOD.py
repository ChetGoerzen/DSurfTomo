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
dep1 = np.array([0, 0.5, 1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0,
                 7.5, 8.0, 8.5, 9.0, 9.5])
#dep1=np.linspace(0, 10, nz)#np.array([0,0.2,0.4,0.6,0.8,1.1,1.4,1.8,2.5])
#dep1=np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.1,1.3,1.5,1.8,2.1,2.5])
#nz=len(dep1)
#end
vs1=np.zeros(nz)
mod=np.zeros((nz*ny,nx))
for k in range(nz):
  for j in range(ny):
    for i in range(nx):
      mod[k*ny+j,i]= minvel+dep1[k]*velgrad
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
