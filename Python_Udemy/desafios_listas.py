import matplotlib.pyplot as plt

x =[x for x in range(101)]
y = [y**2 for y in x]

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')

plt.show()



