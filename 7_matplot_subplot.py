#display the multi plot- with subplot()
'''import matplotlib.pyplot as plt
import numpy as np 
#plot1
x = np.array([21,32,37,42,47,52,60])
y= np.array([10,20,30,40,50,60,70])
plt.subplot(1,2,1) # the figure has 1 row ,2 coloumn and this plot is the first plot
plt.plot(x,y)

#plot2
x = np.array([12,3,45,55,32,37])
y = np.array([10,20,30,40,50,60])
plt.subplot(1,2,2)
plt.plot(x,y)


plt.show()'''
'''import matplotlib.pyplot as plt
import numpy as np
# plot-1
x = np.array([20,30,40,50,60,70])
y = np.array([10,15,20,25,30,35])
plt.subplot(2,1,1)
plt.plot(x,y)

#plot 2
x = np.array([13,35,34,31,43,33,32])
y = np.array([21,34,24,26,27,40,36])
plt.subplot(2,1,2)
plt.plot(x,y)

plt.show() '''
#now we will draw challenge of 6 plot


""" import matplotlib.pyplot as plt
import numpy as np
#plot -01
x = np.array([13,35,34,31,43,33,32])
y = np.array([21,34,24,26,27,40,36])
plt.subplot(2,3,1)
plt.plot(x,y)
plt.title("sales")

#plot-02
x = np.array([20,30,40,50,60,70])
y = np.array([10,15,20,25,30,35])
plt.subplot(2,3,2)
plt.plot(x,y)
plt.title("profit")
#plot -03
x = np.array([20,30,35,50,60,70])
y = np.array([10,14,17,25,30,35])
plt.subplot(2,3,3)
plt.plot(x,y)
plt.title("loses")
#plot - 04
x = np.array([20,32,41,43,55,57])
y = np.array([10,15,20,27,32,38])
plt.subplot(2,3,4)
plt.plot(x,y)
plt.title("margin")

#plot -05
x = np.array([10,23,33,50,60,70])
y = np.array([15,17,20,25,30,35])
plt.subplot(2,3,5)
plt.plot(x,y)

#plot- 06
x = np.array([20,27,34,43,50,70])
y = np.array([12,14,16,19,21,25])
plt.subplot(2,3,6)
plt.plot(x,y)

plt.show()"""

#now we will give super title  suptitle()
#plot -01
import matplotlib.pyplot as plt
import numpy as np
x = np.array([13,35,34,31,43,33,32])
y = np.array([21,34,24,26,27,40,36])
plt.subplot(2,3,1)
plt.plot(x,y)
plt.title("sales")

#plot-02
x = np.array([20,30,40,50,60,70])
y = np.array([10,15,20,25,30,35])
plt.subplot(2,3,2)
plt.plot(x,y)
plt.title("profit")
#plot -03
x = np.array([20,30,35,50,60,70])
y = np.array([10,14,17,25,30,35])
plt.subplot(2,3,3)
plt.plot(x,y)
plt.title("loses")
#plot - 04
x = np.array([20,32,41,43,55,57])
y = np.array([10,15,20,27,32,38])
plt.subplot(2,3,4)
plt.plot(x,y)
plt.title("margin")

#plot -05
x = np.array([10,23,33,50,60,70])
y = np.array([15,17,20,25,30,35])
plt.subplot(2,3,5)
plt.plot(x,y)

#plot- 06
x = np.array([20,27,34,43,50,70])
y = np.array([12,14,16,19,21,25])
plt.subplot(2,3,6)
plt.plot(x,y)
plt.suptitle("MYSHOP")
plt.show()
