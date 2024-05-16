import cv2  # 引入opencv模块

def on_bgr_value_change(args):  # 定义回调函数on_bgr_value_change
    # 获取img_bgr窗口上的名为lower_b滑动条的当前值
    lower_b_value = cv2.getTrackbarPos('lower_b', 'img_bgr')
    # 获取img_bgr窗口上的名为upper_b滑动条的当前值
    upper_b_value = cv2.getTrackbarPos('upper_b', 'img_bgr')
    # 获取img_bgr窗口上的名为lower_g滑动条的当前值
    lower_g_value = cv2.getTrackbarPos('lower_g', 'img_bgr')
    # 获取img_bgr窗口上的名为upper_g滑动条的当前值
    upper_g_value = cv2.getTrackbarPos('upper_g', 'img_bgr')
    # 获取img_bgr窗口上的名为lower_r滑动条的当前值
    lower_r_value = cv2.getTrackbarPos('lower_r', 'img_bgr')
    # 获取img_bgr窗口上的名为upper_r滑动条的当前值
    upper_r_value = cv2.getTrackbarPos('upper_r', 'img_bgr')
    ''' 
    彩色图像分割,img_bgr中像素值位于
    阈值(lower_b_value, lower_g_value, lower_r_value)到
    (upper_b_value, upper_g_value, upper_r_value)范围内的为255,
    阈值范围外为0,输出分割得到的二值图
    '''
    '''
    若获取红色阈值，应调整滑动条，使bgr_divide_binary中红色小球区域为白色，
    其他颜色区域为黑色，从而获得红色阈值(lower_b,lower_g,lower_r),(upper_b,upper_g,upper_r)
    同理，需要获取蓝色阈值，黄色阈值，以及绿色阈值
    '''
    bgr_divide_binary = cv2.inRange(img_bgr, (lower_b_value, lower_g_value, lower_r_value),
                                    (upper_b_value, upper_g_value, upper_r_value))
    cv2.imshow('bgr_divide_binary', bgr_divide_binary)  # 输出显示分割得到的感兴趣区域

# 读取本地图像,并赋值给img_bgr, 默认为bgr三通道图像
# 将图像保存为本地图像可以调用cv2.imwrite(file_name, img)方法，file_name为要保存的文件名，img为要保存的图像数据
# 如可以在get_image.py中，得到img图像数据后调用cv2.imwrite("D:\\class_test\\img.jpg", img)，将img图像保存到D盘#class_test文件夹内并命名为img.jpg
#然后就可以在该文件bgr_segementation中读取本地图像D:\class_test\img.jpg了
img_bgr = cv2.imread('D:\\class_test\\img.jpg')
cv2.namedWindow('img_bgr', cv2.WINDOW_NORMAL)  # 创建img_bgr窗口
# 在img_bgr窗口上创建lower_b进度条,范围为0-255,回调函数为on_bgr_value_change
cv2.createTrackbar('lower_b', 'img_bgr', 0, 255, on_bgr_value_change)
# 在img_bgr窗口上创建upper_b进度条,范围为0-255,回调函数为on_bgr_value_change
cv2.createTrackbar('upper_b', 'img_bgr', 0, 255, on_bgr_value_change)
# 在img_bgr窗口上创建lower_g进度条,范围为0-255,回调函数为on_bgr_value_change
cv2.createTrackbar('lower_g', 'img_bgr', 0, 255, on_bgr_value_change)
# 在img_bgr窗口上创建upper_g进度条,范围为0-255,回调函数为on_bgr_value_change
cv2.createTrackbar('upper_g', 'img_bgr', 0, 255, on_bgr_value_change)
# 在img_bgr窗口上创建lower_r进度条,范围为0-255,回调函数为on_bgr_value_change
cv2.createTrackbar('lower_r', 'img_bgr', 0, 255, on_bgr_value_change)
# 在img_bgr窗口上创建upper_r进度条,范围为0-255,回调函数为on_bgr_value_change
cv2.createTrackbar('upper_r', 'img_bgr', 0, 255, on_bgr_value_change)
cv2.imshow('img_bgr', img_bgr)  # 在img_bgr窗口中显示图像img_bgr

if cv2.waitKey() == ord('q'):  # 如果按键输入q
    cv2.destroyAllWindows()  # 销毁所有窗口
