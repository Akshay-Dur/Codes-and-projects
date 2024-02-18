# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:47:16 2020

@author: Akshay
"""

'''Obtaining a random orthogonal matrix. A gaussian distribution is used to 
get real values for the matrix entries and the Gram-Schmidt process is used to
normalize the columns.'''
import numpy as np
import sympy as sp
dim=4 #Dimension of matrix
n=100 #Trials
k=100 #Successes
p=0.5 #Probability of success
sig=(n*p*(1-p))**0.5    #standard deviation (sigma)
mu=n*p                  #Mean 
mat=sp.Matrix([])

#Generating entries of a matrix which are drawn from a gaussian distribution
for clmn in range(0, dim):
    r=sp.Matrix([])
    for row in range(0, dim): 
        e=sp.Matrix([np.random.normal(mu, sig)]) #matrix element
        r=r.row_insert(row, e)
    mat=mat.col_insert(clmn, r)
print(mat)

#Normalising columns of matrix using Gram-Schmidt process

O=sp.Matrix([]) #I will fill this matrix with orthonormal vectors

for i in range(0, dim):
    outer_prod=sp.zeros(dim, dim)
    if i==0:
        vnorm=mat[0:dim, i]/((mat[0:dim, i].T)*(mat[0:dim, i]))**0.5 #Normalised vector
        O=O.col_insert(i, vnorm)
    else:
        for k in range(0, i):
            outer_prod+=O[0:dim, k]*O[0:dim, k].T #Normalised vectors (ket e) are columns of O
        v=mat[0:dim, i]-(outer_prod)*mat[0:dim, i]
        
        vnorm=v/((v.T)*v)**0.5
        
        O=O.col_insert(i, vnorm)
print(O)






