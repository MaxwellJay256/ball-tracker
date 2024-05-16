# -*-coding:utf-8-*-


import cv2  									#引入第三方opencv模块
from robomaster import robot  				#从第三方robomaster模块中引入robot类


if __name__ == '__main__':						#python主函数入口
    ep_robot = robot.Robot()					#创建robot类的实例对象ep_robot
    ep_robot.initialize(conn_type="ap")			#初始化ep_robot机器人，conn_type指定机器人连接模式，ap表示wifi直连模式，sta表示wifi组网模式，rndis表示USB连接模式

    ep_camera = ep_robot.camera				#创建ep_camera对象

    ep_camera.start_video_stream(display=False, resolution='360p')	#调用camera对象的start_video_stream方法，开始获取视频流，display参数指定是否显示获取到的视频流，resolution参数指定视频的尺寸大小，支持360p，540p，720p
    for i in range(0, 200):							#循环读取200帧图像数据
        img = ep_camera.read_cv2_image()			#调用camera对象的read_cv_image方法，获取一帧图像
        cv2.imshow("Robot", img)					#调用cv2的imshow方法，将该帧图像显示在Robot窗口中
        cv2.waitKey(1)							#调用cv2的waitKey方法，刷新图像显示
    cv2.destroyAllWindows()						#程序结束前，销毁所有窗口
    ep_camera.stop_video_stream()				#停止获取视频流

    ep_robot.close()							#释放ep_robot对象相关资源
