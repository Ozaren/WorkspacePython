'''
Created on Jul 16, 2017

@author: Ranaar Araajakata
'''

import numpy as np
from anma.AnmaEnergy import Anma

if __name__ == '__main__':
    max_trials = 1_000_000
    total = 0
    nums = [None] * max_trials
    counts_min = [x[:] for x in [[0] * 11] * 9]
    counts_max = [x[:] for x in [[0] * 11] * 9]
    
    def prnt(array):
        print(end='\t')
        for j in range(0, len(array[0])):
            print(j / 10 , end='\t')
        print()
        
        for i in range(0, len(array)):
            print(i, end='\t')
            for j in range(0, len(array[i])):
                print(array[i][j] , end='\t')
            print()
        print()
    
    for i in range(0, max_trials):
        if i % 1000 == 0:
            print(i / max_trials * 100 , "%" , end = '\r')
        a = Anma()
        for j in range(0, 11):
            length = np.where(a.fit <= j / 10)[0].__len__()
            counts_min[length][j] += 1
            length = np.where(a.fit > j / 10)[0].__len__()
            counts_max[length][j] += 1
#     
#     prnt(counts_min)
#     prnt(counts_max)
#      
#     for i in range(len(counts_min) - 2, -1, -1):
#         for j in range(0, len(counts_min[i])):
#             counts_min[i][j] += counts_min[i + 1][j]
#     
#     prnt()
#     
#     for i in range(0, len(counts_min)):
#         for j in range(len(counts_min[i]) - 1, 0, -1):
#             counts_min[i][j] -= counts_min[i][j - 1]
#     
    prnt(counts_min)
    prnt(counts_max)
     
    pass
