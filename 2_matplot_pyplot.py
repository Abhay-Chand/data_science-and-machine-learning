''' import matplotlib.pyplot as plt #now the pyplot package can be refer as plt
import numpy as np

# plotting x and y.
# plot() function is used to draw  points or markers in a diagram
# there are 2 parameter to specifying points in diagram i.e. 1. x-axis and y-axis   
xpoint = np.array([1,12])
ypoint = np.array([4,15])
plt.plot(xpoint,ypoint)
plt.show() '''

# the x-axies in horizontal and y-axis is vertical

# Plotting without line 
'''
import matplotlib.pyplot as plt
import numpy as np
 
xpoint = np.array([1,2,15,10,25])
ypoint = np.array([1,3,10,15,30])
plt.plot(xpoint,ypoint,'o')
plt.show()'''


 #default x -points
# if we don't specify the point in x - axis then the default values i.e 1,2,3,4.... value will apply
import matplotlib.pyplot as plt
import numpy as np
ypoint = np.array([2,5,9,7,10,12,4])
plt.plot(ypoint,'p')
plt.show()