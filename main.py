# -*- coding: UTF-8 -*-

from mylib import info
# from mylib import DIP
from mylib import convert

import os



def makedir(pdf_name):
    png_dir = pdf_name[:-4]
    if not os.path.exists(png_dir):
        os.mkdir(png_dir)
    else:
        pass
    return png_dir


if __name__ == '__main__':
    pdf_name = 'test.pdf'
    current_path = os.getcwd() + '/'
    pdf_name_new = pdf_name[:-4]+'_converted'+pdf_name[-4:]

    # 获取原PDF的信息
    information = info.get_info(pdf_name)
    # print(information['author'])

    # 创建PDF对应的图片文件夹
    png_dir = makedir(pdf_name)

    # PDF 转换为 PNGs
    convert.pdf2png(pdf_name, png_dir)



    # 图像增强



    # PNGs 转化为 PDF
    convert.png2pdf(png_dir, pdf_name_new)









