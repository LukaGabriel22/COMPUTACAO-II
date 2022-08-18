
# QUESTÃO 1

import matplotlib.pyplot as plt
x_axis = [1.0, 2.0,3.0]
y_axis = [2.0,4.0,1.0]
plt.axis([1.0, 3.0, 1.0, 4.0])
plt.plot(x_axis, y_axis, 'b-o')
plt.ylabel('y_axis')
plt.xlabel('x_axis')
plt.title('Sample Graph!')
plt.show()

# QUESTÃO 2

from matplotlib import pyplot as plt
date_x = [3,4,5,6,7]
open_y = [774.25,776.030029,779.309998,779,779.659973]
plt.plot(date_x,open_y,label='open')
high_y = [776.065002,778.710022,782.070007,780.47998,779.659973]
plt.plot(date_x,high_y,label='high')
low_y = [769.5,772.890015,775.650024,775.539978,770.75]
plt.plot(date_x,low_y,label='low')
close_y = [772.559998,776.429993,776.469971,776.859985,775.08001]
plt.plot(date_x,close_y,label='close')
plt.xlabel('Oct2016')
plt.legend()
plt.show()

# QUESTÃO 3

import matplotlib.pyplot as plt
x =[0, 50]
y =[0, 150]
plt.plot(x, y)
plt.axis([0, 100, 0, 200])
plt.ylabel('y_axis')
plt.xlabel('x_axis')
plt.title('Draw a line')
plt.show()

# QUESTÃO 4

import matplotlib.pyplot as plt
x_axis = [1,4,5,6,7]
y_axis = [2,6,3,6,3]
plt.axis([1, 8, 1, 8])
plt.plot(x_axis, y_axis, 'r-.o')
plt.plot(x_axis, y_axis, 'bo')
plt.ylabel('y_axis')
plt.xlabel('x_axis')
plt.title('Display marker')
plt.show()
