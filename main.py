import cv2
import numpy as np
import pandas as pd
import argparse

'''Argument parser to take smth from terminal'''
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Image path')
args = vars(ap.parse_args())
img_path = args['image']

