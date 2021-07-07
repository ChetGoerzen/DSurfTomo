import numpy as np

maxPer = 12.3

nx = 60
ny = 60
nz = 20
goxd = -38.4
gozd = 177.945
dvxd = 0.0036
dvzd = 0.0054
nsrc = 1526
weight = 3.0
damp = 0.01
sablayers = 3
minvel = 0.1
maxvel = 3.0
niter = 2
synthetic = 0


with open("DSurfTomo.in", "w") as nFile:
    nFile.write("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc\n")
    nFile.write("c INPUT PARAMETERS\n")
    nFile.write("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc\n")
    nFile.write(f"DSurfTomoJoint.dat                    c: data file\n")
    nFile.write(f"{nx} {ny} {nz}                   c: nx ny nz (grid number in lat lon depth direction)\n")
    nFile.write(f"{goxd}  {gozd}                   c: goxd gozd (upper left point,[lat,lon])\n")
    nFile.write(f"{dvxd} {dvzd}                    c: dvxd dvzd\n")
    nFile.write(f"{nsrc}                           c: max(sources, receivers)\n")
    nFile.write(f"{weight} {damp}                  c: weight damp\n")
    nFile.write(f"{sablayers}                      c: sablayers\n")
    nFile.write(f"{minvel} {maxvel}                c: min, max velocity\n")
    nFile.write(f"{niter}                          c: number of iterations\n")
    nFile.write(f"0.2                              c: sparsity fraction\n")
    nFile.write(f"{len(np.arange(1.0, 13.0, 1.0))}                               c: kmaxRc (followed by periods)\n")
    for period in np.arange(1.0, 13.0, 1.0):
        nFile.write(f"{period:1.1f} ")
    nFile.write("c: periods\n")
    nFile.write(f"{len(np.arange(1.0, 16.0, 1.0))}                                c: kmaxRg\n")
    for period in np.arange(1.0, 16.0, 1.0):
        nFile.write(f"{period:1.1f} ")
    nFile.write("c: periods\n")
    nFile.write(f"0                                c: kmaxLc\n")
    nFile.write(f"0                                c: kmaxLg\n")
    nFile.write(f"{synthetic}                                c: synthetic flag(0:real data,1:synthetic)\n")
    nFile.write(f"0.02                             c: noise level\n")
    nFile.write(f"3.0                              c: threshold\n")
    nFile.write(f"1 100 200 c: vorotomo,ncells,nrelizations")
    nFile.close()

