
import numpy as np;

#Dizi oluşturma
x = np.array([1,2,3,4,5])
print(type(x))
print("*"*50)

# sıfırlardan oluşan dizi oluşturma
y = np.zeros(10)
print(y)
print("*"*50)

# 2 boyutlu array oluşturma
a = np.zeros(((4,4)))
print(a)
print("*"*50)

# 1 lerden oluşan 2 boyutlu array oluşturma
b = np.ones(((2,4)))
print(b)
print("*"*50)

# 5 lerden oluşan 2 boyutlu array oluşturmaçarma ile elde edilebilir
c = np.ones(((3,4)))*5
print(c)
print("*"*50)

# arange metodu
print(np.arange(10,55,5))
print("*"*50)

# 0 dan 5 e kadar 0.3 artarak oluşturur
print(np.arange(0,5,0.3))
print("*"*50)

# 1 ile 5 arasını 50 eşilt parçaya böler
print(np.linspace(1,5,50))
print("*"*50)

#random matris oluşturur
print(np.random.rand(3,3))
print("*"*50)

#negatif sayılardan oluşan matris
print(np.random.randn(3,3))
print("*"*50)

#Birim matris
print(np.eye(5))
print("*"*50)

#1 den 50 ye kadar 15 tane rastgele sayı
print(np.random.randint(1,50,15))
print("*"*50)

#reshape ile farklı boyutlandırma
aa = np.arange(24)
print(aa)
print(aa.reshape(8,3))

print(aa.max())
print(aa.min())
print("*"*50)


