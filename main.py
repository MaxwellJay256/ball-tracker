import cv2
import numpy as np
from robomaster import robot

yellow_lower = np.array((24, 227, 80))
yellow_upper = np.array((37, 255, 255))

kernel = np.ones((3, 3), np.uint8)

y_tar = 0.6
x_tar = 0.5
dia_tar = 41.5

pid_y = [4, 0.9, 0]
pid_x = [120, 100, 1]
pid = [pid_x, pid_y]

error_p = [x_tar, y_tar]
error_pp = [0, 0]

u = [0, 0]
u_prev = [0, 0]

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_camera = ep_robot.camera
    ep_chassis = ep_robot.chassis

    ep_camera.start_video_stream(display=False, resolution='360p')
    while cv2.waitKey(1) != ord('q'):
        img = ep_camera.read_cv2_image()  # 获取一帧图像
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

        cv2.morphologyEx(yellow, op=cv2.MORPH_OPEN, kernel=kernel, iterations=5, dst=yellow)
        cv2.morphologyEx(yellow, op=cv2.MORPH_CLOSE, kernel=kernel, iterations=5, dst=yellow)

        contours, hierarchy = cv2.findContours(yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        diameter_max = 0
        contour_closest = []
        for idx, contour in enumerate(contours):
            area = cv2.contourArea(contours[idx])  # 计算每个轮廓的面积
            if len(contours[idx]) < 5:
                continue
            box = center_idx, size_idx, angle_idx = cv2.fitEllipse(contours[idx])  # 对每个轮廓进行椭圆拟合
            if max(size_idx[0], size_idx[1]) < min(size_idx[0], size_idx[1]) * 1.3:
                center_idx = np.uint16(center_idx)
                size_idx = np.uint16(size_idx)
                cv2.drawContours(img, contours, idx, (0, 0, 255), 3)  # 画出检测到的轮廓
                cv2.circle(img, center_idx, 1, (0, 0, 255), 3)  # 画出圆心
                cv2.putText(img, "(%d, %d)" % (center_idx[0], center_idx[1]), center_idx, cv2.FONT_HERSHEY_SIMPLEX,
                            0.9, (0, 0, 255), 1)
                diameter = np.mean(size_idx)  # 以椭圆的长轴和短轴的平均值作为球的直径
                if diameter > diameter_max:
                    contour_closest = contours[idx]
                    diameter_max = diameter

        pos = [0, 0]
        if len(contour_closest):
            box_closest = center, size, angle = cv2.fitEllipse(contour_closest)
            diameter = np.mean(size)
            pos[0], pos[1] = center
            cv2.ellipse(img, box_closest, (255, 255, 0), 2)  # 画出拟合的椭圆

        cv2.imshow("Robot", img)  # 调用 imshow 方法，将该帧图像显示在 Robot 窗口中

        img_height, img_width, img_depth = img.shape
        pos[0] /= img_width
        pos[1] /= img_height

        x_error = pos[0] - x_tar
        y_error = pos[1] - y_tar
        error = [x_error, y_error]

        for i in range(0, 2):
            u[i] = (u_prev[i]
                    + pid[i][0] * (error[i] - error_p[i])
                    + pid[i][1] * error[i]
                    + pid[i][2] * (error[i] - 2 * error_p[i] + error_pp[i]))
        error_pp = error_p
        error_p = error

        if len(contour_closest) == 0:
            u[0] = 0
            u[1] = 0
        if u[1] > 0.5:
            u[1] = 0.5
        if u[1] < -0.5:
            u[1] = -0.5
        if u[0] > 30:
            u[0] = 30
        if u[0] < -30:
            u[0] = -30

        print("x: ", u[1], "z: ", u[0])
        ep_chassis.drive_speed(x=-u[1], y=0, z=u[0], timeout=0.5)

    cv2.destroyAllWindows()  # 程序结束前，销毁所有窗口
    ep_camera.stop_video_stream()  # 停止获取视频流

    ep_robot.close()  # 释放 ep_robot 对象相关资源
