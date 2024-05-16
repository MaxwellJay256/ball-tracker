# Ball Tracker

HITSZ 2024 金工实习 机器视觉基础实践选修模块

## Task | 任务

使用大疆 RoboMaster EP 机器人，实现对特定颜色小球的跟踪。编程基于 RM 的官方 SDK。

1. 将机器人获取的 BGR 图像转换为 HSV 图像并显示在窗口中。
2. 基于 HSV 颜色模型进行图像分割，获取目标颜色的 HSV 阈值。
3. 根据所得的目标颜色 HSV 阈值对视频流图像帧进行二值化。
4. 利用形态学处理方法对阈值分割后的图像进行腐蚀、膨胀、开运算、闭运算等操作，去除背景中的噪声，并填充目标物体区域内的空洞。
5. 在上一步的输出中进行轮廓查找，通过轮廓特征筛选（轮廓面积、轮廓周长、轮廓最小外包圆、拟合椭圆特征等），对目标小球位置进行定位，输出目标小球中心点位置信息。
6. 引入 PID 控制器，以目标小球位置为输入控制机器人底盘运动，实现对目标小球的跟踪。

## Files | 文件

- Example code:
  - [`get-image.py`](./references/get_image.py): Get and display images from the camera.
  - [`bgr-segmentation.py`](./references/bgr_segmentation.py): Segment the image from 3 channels.
  - [`chassis-speed.py`](./references/chassis_speed.py): Demo code for controlling the chassis.
  - [`gimbal-speed.py`](./references/gimbal_speed.py): Demo code for controlling the gimbal.
- Customized code:
  - `main.py`：Main function for the task.

## Environment | Python 运行环境

Python 3.8 with the packages below:
1. `robomaster`
2. `opencv-python`
3. `numpy`

```bash
pip install robomaster opencv-python numpy
```

## TODO | 未竟之事

- [ ] Encapsulate the colors to be recognized into a class.
- [ ] Encapsulate contours into a class.
- [ ] Encapsulate the PID controller into a class.