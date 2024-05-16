# -*-coding:utf-8-*-

import time
import robomaster
from robomaster import robot


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    #定义机器人云台对象
    ep_gimbal = ep_robot.gimbal
    #定义机器人发射器对象
    ep_blaster = ep_robot.blaster 
    
    #控制云台回中
    ep_gimbal.moveto(pitch=0, yaw=0, pitch_speed=100, yaw_speed=100).wait_for_completed()

    slp =3
    # 控制云台向右以30°/s的速度旋转
    ep_gimbal.drive_speed(pitch_speed=0, yaw_speed=30)
    #延迟3s
    time.sleep(slp)

    # 控制云台向左以30°/s的速度旋转
    ep_gimbal.drive_speed(pitch_speed=0, yaw_speed=-30)
    #延迟3s
    time.sleep(slp)

    # 控制云台向上以10°/s的速度旋转
    ep_gimbal.drive_speed(pitch_speed=10, yaw_speed=0)
    #延迟3s
    time.sleep(slp)

    #控制云台向下以10°/s的速度旋转
    ep_gimbal.drive_speed(pitch_speed=-10, yaw_speed=0)
    #延迟3s
    time.sleep(slp)

    # 发射2颗红外子弹
    ep_blaster.fire(fire_type=blaster.INFRARED_FIRE, times=2)
    time.sleep(2)


    #控制云台回中
    ep_gimbal.moveto(pitch=0, yaw=0, pitch_speed=100, yaw_speed=100).wait_for_completed()

    ep_robot.close()
