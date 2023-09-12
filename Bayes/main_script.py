import numpy as np
from Bayes_learning import Bayes_Learning
from Bayes_testing import Bayes_Testing

def main():
    testing = np.loadtxt("testing_data.txt")
    training = np.loadtxt("training_data.txt")
    validation = np.loadtxt("validation_data.txt")
    p1, p2, pc1, pc2 = Bayes_Learning(training, validation)
    Bayes_Testing(testing, p1, p2, pc1, pc2) 

main()

