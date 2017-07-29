'''
Created on Jul 17, 2017

@author: Ranaar Araajakata
'''

from energy.anma.AnmaEnergy import Anma
from energy.anma.AnmaEnergy import AnmaType

import matplotlib.pyplot as plot, matplotlib.patches as mpatches, numpy as np, random

if __name__ == '__main__':
    fit = [0.192826607199, 0.112339514216, 0.123393802131, 0.172374200162, 0.074922923998, 0.139403908333, 0.179702099504, 0.00503694445705]
    a = Anma(max_anma=5_000 , p0=1e-3 , p1=5, fit=fit, liquidity=1e-4)
    
    history = {}
    
    for i in AnmaType:
        history[i] = []
        a.addEnergy(2 * a.max_anma * random.random() , i)
    
    for i in a.getFit():
        print(i, end='\t')
    print('\n')
    
    parts = a.getEnergyParts()
    for e in parts:
        i = parts[e]
        history[e].append(i)
        print(i , end='\t')
    print(a.ele_val.sum())
    
    accuracy = 60
    dt = 1 / accuracy
    
    max_time = 5 * 3600
    
    for j in range(0, max_time):
        for i in range(0, accuracy):
            a.update(dt)
        
        parts = a.getEnergyParts()
        for e in parts:
            i = parts[e]
            history[e].append(i)
            print((i  if abs(i) > 1e-15 else 0), end='\t')
        print(a.ele_val.sum())
    
    print(a)
    
    parts = a.getEnergyParts()
    for i in parts:
        print(i, ':\t' , parts[i], sep='')
    
    x = np.linspace(0, max_time , max_time + 1)
    
    red_patch = mpatches.Patch(color='red', label='The red data')
    plot.legend(handles=[red_patch])
    
    for i in AnmaType:
        p = plot.plot(x , history[i] , label=i.name)
        
    plot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
            ncol=len(AnmaType), mode="expand", borderaxespad=0.)
        
    plot.xlabel('Time (Minutes)')
    plot.ylabel('Anma')
    
    figManager = plot.get_current_fig_manager()
    figManager.window.showMaximized()

    plot.show()
    
    pass
