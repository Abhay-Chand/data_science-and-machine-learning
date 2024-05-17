#Create labels for plot

'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([12,14,16,18,20,22,24,26])
y = np.array([25,50,75,100,125,150,175,200])
plt.plot(x,y, marker = '*')
plt.xlabel("population")
plt.ylabel("city number")
plt.show()
'''
#create a title for plot
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([12,14,16,18,20,22,24,26])
y = np.array([25,50,75,100,125,150,175,200])
plt.plot(x,y, marker = '*')
plt.title('Health Monitor')
plt.xlabel("population")
plt .ylabel("city number")
plt.show()
'''
# now we will set the font property for tittle and lables via "fontdict"
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([12,14,16,18,20,22,24,26])
y = np.array([25,50,75,100,125,150,175,200])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'arabic','color':'darkred','size':15}
plt.plot(x,y, marker = '*')
plt.title('Health Monitor',fontdict=font1)
plt.xlabel("population",fontdict=font2)
plt.ylabel("city number",fontdict=font2)
plt.show()
'''
#you can also chage the location of tittle via "loc"
import matplotlib.pyplot as plt
import numpy as np
x = np.array([12,14,16,18,20,22,24,26])
y = np.array([25,50,75,100,125,150,175,200])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'arabic','color':'darkred','size':15}
plt.plot(x,y, marker = '*')
plt.title('Health Monitor',fontdict=font1,loc='left')
plt.xlabel("population",fontdict=font2,loc = 'left')
plt.ylabel("city number",fontdict=font2,loc='center')
plt.show()