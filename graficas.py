import os
import numpy as np
import matplotlib.pyplot as plt


a = os.system("g++ ejercicio26.cpp")
a = os.system("./a.out")


plt.figure(figsize=(10,5))
euler = np.loadtxt("euler.dat")
#k4 = np.loadtxt("rk4.dat")
#eapfrog = np.loadtxt("leapfrog.dat")


plt.subplot(3,3,1)
plt.plot(euler[:,0],euler[:,1])
plt.title("Euler")


plt.subplot(3,3,4)
plt.plot(euler[:,0],euler[:,2])
plt.title("Euler")




plt.subplot(3,3,7)
plt.plot(euler[:,1],euler[:,2])
plt.title("Euler")



#x = np.linspace(data.min(), data.max(),100)
#y = np.exp(-0.5*x*x)/np.sqrt(2.0*np.pi)
#plt.plot(x,y, label='resultado esperado')
#plt.xlabel('X')
#plt.ylabel('Histograma')
#plt.legend()
#plt.savefig("mcmc.png")

plt.savefig("algo.png")