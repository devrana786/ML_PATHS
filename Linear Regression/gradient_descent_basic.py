import numpy as np
import math

class gradient_descent:
    def __init__(self,m,epochs):
        self.x = np.random.uniform(0,20,m)
        self.epochs = epochs
        self.learning_rate = 0.01
        self.theta0 = 0
        self.theta1 = 0
        self.y = self.x*10 + 2
        self.m = m
        self.previous_theta0 = 99
        self.previous_theta1 = 99
        print("X: ",self.x," Y: ",self.y)

    def get_hypothesis(self,index):
        return self.theta1 * self.x[index] + self.theta0

    def rate_of_change(self):
        return abs(self.theta0 - self.previous_theta0),abs(self.theta1-self.previous_theta1)

    def gradient_descent(self):
        temp_theta0 = 0
        temp_theta1 = 0
        for i in range(0,len(self.x)):
            temp_theta0 = temp_theta0 + self.get_hypothesis(i) - self.y[i]
            temp_theta1 = temp_theta0 + (self.get_hypothesis(i) - self.y[i])*self.x[i]
        self.theta0 = self.theta0 - (self.learning_rate/self.m)*temp_theta0
        self.theta1 = self.theta1 - (self.learning_rate/self.m)*temp_theta1

    def run_epochs(self):
        for i in range(0,self.epochs):
            a,b = self.rate_of_change()
            if a < 0.01 or b < 0.01:
                break
            self.gradient_descent()

    def print_parameters(self):
        print("Theta0: ",self.theta0," Theta1: ",self.theta1)

if __name__ == "__main__":
    g = gradient_descent(10,2000)
    g.print_parameters()
    g.run_epochs()
    g.print_parameters()
    