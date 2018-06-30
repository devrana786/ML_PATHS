import numpy as np
import math

class gradient_descent:
    def __init__(self,m,learning_rate,epochs):
        self.learning_rate = learning_rate
        self.m = m
        self.parameters_length = 2
        self.aux_array = np.random.uniform(0,20,self.m)
        self.x = np.array([[1,k] for k in self.aux_array])
        self.y = 10 * self.aux_array + 2
        self.parameters = np.array([[0,0]])
        self.epochs = epochs
    
    def get_hypothesis(self,index):
        return np.dot(self.parameters,self.x[index])
    
    def gradient_descent(self):
        self.temp_param = self.parameters
        for i in range(0,len(self.x)):
            self.temp_param = self.temp_param + (self.get_hypothesis(i)[0] - self.y[i]) * self.x[i]
        self.parameters = self.parameters - (self.learning_rate/self.m)*self.temp_param
    
    def run_epochs(self):
        for i in range(0,self.epochs):
            self.gradient_descent()
               
    def print_parameters(self):
        print("Parameters: ",self.parameters)


if __name__ == "__main__":
    g = gradient_descent(10,0.005,2000)
    g.run_epochs()
    g.print_parameters()

