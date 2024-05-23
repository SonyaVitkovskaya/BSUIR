import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 16, 1)
y1=[1.0, 1.7777777777777777, 2.4, 2.909090909090909, 3.3333333333333335, 3.6923076923076925, 4.0, 4.266666666666667, 4.5, 4.705882352941177, 4.888888888888889, 5.052631578947368, 5.2, 5.333333333333333, 5.454545454545454]
labels= []
y2 = [1 for i in range(15)]
plt.figure(figsize=(10,5))
for i in range(15):
    labels.append(str(round(y1[i], 4) ))
for x_coord, y_coord, label in zip(x, y1, labels):
    plt.text(x_coord, y_coord, label)

plt.plot(x,y1,'Dk')
plt.plot(x,y2,'Dk')
plt.xlabel('r', fontsize=14)
plt.ylabel('Ку(r)', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.show()

x = np.arange(1, 201, 1)
y= []
y2 = [1 for i in range(200)]
for x_ in x:
    y.append((8*x_/(7+x_))/8) 
plt.figure(figsize=(30,5))
plt.plot(x,y,'Dk')
plt.plot(x,y2,'Dk')
plt.xlabel('r', fontsize=14)
plt.ylabel('е(r)', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.show()

x = np.arange(1, 201, 1)
y= []
y2 = [1 for i in range(200)]
for x_ in x:
    y.append((8*x_/(7+x_))) 
plt.figure(figsize=(30,5))
plt.plot(x,y,'Dk')
plt.plot(x,y2,'Dk')
plt.xlabel('r', fontsize=14)
plt.ylabel('Ky(r)', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.show()


x = [8 for i in range(15)]
y=[1.0, 1.7777777777777777, 2.4, 2.909090909090909, 3.3333333333333335, 3.6923076923076925, 4.0, 4.266666666666667, 4.5, 4.705882352941177, 4.888888888888889, 5.052631578947368, 5.2, 5.333333333333333, 5.454545454545454]
x2 = [1]
y2 = [1]
plt.figure(figsize=(30,5))

plt.plot(x2,y2,'Dk')
plt.plot(x,y,'Dk')
plt.ylabel('Ку(n)', fontsize=14)
plt.grid(True)
plt.show()


x = np.arange(1, 16, 1)
ky =[1.0, 1.7777777777777777, 2.4, 2.909090909090909, 3.3333333333333335, 3.6923076923076925, 4.0, 4.266666666666667, 4.5, 4.705882352941177, 4.888888888888889, 5.052631578947368, 5.2, 5.333333333333333, 5.454545454545454]
labels= []
y = []
y2 = [1 for i in range(15)]
plt.figure(figsize=(10,5))
for i in range(15):
    y.append(ky[i]/8)
    labels.append(str(round(y[i], 4)))
for x_coord, y_coord, label in zip(x, y, labels):
    plt.text(x_coord, y_coord, label)

plt.plot(x,y,'Dk')
plt.plot(x,y2,'Dk')
plt.xlabel('r', fontsize=14)
plt.ylabel('е(r)', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('graphics_e.png')
plt.show()

x = [8,8,8,8,8,8,8,8,8,8]
ky = [1.0, 1.7777777777777777, 2.4, 2.909090909090909, 3.3333333333333335, 3.6923076923076925, 4.0, 4.266666666666667, 4.5, 4.705882352941177]
y = []
plt.figure(figsize=(10,5))
for i in range(10):
    y.append(ky[i]/8)
plt.plot(x,y,'Dk')
plt.plot([1],[1],'Dk')
plt.ylabel('е(n)', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('graphics_e.png')
plt.show()
