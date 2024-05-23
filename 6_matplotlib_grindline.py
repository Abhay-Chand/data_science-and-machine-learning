#adding the grind line to a plot via "grid()"
'''import matplotlib.pyplot as plt
import numpy as np

y = np.array([12,15,18,21,24,25])
x = np.array([11,13,16,19,22,26])

font1 ={'family':'serif','color':'green','size':'20'}
font2 ={'family':'arial','color':'blue','size':'15'}
plt.title('health monitor',fontdict=font1)
plt.xlabel("population",fontdict=font1)
plt.ylabel("what's up",fontdict=font2)
plt.plot(x,y) 
plt.show() 
'''
#now we will specify which grid line is to display via x axis or y axis(legal values are x nad y and both) nd default value is both

''' import matplotlib.pyplot as plt
import numpy as np
y = np.array([12,15,18,21,24,25])
x = np.array([11,13,16,19,22,26])
font1 = {'family':'arial','color':'darkred','size':'15'}
font2 = {'family':'serif','color':'grey','size':'17'}
plt.title("health monitor" , fontdict=font1)
plt.xlabel("POPULATION",fontdict=font1)
plt.ylabel("what's up buddy",fontdict=font2)
plt.plot(x,y)
plt.grid(axis='y')#here we can print grid line which we want to print it can be -x ,-y,both
plt.show()
'''
#setting up the line property for grid
import matplotlib.pyplot as plt
import numpy as np
y = np.array([12,15,18,21,24,25])
x = np.array([11,13,16,19,22,26])
font1 = {'family':'arial','color':'darkred','size':'15'}
font2 = {'family':'serif','color':'grey','size':'17'}
plt.title("health monitor" , fontdict=font1)
plt.xlabel("POPULATION",fontdict=font1)
plt.ylabel("what's up buddy",fontdict=font2)
plt.plot(x,y)
plt.grid(color = 'green',ls = "-.",lw = 0.5,axis='x')
plt.show()

