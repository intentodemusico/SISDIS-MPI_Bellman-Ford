# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:24:15 2020

@authors: Intentodemusico, oswalman
"""
#%%
from mpi4py import MPI

import numpy as np
nodos= 5
array = [[0,1,-1],
         [0,2,4],
         [1,2,3],
         [1,3,2],
         [1,4,2],
         [3,2,5],
         [3,1,1],
         [4,3,-3]]

#%%
def BellmanFord(src): 
  
        # Crear una lista de infinitos, para medir la distancia del nodo inicial
        # A los otros.
        
        distancias = [np.inf] * nodos
        distancias[src] = 0
        
        #  Buscar camino mas corto con cada nodo
        
        for i in range(nodos - 1): 

            for u, v, w in array:
                if distancias[u] != np.inf and distancias[u] + w < distancias[v]: 
                        distancias[v] = distancias[u] + w 
  
        # Revisa caminos negativos
  
        for u, v, w in array: 
                if distancias[u] != np.inf and distancias[u] + w < distancias[v]: 
                        print ("Grafo contiene peso negativo")
                        return
        return distancias
#%%
comm = MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()
#%%
def startStop(n):
    residuo=n%size
    start=int(n/comm.size*rank)
    stop=int(n/comm.size*(rank+1)) 
    d=[x for x in range(start,stop)]
    print("rank",rank,d)
    return d

#%%
if rank == 0:
    data = nodos

else:
    data = None
data = comm.bcast(data,root=0)
#print ('rank',rank,'has data: ', data)
result=""
for k in startStop(data):
    result+=str(BellmanFord(k))+str("\n")

data=result.strip()
new_data=comm.gather(data,root=0)
if rank==0:
    print("Master recogio: ", new_data)
