import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,25,30]
plt.step(x,y, where ='post')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('stair plot example')
plt.show()
