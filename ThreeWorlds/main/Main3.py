'''
Created on Jul 18, 2017

@author: Ranaar Araajakata
'''

import matplotlib.pyplot as plt

if __name__ == '__main__':
#     plt.subplot(211)
    plt.plot([1,2,3], label="test1")
    plt.plot([3,2,1], label="test2")
    # Place a legend above this subplot, expanding itself to
    # fully use the given bounding box.
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)

    plt.show()