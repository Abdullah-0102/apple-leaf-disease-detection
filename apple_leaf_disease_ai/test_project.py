import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import sklearn
import tensorflow as tf
import keras
from PIL import Image
import plotly

print('='*50)
print('  APPLE LEAF DISEASE AI - PROJECT HEALTH CHECK')
print('='*50)
print()

# 1. Library versions
print('[1/3] Library Imports & Versions')
print('-'*40)
libs = {
    'numpy':        np.__version__,
    'pandas':       pd.__version__,
    'matplotlib':   matplotlib.__version__,
    'seaborn':      sns.__version__,
    'opencv':       cv2.__version__,
    'scikit-learn': sklearn.__version__,
    'tensorflow':   tf.__version__,
    'keras':        keras.__version__,
    'pillow':       Image.__version__,
    'plotly':       plotly.__version__,
}
for lib, ver in libs.items():
    print(f'  [OK] {lib:<15} {ver}')
print()

# 2. Dataset check (train / val / test structure)
import os

dataset_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset')
expected_classes = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy']
splits = ['train', 'val', 'test']

print('[2/3] Dataset Verification')
print('-'*40)

all_ok = True
grand_total = 0

for split in splits:
    split_dir = os.path.join(dataset_dir, split)
    if not os.path.isdir(split_dir):
        print(f'  [MISSING] {split}/ directory not found')
        all_ok = False
        continue
    split_total = 0
    for cls in expected_classes:
        cls_path = os.path.join(split_dir, cls)
        if os.path.isdir(cls_path):
            count = len([f for f in os.listdir(cls_path)
                         if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
            split_total += count
            print(f'  [OK] {split}/{cls}: {count} images')
        else:
            print(f'  [MISSING] {split}/{cls}')
            all_ok = False
    grand_total += split_total
    print(f'       {split} subtotal: {split_total}')
    print()

print(f'  Total images across all splits: {grand_total}')
print()

# 3. Image load test
print('[3/3] Image Load Test')
print('-'*40)
test_class = expected_classes[0]
test_dir = os.path.join(dataset_dir, 'train', test_class)
if os.path.isdir(test_dir):
    test_files = [f for f in os.listdir(test_dir)
                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if test_files:
        test_img_path = os.path.join(test_dir, test_files[0])
        img_cv = cv2.imread(test_img_path)
        img_pil = Image.open(test_img_path)
        print(f'  Sample: {test_files[0]}')
        print(f'  OpenCV shape : {img_cv.shape}')
        print(f'  PIL size     : {img_pil.size}')
        print(f'  [OK] Images load correctly with both OpenCV and PIL')
    else:
        print(f'  [WARN] No image files found in {test_dir}')
        all_ok = False
else:
    print(f'  [WARN] Cannot run load test — train/{test_class} missing')
    all_ok = False

print()
print('='*50)
if all_ok:
    print('  ALL CHECKS PASSED - Project is ready!')
else:
    print('  SOME CHECKS FAILED - See above')
print('='*50)
