import matplotlib.pyplot as plt

from random_walk import RandWalk

#只要程序处于活动状态，就不断地模拟随机漫步
while True:
    #创建一个RandWalk实例，并将其包含的点都绘制出来
    rw = RandWalk(5000)
    rw.fill_walk()

    # #设置绘图窗口尺寸
    # plt.figure(dpi=128,figsize=(10,6))
    #
    # point_numbers = list(range(rw.num_points))
    #
    # plt.scatter(rw.x_value,rw.y_value,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    #
    # #突出起点和终点
    # plt.scatter(0,0,c='orange',edgecolors='none',s=100)
    # plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',edgecolors='none',s=100)

    #15-3 15-4略
    plt.plot(rw.x_value,rw.y_value,linewidth=1)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("make another walk?(y/n):")
    if keep_running =='n':
        break
