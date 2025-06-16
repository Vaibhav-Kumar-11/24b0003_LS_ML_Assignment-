import numpy as np

a=np.random.rand(20)*9 #scale up 
b=np.random.rand(20)
final = a + b
print(final) #Not rounded off

final_rounded_off = np.round(final,2) #built in function in numpy learnt through extra resources
print(final_rounded_off)

print(np.max(final))
print(np.min(final))
print(np.median(final))

for i in range(0,20):
    if(final[i]<5):
        final[i] *= final[i]
print(final) 

def numpy_alternate_sort(array):
    array.sort()
    list=[]
    i = 0
    j = len(array) - 1     # so that wo last pr aajaye "-1" is imp
    while i <= j:
        list.append(float(array[i]))    #float krna hota h remember for future use to wrna debugging krne mei hi boht time consuem hogya tha
        if i != j:
            list.append(float(array[j]))
        i += 1
        j -= 1
    print(list)
numpy_alternate_sort(final)
