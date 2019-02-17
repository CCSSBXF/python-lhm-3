import pygal
import matplotlib.pyplot as plt
from random import choice
from die import Die

x_value = [0]
y_value = [0]
D = Die()

#选择四个方向，前进1-6个值
for value in range(1,1001):
    c = choice([1,2,3,4,])
    d = D.roll()
    if c == 1:
        x_value.append(x_value[-1]+1*d)
        y_value.append(y_value[-1])
    elif c == 2:
        x_value.append(x_value[-1]+(-1)*d)
        y_value.append(y_value[-1])
    elif c == 3:
        x_value.append(x_value[-1])
        y_value.append(y_value[-1]+1*d)
    elif c == 4:
        x_value.append(x_value[-1])
        y_value.append(y_value[-1]+(-1)*d)

#算上初始的点一共有101个，所以range（1,1002）
plt.scatter(x_value,y_value,c=list(range(0,1001)),cmap=plt.cm.Blues,s=5)
plt.show()
q_1 = q_2 = q_3 = q_4 = 0
#点落在坐标轴四个区间的个数
for i in range(0,1001):
    if x_value[i] > 0 and y_value[i]>0:
        q_1 +=1
    elif x_value[i] < 0 and y_value[i] > 0:
        q_2 += 1
    elif x_value[i] < 0 and y_value[i] < 0:
        q_3 += 1
    elif x_value[i] > 0 and y_value[i] < 0:
        q_4 +=1

frequencies = [q_1,q_2,q_3,q_4]
print(frequencies)
hist = pygal.Bar()
hist.title = 'meiyou biaoti'
hist.x_labels = ['1','2','3','4']
hist.x_title = 'xiangxian'
hist.y_title = 'frequence'
hist.add('dot',frequencies)
hist.render_to_file('15-10.svg')











