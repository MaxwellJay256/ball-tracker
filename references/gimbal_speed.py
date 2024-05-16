# -*-coding:utf-8-*-

import time
import robomaster
from robomaster import robot


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    #�����������̨����
    ep_gimbal = ep_robot.gimbal
    #��������˷���������
    ep_blaster = ep_robot.blaster 
    
    #������̨����
    ep_gimbal.moveto(pitch=0, yaw=0, pitch_speed=100, yaw_speed=100).wait_for_completed()

    slp =3
    # ������̨������30��/s���ٶ���ת
    ep_gimbal.drive_speed(pitch_speed=0, yaw_speed=30)
    #�ӳ�3s
    time.sleep(slp)

    # ������̨������30��/s���ٶ���ת
    ep_gimbal.drive_speed(pitch_speed=0, yaw_speed=-30)
    #�ӳ�3s
    time.sleep(slp)

    # ������̨������10��/s���ٶ���ת
    ep_gimbal.drive_speed(pitch_speed=10, yaw_speed=0)
    #�ӳ�3s
    time.sleep(slp)

    #������̨������10��/s���ٶ���ת
    ep_gimbal.drive_speed(pitch_speed=-10, yaw_speed=0)
    #�ӳ�3s
    time.sleep(slp)

    # ����2�ź����ӵ�
    ep_blaster.fire(fire_type=blaster.INFRARED_FIRE, times=2)
    time.sleep(2)


    #������̨����
    ep_gimbal.moveto(pitch=0, yaw=0, pitch_speed=100, yaw_speed=100).wait_for_completed()

    ep_robot.close()
