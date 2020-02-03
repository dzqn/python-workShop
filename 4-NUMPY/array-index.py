
import numpy as np

dizi = np.arange(10)**3

print(dizi)
print("*"*50)

print(dizi[2])
print("*"*50)

print(dizi[2:6])
print("*"*50)

print(dizi.reshape(5,2))
print("*"*50)

for item in dizi.reshape(5,2):
    print(item)    
print("*"*50)


for item in dizi.reshape(5,2).flat:
    print(item)    
print("*"*50)

a = np.array([1,2])
b = np.array([5,8])

print(np.hstack([a,b])) # tek boyutlu bir dizi olarak birleştirdi
print("*"*50)
print(np.vstack([a,b])) # sonucunda iki boyutlu bir dizi oluştu
print("*"*50)

