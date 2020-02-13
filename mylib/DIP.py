# -*- coding: UTF-8 -*-

from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt  # 用于显示图片
import matplotlib.image as mping  # 用于读取图片
from PIL import ImageFilter  # 滤波器
import numpy as np
import os
import math

'''
# 亮度增强
enh_bri = ImageEnhance.Brightness(image)
brightness = 1.5
image_brightened = enh_bri.enhance(brightness)
image_brightened.show()

# 色度增强
enh_col = ImageEnhance.Color(image)
color = 1.5
image_colored = enh_col.enhance(color)
image_colored.show()

# 对比度增强
enh_con = ImageEnhance.Contrast(image)
contrast = 1.5
image_contrasted = enh_con.enhance(contrast)
image_contrasted.show()

# 锐度增强
enh_sha = ImageEnhance.Sharpness(image)
sharpness = 3.0
image_sharped = enh_sha.enhance(sharpness)
image_sharped.show()
'''


def gamma_correction(c, gamma, array):
    # 伽马变换 s = c * r^gamma
    # gamma < 1，会拉伸图像灰度级低的地区

    array = c * np.power(array, gamma)
    return array

def log_transform(c, N, array):
    # 对数变换 s = c * log_N[1+(N-1)*r]
    # N 越大，对低灰度值部分的扩展越强

    array = c * np.log(1+(N-1)*array)/np.log(N)
    return array




if __name__ == '__main__':
    im = Image.open('../test/page_9.png')  # 打开图片
    # im.show()
    # print(im.format,im.size,im.mode)

    # im_new = Image.new('RGB',(256,256))   # 创建新图
    rate = 1.2
    im_array = np.array(im)  # 将 PIL Image 图片转换为 numpy 数组

    # im_filtered = im.filter(ImageFilter.SMOOTH)  # filter参数：检测边缘
    # im_filtered.show()
    # im_filtered.save('../test/page_9_filtered.png')

    # enh_sha = ImageEnhance.Sharpness(im)
    # sharpness = 3.0
    # image_sharped = enh_sha.enhance(sharpness)
    # image_sharped.show()

    # im_filtered = image_sharped.filter(ImageFilter.SMOOTH)  # filter参数：检测边缘
    # im_filtered.show()
    # im_filtered.save('../test/page_9_filtered.png')

    width,height = im.size
    width_big = math.floor(width*rate)
    height_big = math.floor(height*rate)
    im_new = im.resize((width_big,height_big),Image.ANTIALIAS)
    im_new.save('../page_9_big.png')

    # 读取三个信道的数据
    data_1 = im_array[:, :, 0]/np.max(im_array)
    data_2 = im_array[:, :, 1]/np.max(im_array)
    data_2 = im_array[:, :, 1]/np.max(im_array)

    print(np.max(data_1))

    '''
    # L = im.convert('L')
    # L.show()
    # L.save('../test/new_page_0.png')
    '''
