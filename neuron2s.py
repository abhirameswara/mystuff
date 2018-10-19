import numpy as np

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

X = np.array([[1,1,0],
              [0,0,0],
              [1,1,1],
              [0,0,1]])

y = np.array([[1],
              [0],
              [1],
              [0]])

np.random.seed(1)

syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,4)) - 1
syn2 = 2*np.random.random((4,1)) - 1

for j in range(60000):

    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))
    l3 = nonlin(np.dot(l2,syn2))

    l3_error = y - l3

    if (j% 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l3_error))))

    l3_delta = l3_error*nonlin(l3,deriv=True)

    l2_error = l3_delta.dot(syn2.T)
    l2_delta = l2_error*nonlin(l2,deriv=True)

    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error*nonlin(l1,deriv=True)


    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

usin = nonlin(np.dot(np.array([0, 1, 0]), syn0))
usin2 = nonlin(np.dot(usin , syn1))
usin3 = nonlin(np.dot(usin2 , syn2))
print(usin3)
print(l3)