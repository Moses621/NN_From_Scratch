#Code for part 1: Intro and Neuron Code https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=1

#Made up unique inputs
inputs = [1.2, 5.1, 2.1]

#Made up weights for a neuron
weights = [3.1, 2.1, 8.7]

#Made up bias for a neuron
bias = 3

#Summation of inputs * weights + bias
output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
print(output)
