import matplotlib.pyplot as plt
x=["c", "c++","python", "java"]
y=[85,70,60,82]
plt.bar(x,y)
plt.show()

import matplotlib.pyplot as plt
x=["c", "c++","python", "java"]
y=[85,70,60,82]
plt.xlabel("language")
plt.ylabel("No", fontsize = 15)
plt.title("bhave", fontsize= 15)
c=["y", "b", "m", "g"]
plt.bar(x,y, width = 0.4, color = c)
plt.show()


import matplotlib.pyplot as plt
x=["c", "c++","python", "java"]
y=[85,70,60,82]
plt.xlabel("language")
plt.ylabel("No", fontsize = 15)
plt.title("wscube", fontsize= 15)
c=["y", "b", "m", "g"]
plt.bar(x,y, width = 0.4, color = c, align = "edge")
plt.show()


import matplotlib.pyplot as plt
x=["c", "c++","python", "java"]
y=[85,70,60,82]
plt.xlabel("language")
plt.ylabel("No", fontsize = 15)
plt.title("wscube", fontsize= 15)
c=["y", "b", "m", "g"]
plt.bar(x,y, width = 0.4, color = c, align = "center")
plt.show()


import matplotlib.pyplot as plt
x=["c", "c++","python", "java"]
y=[85,70,60,82]
plt.xlabel("language")
plt.ylabel("No", fontsize = 15)
plt.title("wscube", fontsize= 15)
c=["y", "b", "m", "g"]
plt.bar(x,y,width=0.4, color=c, edgecolor = "r",  linewidth = 10)
plt.show()


import matplotlib.pyplot as plt
x=["c", "c++","python", "java"]
y=[85,70,60,82]
plt.xlabel("language")
plt.ylabel("No", fontsize = 15)
plt.title("wscube", fontsize= 15)
c=["y", "b", "m", "g"]
plt.bar(x,y,width=0.4,color=c, edgecolor="r",  linewidth=5, linestyle=":")
plt.show()


import matplotlib.pyplot as plt
x=["c", "c++","python", "java"]
y=[85,70,60,82]
plt.xlabel("language")
plt.ylabel("No", fontsize = 15)
plt.title("wscube", fontsize= 15)
c=["y", "b", "m", "g"]
plt.bar(x,y,width=0.4,color=c, edgecolor="r",  linewidth=5, linestyle=":", alpha=0.5)
plt.show()


import matplotlib.pyplot as plt
x=["c", "c++","python", "java"]
y=[85,70,60,82]
plt.xlabel("language")
plt.ylabel("No", fontsize = 15)
plt.title("wscube", fontsize= 15)
c=["y", "b", "m", "g"]
plt.bar(x,y, width = 0.4, color = c, edgecolor = "r",  label = "wscube")
plt.legend()
plt.show()


import matplotlib.pyplot as plt
x=["c", "c++","python", "java"]
y=[85,70,60,82]
plt.xlabel("language")
plt.ylabel("No", fontsize = 15)
plt.title("wscube", fontsize= 15)
c=["y", "b", "m", "g"]
plt.bar(x,y, width = 0.4, color = "r",  label = "wscube")
plt.legend()
plt.show()