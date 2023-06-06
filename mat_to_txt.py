from scipy.io import loadmat
import numpy as np
import os

matdata = loadmat(r"D:\PostGraduate\pythonex\DATASET\ShanghaiTech_Crowd_Counting_Dataset\part_A_final\train_data\ground_truth\GT_IMG_1.mat")
print(matdata.keys())  # dict_keys(['__header__', '__version__', '__globals__', 'image_info'])
data = matdata['image_info']
save_path = r"D:\PostGraduate\pythonex\DATASET\ShanghaiTech_Crowd_Counting_Dataset"
np.savetxt(save_path, data, fmt='%s')
