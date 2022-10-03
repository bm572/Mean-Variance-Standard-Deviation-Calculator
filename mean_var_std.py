import numpy as np

def calculate(input):
  if len(input) != 9:
    #If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: 
    raise ValueError('List must contain nine numbers.')
    #covert into a 3 x 3 numpy array
  a = np.array(input).reshape(3,3)
  cal = dict()
  cal['mean'] = [a.mean(0).tolist(), a.mean(1).tolist(), a.mean().tolist()]
  cal['variance'] = [a.var(0).tolist(), a.var(1).tolist(), a.var().tolist()]
  cal['standard deviation'] = [a.std(0).tolist(), a.std(1).tolist(), a.std().tolist()]
  cal['max'] = [a.max(0).tolist(), a.max(1).tolist(), a.max().tolist()]
  cal['min'] = [a.min(0).tolist(), a.min(1).tolist(), a.min().tolist()]
  cal['sum'] = [a.sum(0).tolist(), a.sum(1).tolist(), a.sum().tolist()] 
  return cal

print(calculate([0,1,2,3,4,5,6,7,8]))