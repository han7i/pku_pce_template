import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
plt.rcParams["font.family"]="sans-serif" # 设置matplotlib库字体族为非衬线字体
plt.rcParams["font.sans-serif"]=["SimHei"] # 设置matplotlib库字体的非衬线字体为黑体
plt.rcParams['axes.unicode_minus'] =False # 负号显示

filename = "MeOH.txt"
segments = 6 #循环次数

with open(filename, encoding='utf8') as f:
    lines = f.readlines()
    segs = []
    for i in range(segments):
        element = f"Segment {str(i+1)}:\n" # 数据起始词
        find_element = max(index for index, item in enumerate(lines) if item == element) # max+enumerate 查找最后出现位置
        segs.append([datalist.rstrip().split(', ') for datalist in lines[find_element+1:find_element+276]]) # 每个segment长度275
        for datalist in segs[i]:
            for data in datalist:
                datalist[datalist.index(data)] = float(data)
x = [segs[j][i][0] for j in range(segments) for i in range(len(segs[j]))]
y = [segs[j][i][1] for j in range(segments) for i in range(len(segs[j]))]
plt.plot(x, y, color='blue' ,linewidth=1.2) # 叠图时重复此段

# plt.legend([],loc=) # 叠图时添加标注
plt.ylim([4.0e-6, -4.5e-6])
plt.xlim([-0.35, 1.2])
plt.xlabel("E/V")
plt.ylabel("I/A")
plt.show()