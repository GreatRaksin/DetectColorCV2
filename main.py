import cv2
import numpy as np
import pandas as pd
import argparse

'''Argument parser to take smth from terminal'''
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Image path')
args = vars(ap.parse_args())
img_path = args['image']

'''Reading image with CV2'''
image = cv2.imread(img_path)

'''reading csv'''
index = ['color', 'color_name', 'HEX', 'R', 'G', 'B']  # пишем заголовки к Таблице
csv = pd.read_csv('color.csv', names=index, header=None)  # читаем csv как таблицу
print(csv)