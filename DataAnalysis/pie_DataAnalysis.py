import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 默认颜色
# plt.style.use('ggplot')
# 自定义颜色
colors = ['red','pink','magenta','purple','orange']

# 防止中文乱码
plt.rcParams['font.sans-serif']=['SimHei']

#用来正常显示负号  
plt.rcParams['axes.unicode_minus']=False

#字体管理器
import matplotlib.font_manager as fm
my_font = fm.FontProperties(fname="/usr/share/fonts/wqy-microhei/wqy-microhei.ttc")

#准备数据

data = [5,6,5,10,1]

#准备标签

labels = ["专业", "有趣","态度","很好","声音"]

#在饼图中突出某个标签

explode =[0,0.08,0,0,0]

#将横、纵坐标轴标准化处理,保证饼图是一个正圆,否则为椭圆

plt.axes(aspect='equal')

#控制X轴和Y轴的范围(用于控制饼图的圆心、半径)

plt.xlim(0,10)
plt.ylim(0,10)

#不显示边框

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['left'].set_color('none')
plt.gca().spines['bottom'].set_color('none')


# autopct='%.3f%%' 设置百分比的格式,保留3位小数
# pctdistance=0.8, #设置百分比标签和圆心的距离
# labeldistance=1.0,#设置标签和圆心的距离
# center=(4,4),#设置饼图的圆心(相当于X轴和Y轴的范围)
# radius=3.8,#设置饼图的半径(相当于X轴和Y轴的范围)

# 标题名
plt.title('学生反馈数据分析',pad=50,fontsize=20)

plt.pie(x=data,
        labels=labels,
        explode=explode,
        autopct='%.2f%%',
        labeldistance=0.6,
        pctdistance=1.2,
        radius=0.8,
        colors=colors)

# 第二个参数bbox_to_anchor被赋予的二元组中，num1用于控制legend的左右移动，值越大越向右边移动，num2用于控制legend的上下移动，值越大，越向上移动。用于微调图例的位置。
# https://blog.csdn.net/u010440456/article/details/90768681
plt.legend(loc=0,bbox_to_anchor=(1.5, 1),fontsize=15)
# 保存图片
plt.savefig('学生反馈数据分析.png')
# 显示图片
plt.show()