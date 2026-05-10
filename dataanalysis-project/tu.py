import matplotlib.pyplot as plt

# 优化后的操场单圈轨迹数据（32个点，弯道密、直线疏）
trajectory = [
    {"longitude": 102.987430000000, "latitude": 29.981986000000},
    {"longitude": 102.987381700000, "latitude": 29.981685350000},
    {"longitude": 102.987312700000, "latitude": 29.981255850000},
    {"longitude": 102.987192938830, "latitude": 29.980986161427},
    {"longitude": 102.987036214532, "latitude": 29.980877042578},
    {"longitude": 102.986926839353, "latitude": 29.980854497334},
    {"longitude": 102.986768113278, "latitude": 29.980951167527},
    {"longitude": 102.986638747530, "latitude": 29.981105432653},
    {"longitude": 102.986554000000, "latitude": 29.981169000000},
    {"longitude": 102.986558500000, "latitude": 29.981367000000},
    {"longitude": 102.986563900000, "latitude": 29.981604600000},
    {"longitude": 102.986570200000, "latitude": 29.981881800000},
    {"longitude": 102.986616428345, "latitude": 29.982025356453},
    {"longitude": 102.986727221435, "latitude": 29.982138253135},
    {"longitude": 102.986862835154, "latitude": 29.982226851454},
    {"longitude": 102.987023000000, "latitude": 29.982271000000},
    {"longitude": 102.987165841454, "latitude": 29.982228351454},
    {"longitude": 102.987296541551, "latitude": 29.982136451551},
    {"longitude": 102.987398112154, "latitude": 29.982015513215},
    {"longitude": 102.987430000000, "latitude": 29.981986000000},
    {"longitude": 102.987374800000, "latitude": 29.981642400000},
    {"longitude": 102.987305800000, "latitude": 29.981212900000},
    {"longitude": 102.987143440078, "latitude": 29.980941865246},
    {"longitude": 102.986981000000, "latitude": 29.980830000000},
    {"longitude": 102.986819266158, "latitude": 29.980912192653},
    {"longitude": 102.986676724128, "latitude": 29.981048684693},
    {"longitude": 102.986562100000, "latitude": 29.981525400000},
    {"longitude": 102.986567500000, "latitude": 29.981763000000},
    {"longitude": 102.986668385215, "latitude": 29.982084621453},
    {"longitude": 102.986938221535, "latitude": 29.982255651421},
    {"longitude": 102.987233215632, "latitude": 29.982186841245},
    {"longitude": 102.987430000000, "latitude": 29.981986000000}
]

# 提取经度（x轴）、纬度（y轴）数据
lon = [point["longitude"] for point in trajectory]
lat = [point["latitude"] for point in trajectory]

# 设置绘图风格
plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False    # 支持负号
plt.figure(figsize=(8, 6), dpi=100)            # 画布大小+清晰度

# 绘制轨迹：蓝色平滑线 + 红色散点（标记点位）
plt.plot(lon, lat, color='#1f77b4', linewidth=2.5, label='跑步轨迹')
plt.scatter(lon, lat, color='#ff4b4b', s=30, zorder=5, label='定位点')

# 图表标注
plt.title('操场单圈轨迹可视化（32条数据 | 弯道密/直线疏）', fontsize=14, pad=20)
plt.xlabel('经度 (Longitude)', fontsize=12)
plt.ylabel('纬度 (Latitude)', fontsize=12)
plt.legend(loc='best')
plt.grid(True, alpha=0.3)  # 网格（半透明）
plt.tight_layout()         # 自适应布局

# 保存图片 + 显示图片
plt.savefig('playground_track.png', bbox_inches='tight')  # 保存到本地
plt.show()