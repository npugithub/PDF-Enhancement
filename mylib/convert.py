# -*- coding: UTF-8 -*-

# PDF < -- > PNGs
from pdf2image import convert_from_path,convert_from_bytes

import tempfile

from img2pdf import convert

import os

def pdf2png(filename, outputDir):
    print('filename =', filename)
    print('outputDir =', outputDir)
    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path(filename)
        for index, img in enumerate(images):
            img.save('%s/page_%s.png' % (outputDir, index))


def png2pdf(inputDir,filename):
    print('inputDir = ',inputDir)
    print('filename = ',filename)
    temp = os.listdir(inputDir)
    with open(filename, "wb") as f:
        for i in range(len(temp)):
            temp[i] = inputDir + '/' + temp[i]
        f.write(convert(temp))
