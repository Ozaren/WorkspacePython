'''
Created on Jul 2, 2017

@author: Ranaar Araajakata
'''

import numpy as np

from neural_network import plotter

class NeuralNetwork(object):
    '''
    classdocs
    '''

    def __init__(self , layers , activationFunction):
        '''
        Constructor
        '''
        self.synapses = []
        self.actFunc = activationFunction
        self.size = layers
        
        for s in range(0, len(layers) - 1):
            self.synapses.append(np.random.random(layers[s:s + 2]) * 2 - 1)
        
        # end init
    
    def train(self , X , Y):
        layers = []
        
        layers.append(X)
        
        # Calculate each layer of network
        for i in range(1, len(self.synapses) + 1):
            l = self.actFunc(np.dot(layers[i - 1], self.synapses[i - 1]))
            layers.append(l)
        
        delta = []
        
        error = Y - layers[-1]
        d = error * self.actFunc(layers[-1] , deriv=True)
        delta.append(d)
        
        for i in range(1 , len(layers) - 1):
            error = d.dot(self.synapses[-i].T)
            d = error * self.actFunc(layers[-i - 1] , deriv=True)
            delta.append(d)
        
        for i in range(0 , len(self.synapses)):
            self.synapses[-1 - i] += 1 * layers[-2 - i].T.dot(delta[i])
        
        # end function train
    
    def run(self , X):
        output = X
        
        for syn in self.synapses:
            output = self.actFunc(np.dot(output, syn))
            
        return output
        # end function run
        
    def getCost(self , X , Y):
        return np.sum((Y - self.run(X)) ** 2) ** .5
def actFunc(x , deriv=False):
    if(deriv == True):
        return (x * (1 - x))
    
    return 1 / (1 + np.exp(-x))

if __name__ == "__main__":
    nn = NeuralNetwork((3, 2, 1) , actFunc)
    
    X = np.array([[0, 0 , 1],
                  [0, 1 , 1],
                  [1, 0 , 1],
                  [1, 1 , 1]])
    Y = np.array([[0],
                  [1],
                  [1],
                  [0]])
    
    print('Training:')
    for j in range(10000000):
        nn.train(X, Y)
        if j % 10000 == 0:
            cost = nn.getCost(X, Y) * 100
            print('cost = ' , cost , '%')
            
            if cost < 5:
                break
    
    print('Output')
    print(nn.run(X))
    
    networkModel = plotter.NeuralNetworkModel()
    
    l = len(nn.size)
    
    for i in range(l):
        if i == l - 1:
            networkModel.add_layer(nn.size[i])
        else:
            networkModel.add_layer(nn.size[i] , nn.synapses[i].T)
    
    networkModel.draw()


