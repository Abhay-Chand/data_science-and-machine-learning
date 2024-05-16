# line style  or ls - is use to change the style of the plotted line 
'''import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([23,3,33,3,32,21,1,13])
plt.plot(ypoint, ls = 'dashed')
plt.show()
'''
# line colour - c
'''import matplotlib.pyplot as plt
import numpy as np
ypoint = np.array([12,33,44,5,45,56])
plt.plot(ypoint,ls ='dotted', c= 'y')
plt.show()
'''
#line width - lw (width of a line )
'''import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([12,33,44,35,45,23])
plt.plot(ypoint,ls = 'dotted',lw = '5')
plt.show()
'''
#example for multi-line
'''import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([13,33,34,43,54,42])
ypoint =  np.array([10,25,23,55,35,45])

plt.plot(xpoint)
plt.plot(ypoint)
plt.show()'''
