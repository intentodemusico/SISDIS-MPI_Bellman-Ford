##from mpi4py import MPI
##import numpy as np
##nodes=7
##comm = MPI.COMM_WORLD
##size=comm.Get_size()
##rank=comm.Get_rank()
##if rank == 0:
##    
##    data = nodes
##    print ('scattering data',data)
##else:
##    data = None
##data = comm.bcast(data,root=0)
##n=data
###print ('rank',rank,'has data: ', data)
##
##start=int(n/comm.size*rank)
##stop=int(n/comm.size*(rank+1)) 
##d=[x for x in range(start,stop)]
##print("rank",rank,d)


#new_data=comm.gather(data,root=0)
#if rank==0:
   # print("Master recogio: ", new_data)
x="holi"
for i in range(2):
    x+="sano"*i+str("\n")

print(x.strip())
