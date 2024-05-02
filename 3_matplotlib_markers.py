# U can use argument 'marker' to emphasize each point with specified marker.
'''import matplotlib.pyplot as plt 
import numpy as np

#leaving x-axis as default value
ypoint = np.array([12,3,24,55,54,5,66,4])
plt.plot(ypoint,marker = '*')
plt.show() 
'''
#format strings "fmt" - marker |line |color

''' import matplotlib.pyplot as plt
import numpy as np
ypoint = np.array([2,3,33,43,43,43])
plt.plot(ypoint,'o:c')
plt.show()

# line  reference 
# -  solid line 
# :  dotted line 
# -- dashed line 
# -. dashed /dotted line 

#color reference 
# r  red
# g  green
# b  blue
# c  cyan
# m  mangenta
# y  yellow 
# k black
# w white
'''

# Marker size 
'''
import matplotlib.pyplot as plt
import numpy as np
ypoint = np.array([12,333,4,3,43,43 ])
plt.plot(ypoint,'p:y', ms = 20)  # ms is for setting marker size .
plt.show()
'''
#maker color - mac (marker edge  color)
'''import matplotlib.pyplot as plt
import numpy as np
ypoint = np.array([1,2,25,33,14,13,])
plt.plot(ypoint, 'p:b' , ms= 20, mec = 'r' ) 
plt.show()
'''
# maker face colour(mfc)
import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([21,32,34,36,38])
plt.plot(ypoint, 'p:c',ms = 22,mec ='r',mfc ='y')
plt.show()