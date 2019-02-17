import matplotlib.pyplot as plt

x_value = list(range(1,5000))
y_value = [x**3 for x in x_value]

# plt.scatter(x_value,y_value,c=x_value,cmap=plt.cm.Blues,edgecolors='none',s=10)
plt.plot(x_value,y_value,linewidth=1)

plt.title("lifang",fontsize=24)
plt.xlabel("x_zhou",fontsize=12)
plt.ylabel("y_zhou",fontsize=12)

plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()